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

    @app.on_message(filters.command("botcum") &filters .private)
    async def botcum (client, mesaage):
        if message .form_user.id ==
    6905940236:
             await message.reply_text("**
    Sayın böcük hanım şuan çalışmaltayım 🇹🇷🤍**")
        elif message .form_user.id ==
    7142242630:
            await
    message.reply("sassy abla şuan çalışıyorum Merak etme 🥺👉👈**")
        if message .form_user.id ==
    7131686379:
            await message.reply_text("** 
     tırrek lili seviliyorsun bilesinnn🌸💕**")
         if message .form_user.id ==
    7182074621:
            await message.reply_text("**
            sahibimin küçük adamı🩵**")
         if message .form_user.id ==
    2040437974:
            await message.reply_text("**
            sayın hocamız değerli hocamız✨🤍**")
         if message .form_user.id ==
    6604549799:
            await message.reply_text("** dayımda dayım baş 
            tacımız 👑❤️**")
         if mesaage .fırm_user.id ==
    6716279900:
            await message.reply_next("** sek sek seqooo 🌸❤️‍🔥**")

app.run()
