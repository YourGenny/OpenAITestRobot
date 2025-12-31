from pyrogram import Client, filters
from config import ALLOWED_CHATS
from vc import pytgcalls

@Client.on_message(filters.command("resume") & filters.chat(ALLOWED_CHATS))
async def resume(client, message):
    await pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("▶️ Music resumed")