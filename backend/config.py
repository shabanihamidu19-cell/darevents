import os
from dotenv import load_dotenv

load_dotenv()

# API Keys (set these in .env on the server)
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")  # or xAI / Anthropic compatible
AI_BASE_URL = os.getenv("AI_BASE_URL", "https://api.openai.com/v1")  # change for xAI: https://api.x.ai/v1
AI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")  # or grok-beta, claude-3-5-sonnet etc.

# Paths
DATA_DIR = os.getenv("DATA_DIR", os.path.join(os.path.dirname(__file__), "..", "data"))
EVENTS_FILE = os.path.join(DATA_DIR, "events.json")
SPONSORED_FILE = os.path.join(DATA_DIR, "sponsored.json")

# Collection settings
CITIES = ["Dar es Salaam", "Arusha", "Mwanza", "Zanzibar", "Dodoma", "Mbeya"]
SEARCH_QUERIES = [
    "upcoming events Dar es Salaam Tanzania this week next month",
    "matukio yanayokuja Dar es Salaam 2026",
    "concerts festivals sports Dar es Salaam upcoming",
    "Eventbrite Dar es Salaam events",
    "Super Dome Dar es Salaam events",
    "live music nightlife Dar es Salaam this weekend",
]

# How many events to keep max
MAX_EVENTS = 300
# Days ahead to collect
DAYS_AHEAD = 60
