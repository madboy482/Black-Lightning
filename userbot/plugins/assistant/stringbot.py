# Thanks To @Errored_Bachha

# Created by @keinshin
# Ported To Assitant By @keinshin

import asyncio
import logging

import random
import re

# Thanks To Uniborg 
# Help Taken From Uniborg

from telethon import events, Button, custom
from telethon import TelegramClient as assitant_client
from telethon.sessions import StringSession as assistant_string
from telethon.errors.rpcerrorlist import  PhoneCodeInvalidError

from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"

TEXT = """Hi, {}.
This is Your Assitant Now As a String Session Generator Bot. I will generate String Session of your Telegram Account.
Now send your `API_ID` same as `APP_ID` to Start Generating Session."""
LOGGING = """Assitant
**ID**: {APP_ID}
**HASH**: {API_HASH}
[Current User ID](tg://user?id={C}): {C}
[Logged In User ID](tg://user?id={L}): {L}"""

NOT_VAILD = "Do /string This Not Vaild"
PHONE_NUMBER = (
    "Now send your Telegram account's Phone number in Indian Format. \n"
    "Including Country code. Example: **+91 XXXXX XXXXX**\n\n"
    "Press /cancel to Cancel Task."
)
NUMBER_ERROR = (
    f"{DEFAULTUSER} Seems This Number Is Already Registered"
)

TWO_STEPS_VERI = (" Semms That You Have Two Steps Verifcation Input Password")

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

from var import Var




@tgbot.on(events.NewMessage(pattern="^/string"))
async def string(event):    
    vent = event.chat_id
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            vent,
            message=f"Press Start For Making String ",
            buttons=[
                [
                    custom.Button.inline(
                        "Start ",
                        data="start",
                    )
                ],
                [Button.url("Api Hash Bot", "@UseTGXBot")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def ass_string():    
    # We have to manually call "start" if we want an explicit bot token
    client = await assitant_client("Assitant", Var.APP_ID[0], Var.API_HASH[0]
    ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
    async with client:
        # Getting information about yourself
        me = await client.get_me()
        # "me" is an User object. You can pretty-print
        # any Telegram object with the "stringify" method:
        logging.info(me.stringify())
        @client.on(events.NewMessage())
        async def handler(event):
            # logging.info(event.stringify())
            APP_ID, API_HASH = Api_Hash_Id(
                Var.APP_ID,
                Var.API_HASH
            )
            async with event.client.conversation(event.chat_id) as conv:
                await conv.send_message(PHONE_NUMBER)
                response = conv.wait_event(events.NewMessage(
                    chats=event.chat_id
                ))
                response = await response
                logging.info(response)
                phone = response.message.message.strip()
                current_client = assitant_client(
                    assistant_string(),
                    api_id=APP_ID, api_hash=API_HASH, device_model= Var.TG_BOT_USER_NAME_BF_HER, system_version= "assitant", assis_stri="9.6.9",
                )
                await current_client.connect()
                sent = await current_client.send_code_request(phone)
                logging.info(sent)
                if sent.phone_registered:
                    await conv.send_message(NUMBER_ERROR)
                    response = conv.wait_event(events.NewMessage(
                        chats=event.chat_id
                    ))
                    response = await response
                    logging.info(response)
                    received_code = response.message.message.strip()
                    received_tfa_code = None
                    received_code = "".join(received_code.split(" "))
                    try:
                        await current_client.sign_in(phone, code=received_code, password=received_tfa_code)
                    except PhoneCodeInvalidError:
                        await conv.send_message(NOT_VAILD)
                        return
                    except Exception as e:
                        logging.info(str(e))
                        await conv.send_message(
                            TWO_STEPS_VERI,

                        )
                        response = conv.wait_event(events.NewMessage(
                            chats=event.chat_id
                        ))
                        response = await response
                        logging.info(response)
                        received_tfa_code = response.message.message.strip()
                        await current_client.sign_in(password=received_tfa_code),
                        assitant_client = await current_client.get_me()
                        logging.info(assitant_client.stringify())
                    session_string = current_client.session.save()
                    await conv.send_message(f"`{session_string}`")
                    assitant_client = await current_client.get_me()
                    #
                    await event.client.send_message(  entity=Var.PM_PERMIT_GROUP_ID, message=LOGGING.format( C=event.chat_id, L=assitant_client.id,
                            APP_ID=APP_ID,
                            API_HASH=API_HASH
                        ),
                        reply_to=4,
                        parse_mode="md",
                        link_preview=False,
                        silent=True
                    )
                else:
                    NOT_REGISTERED_PHONE = "Number Not Vaild /string To Restart"
                    await conv.send_message(NOT_REGISTERED_PHONE)
                    return
        await client.run_until_disconnected()


if __name__ == '__main__':
    # Then we need a loop to work with
    loop = asyncio.get_event_loop()
    # Then, we need to run the loop with a task
    loop.run_until_complete(ass_string())



def Api_Hash_Id(APP_IDS, API_HASHS):
    total_ids = len(APP_IDS)
    random_index = random.randint(0, len(total_ids) - 1)
    return APP_IDS[random_index], API_HASHS[random_index]
