import { useEffect, useMemo, useState } from 'react'

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

function Section({ title, children }) {
  return (
    <section className="card">
      <h2>{title}</h2>
      {children}
    </section>
  )
}

export default function App() {
  const [dashboard, setDashboard] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    async function load() {
      try {
        const companiesRes = await fetch(`${API_BASE}/api/companies`)
        const companies = await companiesRes.json()
        const companyId = companies?.[0]?.company_id
        if (!companyId) return

        const dashboardRes = await fetch(`${API_BASE}/api/companies/${companyId}/dashboard`)
        const data = await dashboardRes.json()
        setDashboard(data)
      } catch (e) {
        setError(e.message)
      }
    }

    load()
  }, [])

  const summary = useMemo(() => {
    if (!dashboard) return null
    const cm = dashboard.company_master
    const latestMetrics = dashboard.computed_metrics?.[0]?.metrics || {}
    return {
      name: cm.company_name,
      ticker: cm.tickers?.[0]?.symbol,
      sector: cm.sector,
      categories: cm.category_tags?.join(' · '),
      netCash: latestMetrics.net_cash_inr,
      ebitMargin: latestMetrics.ebit_margin_pct,
      dso: latestMetrics.dso_days
    }
  }, [dashboard])

  if (error) return <div className="error">Failed to load dashboard: {error}</div>
  if (!dashboard || !summary) return <div className="loading">Loading dashboard...</div>

  const thesis = dashboard.qualitative_frameworks?.thesis
  const moatMap = dashboard.qualitative_frameworks?.moat_map
  const killShots = dashboard.qualitative_frameworks?.kill_shots || []
  const ownership = dashboard.ownership_governance?.[0]

  return (
    <main>
      <header className="sticky">
        <div>
          <h1>{summary.name} ({summary.ticker})</h1>
          <p>{summary.sector}</p>
        </div>
        <div className="chips">
          <span>{summary.categories}</span>
          <span>EBIT Margin: {summary.ebitMargin}%</span>
          <span>DSO: {summary.dso} days</span>
          <span>Net Cash: ₹{summary.netCash}</span>
        </div>
      </header>

      <Section title="Thesis Card">
        <p>{thesis.business_summary}</p>
        <h3>Must be true</h3>
        <ul>{thesis.must_be_true.map((item) => <li key={item}>{item}</li>)}</ul>
        <h3>Key risks</h3>
        <ul>{thesis.key_risks.map((item) => <li key={item}>{item}</li>)}</ul>
      </Section>

      <Section title="Moat Map + Half-Life">
        <p>Half-life: <strong>{moatMap.moat_half_life_band}</strong></p>
        <ul>
          {moatMap.moats.map((moat) => (
            <li key={moat.moat_type}>{moat.moat_type}: {moat.score_0_5}/5</li>
          ))}
        </ul>
      </Section>

      <Section title="Ownership + Governance">
        <div className="grid">
          <p>Promoter Holding: {ownership.promoter_holding_pct}%</p>
          <p>Promoter Pledge: {ownership.promoter_pledge_pct}%</p>
          <p>FII: {ownership.fii_holding_pct}%</p>
          <p>DII: {ownership.dii_holding_pct}%</p>
        </div>
      </Section>

      <Section title="Kill-shots + Early Warnings">
        {killShots.map((shot) => (
          <article key={shot.risk} className="killshot">
            <h3>{shot.risk}</h3>
            <p>{shot.why_it_kills}</p>
            <ul>
              {shot.early_indicators.map((indicator) => (
                <li key={indicator.indicator}>{indicator.indicator} ({indicator.threshold})</li>
              ))}
            </ul>
          </article>
        ))}
      </Section>
    </main>
  )
}
