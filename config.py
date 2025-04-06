from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://userbot:userbot@cluster0.yyijp36.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2b4e22e24548f55f40e65.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2b4e22e24548f55f40e65.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Bot4Chan")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CerenFm")
PLAYLIST = getenv("PLAYLIST", "https://t.me/CerenFm")

PLAYLIST_ID = int(getenv("PLAYLIST_ID", "-1002129397210"))


FAILED = "https://telegra.ph/file/2b4e22e24548f55f40e65.jpg"
