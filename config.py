import os

def env_int(name, default=0):
    try:
        return int(os.getenv(name, default))
    except ValueError:
        return default

API_ID = env_int("API_ID")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

OWNER_ID = env_int("OWNER_ID")
SUDO_USERS = [int(x) for x in os.getenv("SUDO_USERS", "").split() if x.isdigit()]

MONGO_URL = os.getenv("MONGO_URL", "")
CHANNEL_ID = env_int("CHANNEL_ID")
PREMIUM_LOGS = os.getenv("PREMIUM_LOGS", "")
