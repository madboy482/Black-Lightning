# Thanks to Sipak bro and Aryan..
# animation Idea by @(Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import os
import time
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME, CMD_HELP, StartTime, topfunc
from userbot.Config import Var
from userbot.thunderconfig import Config
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


LIGHTNING_IMAGE = os.environ.get("LIGHTNING_IMAGE", None)
if LIGHTNING_IMAGE is None:
    LIGHTNING_IMG = "https://telegra.ph/file/c828d5c695b4cf95c814e.mp4"
else:
    LIGHTNING_IMG = LIGHTNING_IMAGE




version = "4.5"
python_version = "3.8.5"
catversion = "3.0"
ALIVE_MSG = Config.ALIVE_MSG or "✮ MY BOT IS RUNNING SUCCESFULLY ✮"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  ✥ "
hellversion = "7.0"
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

# Thanks to Sipak bro and Raganork..
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b4f20d392bf8dcc50bdd9.mp4"
file2 = "https://telegra.ph/file/b01cd4ef19edc14195648.mp4"
file3 = "https://telegra.ph/file/c828d5c695b4cf95c814e.mp4"
file4 = "https://telegra.ph/file/c828d5c695b4cf95c814e.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "** вℓα¢к ℓιgнтηιηg 𝙸𝚂 🅾🅽🅻🅸🅽🅴**\n\n"

pm_caption += "➾ `ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ` ☞ 1.17.5\n"
pm_caption += "➾ `ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ` ☞ [ᴊᴏɪɴ](https://t.me/blacklightningot)\n"
pm_caption += "➾ `ʟɪᴄᴇɴꜱᴇ`  ☞ [𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤](https://github.com/KeinShin)\n"
pm_caption += "➾ `ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ` ☞ [𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤](https://github.com/KeinShin/Black-Lightning)\n\n"
pm_caption += f"➾ `ᴍʏ ᴍᴀsᴛᴇʀ` ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"
pm_caption += "➾ `🔥Creator🔥` ☞ [ᴊᴏɪɴ](https://t.me/krish1303y)\n"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def amireallyalive(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await yes.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(yes.chat_id, PM_IMG,caption=pm_caption)
    await yes.delete()
