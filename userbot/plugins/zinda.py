# By @TeleBotHelp
# This plugin is by @xaditya

"""Check if your userbot is working."""
import os
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME
from userbot.__init__ import StartTime

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Black Lightning"


@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    start = datetime.now()
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALIVE_PIC:
        tele = f"**This Black Lightning Assistant**\n\n"
        tele += "**`Hey! I'm alive. All systems online and functioning normally!`**\n\n"
        tele += "` 🔸 Telethon version:` **1.15.0**\n` 🔹 Python:` **3.8.3**\n"
        tele += "` 🔸 More info:` [Black Lightning](https://github.com/Anmol-dot283/Black-Lightning)\n"
        tele += "` 🔹 Bot created by:` [@krish130y](https://t.me/krish1303y)\n"
        tele += f"` 🔸 DARK COBRA Uptime:` {uptime}\n"
        tele += "` 🔸 Database Status:` **All OK 👌!**\n"
        tele += f"` 🔹 My pro owner`: {DEFAULTUSER}\n\n"
        tele += "    [✨ GitHub Repository ✨](https://github.com/Anmol-dot283/Black-Lightning)"

        await alive.get_chat()
        await alive.delete()
        """ For .alive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALIVE_PIC, caption=tele, link_preview=False)
        await alive.delete()
        return
    req = requests.get("https://telegra.ph/file/b233f8b6332fbeb3f61dc.mp4")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "mp4")
        sticker.name = "sticker.mp4"
        sticker.seek(0)
        await borg.send_message(
            alive.chat_id,
            f"**Welcome To Black Lightning **\n\n"
            "**`Hey! I'm alive. All systems online and functioning normally!`**\n\n"
            "` 🔸 Telethon version:` **1.15.0**\n` 🔹 Python:` **3.8.3**\n"
            "` 🔸 More info:` [Black Lightning](https://github.com/Anmol-dot283/Black-Lightning)\n"
            "` 🔹 Bot created by:` [@krish1303y](https://t.me/krish1303y)\n"
            f"` 🔸 TeleBot Uptime:` {StartTime}\n"
            "` 🔸 Database Status:` **All OK 👌!**\n"
            f"` 🔹 My pro owner`: {DEFAULTUSER}\n\n"
            "    [✨ GitHub Repository ✨](https://github.com/Anmol-dot283/Black-Lightning)",
            link_preview=False,
        )
        await borg.send_file(alive.chat_id, file=sticker)
        await alive.delete()
