from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from telethon import TelegramClient
from telethon.tl.types import MessageMediaDocument
import os, re, asyncio, nest_asyncio

# --- Setup ---
nest_asyncio.apply()
app = Flask(__name__)
CORS(app)

api_id = 0000000 # your api id
api_hash = 'YOUR_API_HASH'
directory = 'Credentials'
DOWNLOAD_DIR = 'Downloads'
with TelegramClient('Credentials', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Connected You With Telegram Server Now Enjoy'))
local_client = TelegramClient('Credentials', api_id, api_hash)   

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/api/telegram')
def telegram_download():
    url = request.args.get('url')

    async def fetch_video():
        try:
            parts = url.split('/')
            message_id = int(parts[-1])

            # ✅ Create a new client per request
            local_client = TelegramClient('Credentials', api_id, api_hash)
            await local_client.connect()

            if not await local_client.is_user_authorized():
                await local_client.disconnect()
                return {'success': False, 'error': 'Telegram client not authorized'}

            # ✅ Detect private (t.me/c) or public channels
            if "t.me/c/" in url:
                chat_id = int("-100" + parts[-2])
            else:
                entity = await local_client.get_entity(parts[-2])
                chat_id = entity.id

            msg = await local_client.get_messages(chat_id, ids=message_id)

            if msg.media and isinstance(msg.media, MessageMediaDocument):
             filename = f"{chat_id}_{message_id}.mp4"
             path = os.path.join(DOWNLOAD_DIR, filename)
              
             # ✅ Use low-level file downloader for speed
             input_location = msg.document
             with open(path, "wb") as f:
                async for chunk in local_client.iter_download(input_location, chunk_size=2 * 1024 * 1024):
                    f.write(chunk)
   
             await local_client.disconnect()
             return {'success': True, 'videoUrl': f'/video/{filename}'}

            else:
                await local_client.disconnect()
                return {'success': False, 'message': 'No media in message'}

        except Exception as e:
            return {'success': False, 'error': str(e)}


    return jsonify(asyncio.run(fetch_video()))

@app.route('/video/<filename>')
def serve_video(filename):
    path = os.path.join(DOWNLOAD_DIR, filename)
    if not os.path.exists(path):
        return "File not found", 404
    return send_file(path, as_attachment=True, download_name=filename)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
