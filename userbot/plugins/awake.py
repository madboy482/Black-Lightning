"""Check if userbot awake or not . 

"""
from userbot import ALIVE_NAME
from userbot.Config import Var
from userbot.utils import lightning_cmd
import os
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)
if ALIVE_PHOTTO is None:
    ALIVE_ME = "https://telegra.ph/file/b01cd4ef19edc14195648.mp4"
else:
    ALIVE_ME = ALIVE_PHOTTO


DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)

ALIVE_MESSAGE = Var.ALIVE_MSG
if ALIVE_MESSAGE is None:
    ALIVE_MESSAGE = "**🔱Black Lightning IS Awake🔱 \n\n\n**"
    ALIVE_MESSAGE += "`My Bot Status \n\n\n`"
    ALIVE_MESSAGE += f"`Telethon: TELETHON-15.0.0 \n\n`"
    ALIVE_MESSAGE += f"`Python: PYTHON-3.8.5 \n\n`"
    ALIVE_MESSAGE += "`I'll Be With You Master Till My Dyno Ends!!☠ \n\n`"
    ALIVE_MESSAGE += f"`Support Channel` : @blacklightningot \n\n"
    ALIVE_MESSAGE += f"`MY BOSS🤗`: {DEFAULTUSER} \n\n "


# @command(outgoing=True, pattern="^.awake$")
@borg.on(lightning_cmd(pattern=r"awake"))
async def amireallyalive(awake):
    """ For .awake command, check if the bot is running.  """
    await awake.delete()
    await borg.send_file(awake.chat_id, ALIVE_ME, caption=ALIVE_MESSAGE)
