from pyrogram import Client, filters, idle
from pyrogram.types import Message
import pyrogram
from Config import Config
app = Client(
    "MentionAll",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

@app.on_message(filters.command("start"))
async def _py(client: Client, message: Message):
    message.reply_text('Pyrogram is a Python library for Telegram bots.')

app.start()
print(f"Bot pyrogram ( {pyrogram.__version__} sürümü ile başlatıldı. ")
idle()
