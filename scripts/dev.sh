#!/usr/bin/env bash

set -euo pipefail

trap "pkill -P $$ || true" EXIT

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source ./.venv/bin/activate
pip -q install -r backend/requirements.txt

uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

cd frontend
if [ ! -d "node_modules" ]; then
    npm i --silent
fi

npm run dev
