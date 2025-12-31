from pyrogram import Client, filters
from config import ALLOWED_CHATS
from vc import leave_vc

@Client.on_message(filters.command("stop") & filters.chat(ALLOWED_CHATS))
async def stop(client, message):
    await leave_vc(message.chat.id)
    await message.reply_text("⏹ Music stopped.")