
# Created By @krish1303y Inspired By Hellbot
# Some Modifcations By @krish1303y

import asyncio
import os

from telethon import __version__ 
from userbot import ALIVE_NAME, TG_CHANNEL, TG_GRUP
from userbot.thunderconfig import Config
from userbot.utils import admin_cmd

LIGHTNING_IMAGE = os.environ.get("LIGHTNING_IMAGE", None)
if LIGHTNING_IMAGE is None:
    LIGHTNING_IMG = "https://telegra.ph/file/5db4087d9de9b738ad0fc.mp4"
else:
    LIGHTNING_IMG = LIGHTNING_IMAGE


version = "4.5"
python_version = "3.8.5"

# Functions
def lightning_Read_time(seconds: int) -> str:
    count = 0
    kirsh = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            lol_hehehe, result = divmod(seconds, 60)
        else:
            lol_hehehe, result = divmod(seconds, 24)
        if seconds == 0 and lol_hehehe == 0:
            break
        time_list.append(int(result))
        seconds = int(lol_hehehe)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        kirsh += time_list.pop() + ", "

    time_list.reverse()
    kirsh += ":".join(time_list)

    return kirsh

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "вℓα¢к ℓιgнтηιηg"

TG = str(TG_GRUP) if TG_GRUP else "No  YT Yet😁😁"
TG = str(TG_CHANNEL) if TG_CHANNEL else "No YT Yet😁😁"
LIGHTNING_ALV_IMG = os.environ.get("LIGHTNING_ALV_IMG", None)

if LIGHTNING_ALV_IMG is None:
    ALV_LIGHTNING = "https://telegra.ph/file/b01cd4ef19edc14195648.mp4"
else:
    ALV_LIGHTNING = LIGHTNING_ALV_IMG

lightning_cap = "**вℓα¢к ℓιgнтηιηg 𝙸𝚂 🅾🅽🅻🅸🅽🅴**\n\n"
lightning_cap += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
lightning_cap += f"{DEFAULTUSER}'s ɢʀօʊք       : {TG}\n"  
lightning_cap += f"{DEFAULTUSER}'s ƈɦǟռռɛʟ                  : {TG_CHANNEL}"
lightning_cap += f"тєℓєтнσи νєяѕισи        : {__version__}\n"
lightning_cap += "ρყƚԋσɳ ʋҽɾʂισɳ           : 3.9.0\n"
lightning_cap += "ֆʊքքօʀƭ ƈɦǟռռɛʟ          : [ᴊᴏɪɴ](https://t.me/blacklightningot)\n"
lightning_cap += "ֆʊքքօʀƭ ɢʀօʊք            : [ᴊᴏɪɴ](https://t.me/lightningsupport)\n\n"
lightning_cap += "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/KeinShin)\n"
lightning_cap += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏:              [KeinShin](https://t.me//krish1303y)\n"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def lightning(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, LIGHTNING_ALV_IMG, caption=lightning_cap)
    await alive.delete()
