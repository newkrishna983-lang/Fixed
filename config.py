import os

def env_int(name, default=0):
    try:
        return int(os.getenv(name, default))
    except ValueError:
        return default

API_ID = env_int("API_ID", "34422904")
API_HASH = os.getenv("API_HASH", "7e0002469784f47fc08a6b3d93d7ebed")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8638398538:AAGd0NJuGoMEGbY2Zx7d1RHF8z6gaZ5PVo4")

OWNER_ID = env_int("OWNER_ID", "5349573682")
SUDO_USERS = [int(x) for x in os.getenv("SUDO_USERS", "").split() if x.isdigit()]

MONGO_URL = os.getenv("MONGO_URL", "")
CHANNEL_ID = env_int("CHANNEL_ID", "")
PREMIUM_LOGS = os.getenv("PREMIUM_LOGS", "")
