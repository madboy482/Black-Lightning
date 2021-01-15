

import asyncio
import os

from telethon import __version__ 
from userbot import ALIVE_NAME, TG_CHANNEL, TG_GRUP
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd

LIGHTNING_ALV_IMG = os.environ.get("LIGHTNING_ALV_IMG", None)
if LIGHTNING_ALV_IMG is None:
    ALV_LIGHTNING = "https://telegra.ph/file/b01cd4ef19edc14195648.mp4"
else:
    ALV_LIGHTNING = LIGHTNING_ALV_IMG


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

TG = str(TG_GRUP) if TG_GRUP else "Not  Yet😁😁"
TG_CHANN = str(TG_CHANNEL) if TG_CHANNEL else "Not Yet😁😁"


from userbot import CMD_LIST

lightning_cap = "**вℓα¢к ℓιgнтηιηg 𝙸𝚂 `ɘᴎi|ᴎO`**\n\n"
lightning_cap += f"**†rïdεη† ﾚïgh†'š mαš†εr**          : {DEFAULTUSER}\n"
lightning_cap += f"⚔️⚔️ {DEFAULTUSER}'s⚔️⚔️ ɢʀօʊք   : {TG}\n"  
lightning_cap += f"⚔️⚔️{DEFAULTUSER}'s⚔️⚔️ ƈɦǟռռɛʟ : {TG_CHANN}\n\n"
lightning_cap += f"`тєℓєтнσи νєяѕισи`       : {__version__}\n"
lightning_cap += "`ρყƚԋσɳ ʋҽɾʂισɳ`           : 3.9.0\n\n"
lightning_cap += "`ֆʊքքօʀƭ ƈɦǟռռɛʟ`          : [ᴊᴏɪɴ](https://t.me/blacklightningot)\n"
lightning_cap += "`ֆʊքքօʀƭ ɢʀօʊք`            : [ᴊᴏɪɴ](https://t.me/lightningsupport)\n"
lightning_cap += "`𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏`:              [KeinShin](https://t.me//krish1303y)\n"


@borg.on(lightning_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def lightning(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, ALV_LIGHTNING, caption=lightning_cap)
    await alive.delete()
