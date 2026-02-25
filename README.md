# Sector Analysis Dashboard MVP

Full-stack MVP using **FastAPI + React + Postgres** for an India-listed software company analysis dashboard.

## Stack

- Backend: FastAPI, SQLAlchemy
- Frontend: React (Vite)
- Database: Postgres
- Orchestration: Docker Compose

## Quick start (Docker)

```bash
docker compose up --build
```

- API: `http://localhost:8000`
- Frontend: `http://localhost:5173`

## Local backend run

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/sector_analysis
uvicorn app.main:app --reload
```

## API endpoints

- `GET /health`
- `GET /api/companies`
- `GET /api/companies/{company_id}/dashboard`

The backend seeds one sample company (`NSE-INFY`) on startup if missing.
