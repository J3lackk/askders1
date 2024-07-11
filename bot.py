import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



api_id = 26597515
api_hash = "e556b966e7192209f7f419b07de8cc6a"
bot_token = "7379409256:AAHVQ7mzZ82_SQL4N96g5Tndb1QZYxn5ujc"


app = Client(
    "ask_test",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token  
)



OWNER_ID = 7142242630


# /start komutunu özel mesajlarda dinleyen bir handler tanımlıyoruz.
@app.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
      # butonları içeren bir klavye oluşturuyoruz.
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [ 
                # ilk buton destek chatine yönlendiriliyor.
                InlineKeyboardButton(text="Destek 🎉", url="https://t.me/yikilmayanchat")
            ],
            [
                # ikinci buton sahibin profiline yönlendiriyor.
                InlineKeyboardButton(text="Sahip 🦄", url="https://t.me/simarikkizz")
            ]
        ]
    )
    # kullanıcıya yanıt olarak bir mesaj gönderiyoruz ve klavyeyi ekliyoruz.
    await message.reply(
        "Merhaba, ben test deneme butonuyum. Aşağıdaki butonlardan birini seçebilirsiniz:",
        reply_markup=keyboard
    )
      
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
      
  elif message.from_user.id == 1853260100:
    await message.reply_text("** sahibimin güzel prensesi🌸❤🩵✨**")
      
  elif message.from_user.id == 6423044130:
    await message.reply_text("** Google perisi💫💕**") 

  else:
    await message.reply_text("__Seni tanımıyorum sen kimsin__ 🙈")

# yeni bir kullancı gruba katıldığında çalışacak 
@app.on_message(filters.new_chat_members) # yeni bir kullanıcı gruba katıldığında bu fonksiyon tetiklenecek
def welcome(client, message): # hoş geldin mesajı fonksiyonu tanımlıyoruz
    for member in message.new_chat_members:  # yeni katılan her kullanıcı için döngü başlatıyoruz
        if member.id == OWNER_ID:  # eğer katılan bot sahibiyse 
            message.reply(f"hoş geldiniz, {member.mention}! Botun sahibinin gruba katılması büyük bir onur.") # özel bir hoş geldin mesajı gönderiyoruz
        else:  # eğer katılan kullanıcı bot sahibi değilse 
            message.reply(f"hoş geldiniz, {member.mention}! Grubumuza katıldığınız için mutluyuz."). # genel hoş geldin mesajı gönderiyoruz

# bir kullanıcı gruptan ayrıldığında çalışacak fonksiyon 
@app.on_message(filters.left_chat_member)
def goodbye(client, message):
    member = message.left_chat_member
    if member.id == OWNER_ID:
        message.reply(f"maalesef, {member.mention} gruptan ayrıldı. umarım tekrar gelirsin.! ")
    else:
        message.reply(f"hoşça kal, {member.mention} seni özleyeceğiz. ")
            
app.run()
