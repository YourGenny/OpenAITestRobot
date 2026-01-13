from pyrogram import Client, filters
from config import ALLOWED_CHATS
from vc import pytgcalls

@Client.on_message(filters.command("pause") & filters.chat(ALLOWED_CHATS))
async def pause(client, message):
    await pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("⏸ Music paused")