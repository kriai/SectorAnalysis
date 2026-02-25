SAMPLE_COMPANY_ID = "NSE-INFY"

SAMPLE_DASHBOARD = {
    "schema_version": "1.0",
    "company_master": {
        "company_id": SAMPLE_COMPANY_ID,
        "company_name": "Infosys Limited",
        "tickers": [{"exchange": "NSE", "symbol": "INFY"}, {"exchange": "BSE", "symbol": "500209"}],
        "sector": "IT Services",
        "category_tags": ["IT_SERVICES", "HYBRID"],
        "business_model_tags": ["SERVICES", "SUPPORT_AMC", "MIXED"],
        "primary_geographies": [
            {"region": "US", "share_pct": 60.0},
            {"region": "EU", "share_pct": 27.0},
            {"region": "INDIA", "share_pct": 3.0},
            {"region": "OTHER", "share_pct": 10.0}
        ]
    },
    "data_sources": {
        "documents": [
            {
                "doc_id": "DOC-INFY-AR-2024",
                "doc_type": "ANNUAL_REPORT",
                "exchange": "NSE",
                "period_end": "2024-03-31",
                "published_at": "2024-05-10",
                "title": "Annual Report FY24",
                "url": "https://www.nseindia.com/",
                "hash": None
            },
            {
                "doc_id": "DOC-INFY-Q1-2025",
                "doc_type": "QUARTERLY_RESULTS",
                "exchange": "NSE",
                "period_end": "2024-06-30",
                "published_at": "2024-07-18",
                "title": "Q1 FY25 Results",
                "url": "https://www.nseindia.com/",
                "hash": None
            }
        ],
        "extractions": [
            {
                "extract_id": "EX-INFY-001",
                "doc_id": "DOC-INFY-AR-2024",
                "field_path": "qualitative_frameworks.thesis.why_it_wins[0]",
                "value": "Large enterprise client relationships and delivery scale",
                "page_or_section": "CEO letter",
                "confidence": 0.9,
                "notes": "Manual extraction"
            }
        ]
    },
    "period_financials": [
        {
            "period_id": "FY24",
            "period_type": "FY",
            "period_end": "2024-03-31",
            "currency": "INR",
            "income_statement": {
                "revenue": 1536700,
                "cost_of_revenue": None,
                "gross_profit": None,
                "employee_cost": 853000,
                "other_opex": 331000,
                "ebitda": 352000,
                "ebit": 311000,
                "pat": 262000
            },
            "balance_sheet": {
                "cash_and_investments": 413000,
                "total_debt": 0,
                "trade_receivables": 272000,
                "contract_liabilities_or_deferred_revenue": 89000,
                "total_assets": 1712000
            },
            "cash_flow": {
                "cash_from_operations": 337000,
                "capex": 41000,
                "free_cash_flow": 296000
            },
            "segment_or_mix": {
                "services_revenue": 1440000,
                "product_license_revenue": 12000,
                "subscription_or_recurring_revenue": 40000,
                "support_amc_revenue": 44700
            },
            "operating_kpis_if_disclosed": {
                "headcount": 317000,
                "utilization_pct": 82.0,
                "attrition_pct": 14.7,
                "deal_wins_count": None,
                "large_deal_tcv": 171000
            },
            "citations": ["DOC-INFY-AR-2024"]
        }
    ],
    "ownership_governance": [
        {
            "period_end": "2024-06-30",
            "promoter_holding_pct": 14.6,
            "promoter_pledge_pct": 0,
            "fii_holding_pct": 33.8,
            "dii_holding_pct": 31.2,
            "public_holding_pct": 20.4,
            "rpt_summary": {
                "rpt_flag": False,
                "rpt_amount_inr": 0,
                "rpt_notes": "No material adverse RPT pattern detected"
            },
            "governance_flags": [],
            "citations": ["DOC-INFY-Q1-2025"]
        }
    ],
    "computed_metrics": [
        {
            "period_end": "2024-03-31",
            "metrics": {
                "revenue_yoy_growth_pct": 1.9,
                "revenue_qoq_growth_pct": None,
                "gross_margin_pct": None,
                "ebitda_margin_pct": 22.9,
                "ebit_margin_pct": 20.2,
                "pat_margin_pct": 17.0,
                "fcf_margin_pct": 19.3,
                "cash_conversion_cfo_over_ebitda": 0.96,
                "net_cash_inr": 413000,
                "dso_days": 64.6,
                "revenue_per_employee_inr": 4.85,
                "r_and_d_intensity_pct": 1.2,
                "employee_cost_pct_of_revenue": 55.5,
                "recurring_proxy_score_0_100": 58,
                "software_ness_score_0_100": 62,
                "governance_risk_score_0_100": 18
            },
            "formula_notes": {
                "dso_days": "trade_receivables / revenue * 365 (FY) or * 90 (quarter approx)",
                "net_cash_inr": "cash_and_investments - total_debt",
                "fcf_margin_pct": "free_cash_flow / revenue",
                "recurring_proxy_score_0_100": "weighted from contract_liabilities trend + support/AMC mix + mgmt commentary flags",
                "software_ness_score_0_100": "weighted from recurring_proxy + gross margin quality + scalability proxies"
            }
        }
    ],
    "qualitative_frameworks": {
        "thesis": {
            "business_summary": "Infosys is a scaled global IT services and digital transformation vendor with long-duration enterprise relationships.",
            "why_it_wins": [
                {
                    "moat_type": "COST_SCALE",
                    "claim": "Global delivery engine supports margin resilience at scale.",
                    "evidence_extract_ids": ["EX-INFY-001"],
                    "counter_extract_ids": []
                }
            ],
            "must_be_true": [
                "Large-deal pipeline converts into revenue at healthy margins.",
                "Attrition stays manageable for delivery continuity.",
                "DSO remains stable despite macro pressure."
            ],
            "key_risks": [
                "Delayed discretionary spending from US clients.",
                "Wage inflation compressing margins.",
                "Higher competition in AI-led transformation deals."
            ],
            "what_changes_my_mind": [
                "2+ quarters of margin contraction without recovery plan.",
                "Persistent rise in DSO above 80 days.",
                "Meaningful governance red flag filings."
            ]
        },
        "moat_map": {
            "moats": [
                {
                    "moat_type": "SWITCHING",
                    "score_0_5": 4,
                    "evidence": [{"text": "Multi-year managed services contracts", "extract_ids": ["EX-INFY-001"]}],
                    "counter_evidence": [{"text": "Price-led rebids in weak demand", "extract_ids": []}]
                }
            ],
            "moat_half_life_band": "5_10Y",
            "decay_drivers": ["AI commoditization", "Cloud-native challengers"],
            "reinforcers": ["Client wallet share expansion", "Automation investments"]
        },
        "kill_shots": [
            {
                "risk": "Margin compression spiral",
                "why_it_kills": "Sustained margin compression weakens valuation support and cash generation.",
                "early_indicators": [
                    {"indicator": "EBIT margin drops below 18%", "metric_key": "ebit_margin_pct", "threshold": "<18"},
                    {"indicator": "Employee cost rises above 60%", "metric_key": "employee_cost_pct_of_revenue", "threshold": ">60"}
                ],
                "citations": ["DOC-INFY-Q1-2025"]
            }
        ]
    }
}
