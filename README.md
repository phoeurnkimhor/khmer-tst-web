# KhmerTST Web

## Containers

- Backend: Python FastAPI (dev) on port 8000
- Frontend: Node.js dev server on port 3000
- Database: Supabase Postgres (hosted), no local DB container

## Setup

- Copy `.env.example` to `.env` and fill `SUPABASE_DB_URL` from your Supabase project.
- Optional: adjust `API_URL` for the frontend.

## Run

```sh
docker compose up --build
```

Backend serves a basic `/health` endpoint at `http://localhost:8000/health`.