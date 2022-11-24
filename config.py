import os

from dotenv.main import load_dotenv

load_dotenv()

# Discord config
TOKEN = os.getenv("TOKEN", "")
NAPKIN_TOKEN = os.getenv("NAPKIN_TOKEN", "")
EMAIL = os.getenv("EMAIL", "")
