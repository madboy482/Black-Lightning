# Thanks to Sipak bro and Aryan..
# animation Idea by @(Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import os
from io import BytesIO
import time

import requests
from PIL import Image

from userbot import ALIVE_NAME, CMD_HELP, topfunc, StartTime
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply, sudo_cmd


PM_IMG = Config.ALIVE_PIC
version = "4.5"
python_version = "3.8.5"
catversion = "3.0"
ALIVE_MSG = Config.ALIVE_MSG or "✮ MY BOT IS RUNNING SUCCESFULLY ✮"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  ✥ "

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤"
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
file1 = "https://telegra.ph/file/7f72b0ea1893e84028298.mp4"
file2 = "https://telegra.ph/file/7f72b0ea1893e84028298.mp4"
file3 = "https://telegra.ph/file/7f72b0ea1893e84028298.mp4"
file4 = "https://telegra.ph/file/7f72b0ea1893e84028298.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "** 𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n\n"
pm_caption += (
    "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
)
pm_caption += "**I Will Be With You Until My Dynos Dead"
pm_caption += "✘ About My System ✘\n\n"
pm_caption += "➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ 1.17.5\n"
pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/blacklightningot)\n"
pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤](https://github.com/KeinShin)\n"
pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤](https://github.com/KeinShin/Black-Lightning)\n\n"
pm_caption += (
    "➾ **Hey Whoever Is Seein This Alive Dont Dm  And Dont Spam In My  Master DM"
)
pm_caption += "➾ **Spammer Go Away Im His Assitant"
pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def amireallyalive(yes):
    await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

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

    await alive.delete()

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


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


@borg.on(admin_cmd(outgoing=True, pattern="salive"))
@borg.on(sudo_cmd(pattern=r"salive", allow_sudo=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "**𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴**\n"
        pm_caption += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
        pm_caption += "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
        pm_caption += "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
        pm_caption += (
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/blacklightningot)\n"
        )
        pm_caption += (
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/blacklightningot)\n"
        )
        pm_caption += "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/hellboi-atul)\n"
        pm_caption += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ 𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤 ](https://t.me/blacklightningot)\n"
        pm_caption += "[┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/blacklightningot)"
        await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(
            alive.chat_id, ALIVE_PHOTTO, caption=pm_caption, link_preview=False
        )
        await allive.delete()
        return
    req = requests.get("https://telegra.ph/file/7f72b0ea1893e84028298.mp4")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(
            alive.chat_id,
            "**𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴**\n"
            f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
            "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
            "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/blacklightningot)\n"
            "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/blacklightningot)\n"
            "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/hellboi-atul)\n"
            "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ 𝔅𝔩𝔞𝔠𝔨 𝔏𝔦𝔤𝔥𝔱𝔫𝔦𝔫𝔤 ](https://t.me/blacklightningot)\n"
            "[ ┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/blacklightningot)",
            link_preview=False,
        )
        await alive.delete()
        
        


# Hellbot's Alive Message 
# Credits to Hellboy Op



        
ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = "https://telegra.ph/file/80e5200c615cf0cb57aa9.mp4"
pm_caption = "__**🔥🔥ɮʟǟƈӄ ʟɨɢɦȶռɨռɢ ɨs օռʟɨռɛ🔥🔥**__\n\n"

pm_caption += (
    f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"
)

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n"

pm_caption += f"😈ɮʟǟƈӄ ʟɨɢɦȶռɨռɢ😈       : __**{hellversion}**__\n"

pm_caption += f"⚜️Sudo⚜️            : `{sudou}`\n"

pm_caption += "⚠️CHANNEL⚠️   : [ᴊᴏɪɴ](https://t.me/lightningsupport)\n"

pm_caption += "🔥CREATOR🔥    : [Nub Here](https://t.me/krish1303y)\n\n"

pm_caption += "    [✨REPO✨](https://github.com/KeinShin/Black-Lightningt) 🔹 [📜License📜](https://github.com/KeinShin/Black-Lightning/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="halive$"))
@bot.on(sudo_cmd(pattern="halive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .halive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


# catuserbot's Alive
# Credits To catbot And Sandi


@bot.on(admin_cmd(outgoing=True, pattern="calive$"))
@bot.on(sudo_cmd(pattern="calive$", allow_sudo=True))
async def amireallyalive(calive):
    if calive.fwd_from:
        return
    reply_to_id = await reply_id(calive)
    uptime = await topfunc.get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if PM_IMG:
        pm_caption = f"**{ALIVE_MSG}**\n\n"
        pm_caption += f"**{EMOJI} Database :** `{check_sgnirts}`\n"
        pm_caption += f"**{EMOJI} Telethon version :** `{version}\n`"
        pm_caption += f"**{EMOJI} Lightning Userbot Version :** `{catversion}`\n"
        pm_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
        pm_caption += f"**{EMOJI} Uptime :** `{uptime}\n`"
        pm_caption += f"**{EMOJI} Master:** {DEFAULTUSER}\n"
        await calive.client.send_file(
            calive.chat_id, PM_IMG, caption=pm_caption, reply_to=reply_to_id
        )
        await calive.delete()
    else:
        await edit_or_reply(
            calive,
            f"**{ALIVE_MSG}**\n\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"**{EMOJI} Telethon Version :** `{version}\n`"
            f"**{EMOJI} Lightning Userbot Version :** `{catversion}`\n"
            f"**{EMOJI} Python Version :** `{python_version()}\n`"
            f"**{EMOJI} Uptime :** `{uptime}\n`"
            f"**{EMOJI} Master:** {DEFAULTUSER}\n",
        )    
    
def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output

# Telebot's Alive
# Credits To Telbot And xditya
from userbot.Config import Var
from userbot.thunderconfig  import Config
from datetime import datetime 

CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "Hey! I'm alive. All systems online and functioning normally!"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else None

from userbot import telever

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


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@lightningsupport"


@borg.on(admin_cmd(outgoing=True, pattern="talive"))
@borg.on(sudo_cmd(outgoing=True, pattern="talive", allow_sudo=True))
async def amireallyalive(talive):
    start = datetime.now()
    myid = bot.uid
    """ For .talive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
        tele = f"**Welcome To Black Lightning **\n\n"
        tele += f"`{CUSTOM_ALIVE}`\n\n"
        tele += (
            f"{telemoji} **Telethon version**: `1.17`\n{telemoji} **Python**: `3.8.3`\n"
        )
        tele += f"{telemoji} **Black Lightning Version**: `{telever}`\n"
        tele += f"{telemoji} **More Info**: @lightningsupport\n"
        tele += f"{telemoji} **Sudo** : `{sudo}`\n"
        tele += f"{telemoji} **Lightning Uptime**: `{uptime}`\n"
        tele += f"{telemoji} **Database Status**: `All OK 👌!`\n"
        tele += (
            f"{telemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
        )
        tele += "    [✨ GitHub Repository ✨](https://github.com/KeinShin/Black-Lightning)"
        await talive.get_chat()
        await talive.delete()
        """ For .talive command, check if the bot is running.  """
        await borg.send_file(talive.chat_id, ALV_PIC, caption=tele, link_preview=False)
        await talive.delete()
        return
    req = requests.get("https://telegra.ph/file/07d55d71944a852ac6d5e.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(
            talive.chat_id,
            f"**Welcome To Black Lightning **\n\n"
            f"`{CUSTOM_ALIVE}`\n\n"
            f"{telemoji} **Telethon version**: `1.17`\n{telemoji} **Python**: `3.8.3`\n"
            f"{telemoji} **Black Lightning Version**: `{telever}`\n"
            f"{telemoji} **More Info**: @lightningsupport\n"
            f"{telemoji} **Sudo** : `{sudo}`\n"
            f"{telemoji} **Black Lightning Uptime**: `{uptime}`\n"
            f"{telemoji} **Database Status**: `All OK 👌!`\n"
            f"{telemoji} **My pro owner** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"
            "    [✨ GitHub Repository ✨](https://github.com/KeinShin/Black-Lightning)",
            link_preview=False,
        )
        await borg.send_file(talive.chat_id, file=sticker)
        await talive.delete()






CMD_HELP.update(
    {
        "spam": "**Plugin : **`spam`\
        \n\n**Syntax : **`.halive For Hellbot's Alive`\
        \n**Function : **__ Hellbot's Alive__\
        \n\n**Syntax : **`.talive`\
        \n**Function : **__Telebot's Alive !!__\
        \nFor above two commands use `.bigspam` instead of spam for spamming more than 50 messages\
        \n\n**Syntax : **`.falive`\
        \n**Function : **__ Fridays's Alive.__\
        \n\n**Syntax : **`.malive`\
        \n**Function : **__ Mello's Alive t.__\
        \n\n**Syntax : **`.calive `\
        \n**Function : **__ .CatUSerbot's Alive.__\
        \n\n\n**NOTE : All Credits To Thier Respective !!**"
    }
)    
