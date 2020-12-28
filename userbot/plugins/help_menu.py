# Rewritten by @krish1303y

from  userbot import CMD_LIST, ALIVE_NAME
from userbot.utils import admin_cmd, lightning_command 
from telethon import  functions
import asyncio


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Pls Go To Heroku Vars Then in  `ALIVE_NAME`place You Telegram `Username` "

@lightning_command(pattern="^.help ?(.*)")
async def lightning_cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        lightning_userbot_name = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if lightning_userbot_name is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "ℹ️ " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "Do .help cmd")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:\n".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + "  ☹️ is not a valid plugin😞😞!")
        else:
            lightn_string = f"""Black Lightning Heres With The Detailed Help For This CMD 😉😉 !\n
{DEFAULTUSER}Sir Like If Faced Any Bug Please Give The Feed Back at @lightningsupport"""
            results = await bot.inline_query(  # pylint:disable=E0602
                lightning_userbot_name,
                lightn_string
            )
            await results[0].click(
                event.chat_id,
                reply_to=event.reply_to_msg_id,
                hide_via=True
            )
            await event.delete()

@borg.on(admin_cmd(pattern="lightningconfig"))  # pylint:disable=E0602
async def config(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("Telethon UserBot powered by Black Lightning")
