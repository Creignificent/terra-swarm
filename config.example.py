# Copy to config.py and fill in values.
# Prefer local / free endpoints where possible.

LLM_PROVIDER = "ollama"  # or "openai", "groq", etc.
LLM_BASE_URL = "http://localhost:11434"
LLM_MODEL = "qwen2.5:7b"

# Optional external APIs
STRIPE_SECRET_KEY = ""
SHIPPING_API_KEY = ""

# Paths
DATA_DIR = "data"
LOG_DIR = "logs"
