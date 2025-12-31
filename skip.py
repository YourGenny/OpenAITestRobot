from pyrogram import Client, filters
from config import ALLOWED_CHATS
from vc import leave_vc, start_vc
from utils.queue import get_next

@Client.on_message(filters.command("skip") & filters.chat(ALLOWED_CHATS))
async def skip(client, message):
    await leave_vc(message.chat.id)
    next_song = get_next(message.chat.id)
    if next_song:
        await start_vc(message.chat.id, next_song)
        await message.reply_text(f"⏭ Skipped. Now playing: {next_song}")
    else:
        await message.reply_text("⏹ No more songs in queue.")