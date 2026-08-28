# DarEvents — Automated Events Platform (Tanzania)

**Jukwaa la matukio linalojisimamia** — data inakusanywa otomatiki kwa Tavily + AI.

## Features

- ✅ **Automated collection** (Tavily + AI structured extraction)
- ✅ **Sponsored / Ads always first**
- ✅ **Anyone can post an event** (“Weka Tukio”) — free for now + duration selector (demo $1 / 2 days)
- ✅ **Like 👍 / Dislike 👎** → Trending score
- ✅ Images support (`image_url`)
- ✅ Self-managing: dedup, expire old, max 300
- ✅ Polished Swahili frontend (stronger than local competitors)
- ✅ M-Pesa ready UI, filters, map, digest
- ✅ Ready for cron / Docker / any VPS

## Project Structure

```
darevents/
├── backend/
│   ├── main.py          # FastAPI app
│   ├── collector.py     # Tavily + AI collector
│   ├── config.py
│   ├── models.py
│   └── requirements.txt
├── frontend/
│   └── index.html       # Dynamic UI (fetches /api/events)
├── data/
│   ├── events.json      # Live events (auto-updated)
│   └── sponsored.json
├── scripts/
│   └── run_collector.sh
├── .env.example
├── Dockerfile
└── README.md
```

## Quick Start (Local)

```bash
cd darevents/backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Seed demo data (works without keys)
python collector.py seed

# Run API + frontend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000

## Production (Server)

1. Copy `.env.example` → `.env` and put your real keys:
   ```
   TAVILY_API_KEY=tvly-...
   OPENAI_API_KEY=...          # or xAI key
   AI_BASE_URL=https://api.x.ai/v1   # if using Grok
   AI_MODEL=grok-beta
   ```

2. Install & run:
   ```bash
   pip install -r backend/requirements.txt
   cd backend
   python collector.py seed          # first time
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

3. **Auto-collect every 6 hours** (cron example):
   ```cron
   0 */6 * * * cd /path/to/darevents/backend && /path/to/venv/bin/python collector.py >> /var/log/darevents-collect.log 2>&1
   ```

4. Trigger manually:
   ```bash
   curl -X POST http://localhost:8000/api/collect
   ```

## Sponsored Events (Ads first)

```bash
curl -X POST "http://localhost:8000/api/sponsored/EVENT_ID?sponsored=true"
```

## Like / Dislike (Trending)

```bash
curl -X POST "http://localhost:8000/api/events/EVENT_ID/vote?vote=like"
curl -X POST "http://localhost:8000/api/events/EVENT_ID/vote?vote=dislike"
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/events` | List events (sponsored first, optional `sort=trending`) |
| GET | `/api/events/{id}` | Single event |
| POST | `/api/events/submit` | Anyone can post an event (free) |
| POST | `/api/events/{id}/vote` | Like or dislike |
| POST | `/api/collect` | Trigger collection |
| POST | `/api/seed` | Seed demo data |
| POST | `/api/sponsored/{id}` | Mark/unmark sponsored |
| GET | `/api/health` | Health check |
| GET | `/docs` | Swagger UI |

## Notes

- Without API keys the site still works with the seeded demo events.
- Put keys **only** in server `.env` — never in frontend or git.
- Ticket sales: external links for now; optional low commission can be added later.
- Google Ads: recommended only after real user reactions.
