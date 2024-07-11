# slapmessages örnekleri 
slapmessages =[
    "{}, {}'in yüzüne tükürdü.😄",
    "{}, {}'i tekmeledi.🙊",
    "{}, {}'yı tekme tokat dövdü.😱",
    "{}, {}'e tokat attı.🤠",
    "{}, {}'i tekmeledi.🤡",
    "{}, {}'in telefonunu suya fırlattı.💀",
    "{}, {}'in üstüne kahve döktü.👾",
]
@app.on_message(filters.command(["sille"]) & filters.group)
async def sille(client, message):
    # komutun bir yanıt olup olmadığını kontrol ediyoruz.
    if not message.reply_to_message:
         await message.reply("bu mesajı kullanmak için bir mesajı yanıtlamalısınız.")
         return
         
    # yanıtlayan kişinin (gönderici) ve yanıtlanan kişinin (bilgilerini alıyoruz)
    sender = message.from_user
    target = message.reply_to_message.from_user

    # eğer yanıtlanan kişi OWNER_ID ise özel bir mesaj gönderiyoruz.
    if target.id == OWNER_ID:
        await message.reply("Beni tokatlayamazsın!")
        return
         
    # yanıtlayan ve yanıtlanan kişilerin mentionlarını alıyoruz
    sender_mention = sender.mention
    target_mention = target.mention

    # rastgele bir slap mesajı seçiyoruz ve isimlerle dolduruyoruz
    slap_message = random.choice(slapmessages).format(sender_mention, target_mention)

    # yanıtlanan mesaja gönderilecek metni oluşturuyoruz
    await message.reply_to_message.reply(slap_message)