# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21188057"))
API_HASH = getenv("API_HASH", "8564fab8db759bb04b1907bd12ed98ef")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6976744562 8102446291 21188057").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")
LOG_GROUP = getenv("LOG_GROUP", "-1002451145033")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002303215395"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
