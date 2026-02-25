#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND_DIR="$ROOT_DIR/backend"
FRONTEND_DIR="$ROOT_DIR/frontend"

BACKEND_HOST="${BACKEND_HOST:-0.0.0.0}"
BACKEND_PORT="${BACKEND_PORT:-8000}"
FRONTEND_HOST="${FRONTEND_HOST:-0.0.0.0}"
FRONTEND_PORT="${FRONTEND_PORT:-5173}"

DATABASE_URL="${DATABASE_URL:-postgresql+psycopg2://postgres:postgres@localhost:5432/sector_analysis}"
export DATABASE_URL
export VITE_API_BASE="${VITE_API_BASE:-http://localhost:${BACKEND_PORT}}"

BACKEND_PID=""
FRONTEND_PID=""

cleanup() {
  set +e
  if [[ -n "$BACKEND_PID" ]] && kill -0 "$BACKEND_PID" 2>/dev/null; then
    kill "$BACKEND_PID"
  fi
  if [[ -n "$FRONTEND_PID" ]] && kill -0 "$FRONTEND_PID" 2>/dev/null; then
    kill "$FRONTEND_PID"
  fi
}
trap cleanup EXIT INT TERM

echo "[run-local] Root: $ROOT_DIR"
echo "[run-local] DATABASE_URL=$DATABASE_URL"
echo "[run-local] VITE_API_BASE=$VITE_API_BASE"

if ! command -v python >/dev/null 2>&1; then
  echo "[run-local] ERROR: python is required"
  exit 1
fi
if ! command -v npm >/dev/null 2>&1; then
  echo "[run-local] ERROR: npm is required"
  exit 1
fi

if [[ ! -d "$BACKEND_DIR/.venv" ]]; then
  echo "[run-local] Creating backend virtualenv..."
  python -m venv "$BACKEND_DIR/.venv"
fi

source "$BACKEND_DIR/.venv/bin/activate"
if ! python -c "import fastapi" >/dev/null 2>&1; then
  echo "[run-local] Installing backend dependencies..."
  pip install -r "$BACKEND_DIR/requirements.txt"
fi

if [[ ! -d "$FRONTEND_DIR/node_modules" ]]; then
  echo "[run-local] Installing frontend dependencies..."
  (cd "$FRONTEND_DIR" && npm install)
fi

echo "[run-local] Starting backend on ${BACKEND_HOST}:${BACKEND_PORT}"
(
  cd "$BACKEND_DIR"
  source .venv/bin/activate
  uvicorn app.main:app --reload --host "$BACKEND_HOST" --port "$BACKEND_PORT"
) &
BACKEND_PID=$!

echo "[run-local] Starting frontend on ${FRONTEND_HOST}:${FRONTEND_PORT}"
(
  cd "$FRONTEND_DIR"
  npm run dev -- --host "$FRONTEND_HOST" --port "$FRONTEND_PORT"
) &
FRONTEND_PID=$!

echo "[run-local] App is starting..."
echo "[run-local] Frontend: http://localhost:${FRONTEND_PORT}"
echo "[run-local] Backend:  http://localhost:${BACKEND_PORT}"
echo "[run-local] Press Ctrl+C to stop both services"

wait "$BACKEND_PID" "$FRONTEND_PID"
