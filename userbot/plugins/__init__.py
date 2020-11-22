import html
import time
from datetime import datetime

from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location

from userbot.__init__ import ALIVE_NAME, bot, Uptime
from userbot.__init__ import StartTime
from userbot.thunderconfig import Config, Var
from userbot.utils import admin_cmd, sudo_cmd

# stats
if Config.PRIVATE_GROUP_BOT_API_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Var.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

TELEUSER = str(ALIVE_NAME) if ALIVE_NAME else "Thunder"

tele = f"Thunder Version: {Uptime}\n"
tele += f"Log Group: {log}\n"
tele += f"Assistant Bot: {bots}\n"
tele += f"Lydia: {lyd}\n"
tele += f"Sudo: {sudo}\n"
tele += f"PMSecurity: {pm}\n"
tele += f"\nVisit @blackthundersupport for assistance.\n"
telestats = f"{tele}"

TELE_NAME = bot.me.first_name
OWNER_ID = bot.me.id
