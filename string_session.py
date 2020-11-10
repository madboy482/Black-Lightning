from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print ("")
print ("")
print("""processing.......""")

API_KEY = '1628628'
API_HASH = "06aa9b10e8ac2f1060e8e7f4f4093cec"
while True:
  try:
   with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
      print("")
      session = client.session.save()
      client.send_message("me", f"Here is your TELEGRAM STRING SESSION\n(tap to copy)👇 \n\n `{session}`")
      print("You telegram String session successfully stored in your telegram, please check your Telegram Saved Messages ")
      print("Store it safe !! Don't share with anyone.. Regards.. Team BLACK THUNDER")
  except:
   print ("")
   print ("Wrong phone number \n make sure its with correct  country code")
   print ("")
   continue
  break
