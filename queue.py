queue = {}

def add_song(chat_id, song_file):
    if chat_id not in queue:
        queue[chat_id] = []
    queue[chat_id].append(song_file)

def get_next(chat_id):
    if chat_id in queue and queue[chat_id]:
        return queue[chat_id].pop(0)
    return None