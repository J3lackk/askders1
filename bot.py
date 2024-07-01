import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message




api_id = 26597515
api_hash = "e556b966e7192209f7f419b07de8cc6a"
bot_token = "7379409256:AAFndQN5bxWkskWsdGbCyjg2d_MU3RIPKVI"



app = Client(
    "ask_test",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token 
)


@app.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply("Ben test deneme botuyum")

    


app.run()
