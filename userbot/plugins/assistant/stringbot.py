import asyncio

from telethon.errors.rpcbaseerrors import FloodError
from telethon.tl.types import ClientDHInnerData

from userbot import bot

from asyncio.exceptions import TimeoutError
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import events


from telethon import Button
from var import Var
stringbot = Var.TG_BOT_USER_NAME_BF_HER
TEXT = """Hi, {}.
This is Your Assitant Now As a String Session Generator Bot. I will generate String Session of your Telegram Account.
Now send your `API_ID` same as `APP_ID` to Start Generating Session."""
TEXT = "Now send your `API_HASH`.\n\nPress /cancel to Cancel Task."
PHONE_NUMBER = (
    "Now send your Telegram account's Phone number in Indian Format. \n"
    "Including Country code. Example: **+91 XXXXX XXXXX**\n\n"
    "Press /cancel to Cancel Task."
)

from userbot.utils import assistant_cmd

@tgbot.on(events.NewMessage(pattern="^/string"))
async def genStr(msg):
    chat = msg.chat
    api = await bot.ask(
        chat.id, TEXT.format(msg.from_user.mention)
    )
    try:
        check_api = int(api.text)
    except Exception:
        await msg.reply("`API_ID` is Invalid.\nPress /start to Start again.")
        return
    hash = await bot.ask(chat.id, TEXT)
    session_name = "startup"
    api = await bot.send_message(
        chat.id, TEXT.format(msg.from_user.mention)
    )
    
    api_id = api.text
    hash = await bot.ask(chat.id, TEXT)
    if not len(hash.text) >= 30:
        await msg.reply("`API_HASH` is Invalid.\nPress /start to Start again.")
        return
    api_id = api.text
    api_hash = hash.text
    client = TelegramClient(session_name, api_id, api_hash)
    while True:
        number = await bot.ask(chat.id, PHONE_NUMBER)
        if not number.text:
            continue
        phone = number.text
        confirm = await bot.ask(chat.id, f'`Is "{phone}" correct? (y/n):` \n\nSend: `y` (If Yes)\nSend: `n` (If No)')
        if "y" in confirm.text:
            break
    try:
        client = TelegramClient(session_name, api_id, api_hash)
    except Exception as e:
        await bot.send_message(chat.id ,f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
        return
    try:
        await client.connect()
    except ConnectionError:
        await client.disconnect()
        await client.connect()
    try:
        await client.connect()
    except TimeoutError:
        await bot.send_message("Time limit reached of 5 min.\nPress /string to Start again.")
        return    
    
    try:
        code = await client.send_code(phone)
        await asyncio.sleep(1)
        otp = await bot.ask(
            chat.id, ("An OTP is sent to your phone number, "
                      "Please enter OTP in `1 2 3 4 5` format. __(Space between each numbers!)__ \n\n"
                      "If Bot not sending OTP then try  /string command to Bot.\n"
                      "Press /cancel to Cancel."), timeout=300)
        otp_code = otp.text
        code = await client.send_code(phone)
        await client.sign_in(phone, code.phone_code_hash, phone_code=' '.join(str(otp_code)))
    except TimeoutError:
        await bot.send_message("Time limit reached of 5 min.\nPress /string to Start again.")
        return
    try:
        session_str = client.session.save()
        s_m = client.send_message("me", session_str)    
    except FloodError:
        await bot.send(f"You Have Floodwait Of {FloodError.x} Seconds ")


