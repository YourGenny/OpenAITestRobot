import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

# Allowed GC IDs (replace with your own)
ALLOWED_CHATS = [-1003284051384, -1003199415158]