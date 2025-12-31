from pyrogram import Client, filters
from config import ALLOWED_CHATS
from utils.yt import download_audio
from vc import start_vc
from utils.queue import add_song

@Client.on_message(filters.command("play") & filters.chat(ALLOWED_CHATS))
async def play(client, message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        await message.reply_text("Usage: /play <song name or YouTube link>")
        return

    query = text[1]
    msg = await message.reply_text("🔄 Searching and downloading...")
    audio_file = await download_audio(query)
    add_song(message.chat.id, audio_file)
    await start_vc(message.chat.id, audio_file)
    await msg.edit(f"🎵 Now playing: {query}")