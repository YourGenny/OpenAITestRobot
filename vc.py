from pyrogram import Client
from pytgcalls import PyTgCalls
from config import SESSION_STRING, API_ID, API_HASH

assistant = Client(session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)
pytgcalls = PyTgCalls(assistant)

async def start_vc(chat_id, audio_file):
    await pytgcalls.join_group_call(
        chat_id,
        input_file=audio_file,
        stream_type='local_stream'
    )

async def leave_vc(chat_id):
    await pytgcalls.leave_group_call(chat_id)