import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message




api_id = 26597515
api_hash = "e556b966e7192209f7f419b07de8cc6a"
bot_token = "7379409256:AAHiIQV-AJYk-JfcaEgg2tSgXh6juk0C1CU"



app = Client(
    "ask_test",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token 
)



@app.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply("Ben test deneme botuyum")


  
@app.on_message(filters.command("botcum") & filters.group) 
async def botcum(client, message):
  
  if message.from_user.id == 6905940236:
    await message.reply_text("**Sayın böcük hanım şuan çalışmaktayım 🇹🇷🤍**")
 
  elif message.from_user.id == 7142242630:
    await message.reply_text("sassy abla şuan çalışıyorum Merak etme 🥺👉👈**")
    
  elif message.from_user.id == 7131686379:
    await message.reply_text("**tırrek lili seviliyorsun bilesinnn**🌸💕")

  elif message.from_user.id == 7182074621:
    await message.reply_text("**sahibimin küçük adamı**🩵")

  elif message.from_user.id == 2040437974:
    await message.reply_text("**sayın hocamız değerli hocamız✨🤍**")
    
  elif message.from_user.id == 6604549799:
    await message.reply_text("dayımda dayım baş tacımız 👑❤️")
         
  elif message.from_user.id == 6716279900:
    await message.reply_text("** sek sek seqooo 🌸❤️‍🔥**")

  elif message.from_user.id == 6423044130:
    await message.reply_text("** Google perisi💫💕**") 

  else:
    await message.reply_text("__Seni tanımıyorum sen kimsin__ 🙈")
app.run()
