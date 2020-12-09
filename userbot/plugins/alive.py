"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
# For @TeleBotHelp
"""Check if your userbot is working."""
import time

from userbot import ALIVE_NAME, CMD_HELP, Lastupdate
from userbot.Config import Var
from userbot.plugins import currentversion
from userbot.thunderconfig import Config
from userbot.utils import admin_cmd, sudo_cmd

# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Hey! I'm alive. All systems online and functioning normally!"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else None
telemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**✵**"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


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


# Functions
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


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = Var.ALIVE_IMAGE
pm_caption = "➥ **𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤 IS:** `ONLINE`\n\n"
pm_caption += "➥ **ѕуѕтєм ѕтαтѕ**\n"
pm_caption += "➥ **тєℓєтнση νєяѕιση:** `1.15.0` \n"
pm_caption += "➥ **ρутнση:** `3.7.4` \n"
pm_caption += f"➥ **υρтιмє** : `{uptime}` \n"
pm_caption += "➥ **∂αтαвαѕє ѕтαтυѕ:**  `Functional`\n"
pm_caption += "➥ **ℭ𝔲𝔯𝔯𝔢𝔫𝔱 𝔅𝔯𝔞𝔫𝔠𝔥** : `master`\n"
pm_caption += f"➥ **ᴠᴇʀꜱɪᴏɴ** : `{currentversion}`\n"
pm_caption += f"➥ **Mყ Bσʂʂ** : {DEFAULTUSER} \n"
pm_caption += "➥ **ℌ𝔢𝔯𝔬𝔨𝔲 𝔇𝔞𝔱𝔞𝔟𝔞𝔰𝔢** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **Lιƈҽɳʂҽ** : [GNU General Public License v3.0](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [Krish1303y](https://t.me/krish1303y)\n"
pm_caption += "➥ **Check Stats By Doing** `.stat`. \n\n"
pm_caption += "[🇮🇳 Deploy 𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤 🇮🇳](https://telegra.ph/FRIDAY-06-15)"
pm_caption += "See Whoever Is Seen This Dont Spam Or Dm My master"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if UserBot is Alive"
    }
)
