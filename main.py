import asyncio
from pyrogram import Client
from pyrogram.idle import idle
from config import BOT_TOKEN, API_ID, API_HASH, SESSION_STRING
from vc import assistant, pytgcalls
import handlers.play  # import all handlers
import handlers.pause
# import other handlers similarly

app = Client("bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

async def main():
    await assistant.start()
    await pytgcalls.start()
    await app.start()
    print("✅ Music Bot is running...")
    await idle()  # keep running
    await app.stop()
    await assistant.stop()

if __name__ == "__main__":
    asyncio.run(main())