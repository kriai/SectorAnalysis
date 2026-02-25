# Sector Analysis Dashboard MVP

Full-stack MVP using **FastAPI + React + Postgres** for an India-listed software company analysis dashboard.

## Stack

- Backend: FastAPI, SQLAlchemy
- Frontend: React (Vite)
- Database: Postgres
- Optional orchestration: Docker Compose

## Quick start (Docker)

```bash
docker compose up --build
```

- API: `http://localhost:8000`
- Frontend: `http://localhost:5173`

---

## One-command local run (no Docker)

### Prerequisites

- PostgreSQL running locally on `localhost:5432`
- Python + `venv`
- Node.js + npm

Create DB (once):

```sql
CREATE DATABASE sector_analysis;
```

### Command

```bash
make run-local
```

What this command does:

1. Creates `backend/.venv` if missing
2. Installs backend deps if missing
3. Installs frontend deps if missing
4. Starts FastAPI on `http://localhost:8000`
5. Starts React on `http://localhost:5173`

Stop everything with `Ctrl+C`.

### Optional environment overrides

```bash
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/sector_analysis \
BACKEND_PORT=8000 \
FRONTEND_PORT=5173 \
make run-local
```

---

## API endpoints

- `GET /health`
- `GET /api/companies`
- `GET /api/companies/{company_id}/dashboard`

Backend seeds one sample company (`NSE-INFY`) on startup if missing.

## Common local issues

- `connection refused` on backend startup: Postgres is not running or credentials in `DATABASE_URL` are wrong.
- Frontend shows loading forever: ensure backend is running and `VITE_API_BASE` points to backend URL.
- Port already in use: set `BACKEND_PORT` / `FRONTEND_PORT` before `make run-local`.
