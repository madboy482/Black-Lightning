# Rewritten by @krish1303y
import io
from  userbot import COOL_CMD, ALIVE_NAME, bot as light
from userbot.utils import lightning_cmd
import asyncio
from var import Var

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Pls Go To Heroku Vars Then in  `ALIVE_NAME`place You Telegram `Username` "
    
            



@light.on(lightning_cmd(pattern="help ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        lightningusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if lightningusername is None or input_str == "text":
            string = ""
            for i in COOL_CMD:
                string += "ℹ️ " + i + "\n"
                for iter_list in COOL_CMD[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "`Lol Try .help`")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in COOL_CMD:
                string = "Commands found in {}:\n".format(input_str)
                for i in COOL_CMD[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit("`Wait Checking..`")
                await asyncio.sleep(2)
                await event.edit(input_str + "  ☹️ is not a valid plugin😞😞!")
        else:
            light_help_strin = """**Black Lightning Heres With The Detailed Help For CMDs** 😉😉 !\n If Faced Any Bug Please Give The Feed Back at @lightningsupport:"""
        try:
            results = await bot.inline_query(  # pylint:disable=E0602
            lightningusername, light_help_strin
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except BaseException: # Help Taken From Telebot
            await event.edit(f"It Will   Wont Work {lightningusername} Is Wrong or Inline Is Turned Off")
            await asyncio.sleep(2)
            await event.edit(f"[It Will   Wont Work {lightningusername} Is Wrong Or Inline Is Turned Off](https://telegra.ph/file/ed8a9e7ee3e52cf5f2598.mp4)")





@light.on(lightning_cmd(pattern="hardhelp ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        lightningusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if lightningusername is None or input_str == "text":
            string = ""
            for i in COOL_CMD:
                string += "ℹ️ " + i + "\n"
                for iter_list in COOL_CMD[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await borg.send_message(event.chat_id, "`Lol Try .hardhelp`")
                await asyncio.sleep(5)
            else:
                await event.edit(string)
        elif input_str:
            if input_str in COOL_CMD:
                string = "Some Articles{}:\n".format(input_str)
                for i in COOL_CMD[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
        else:
            light_help_strin = """**Cool Lightning For The Detailed Help**"""
        try:
            results = await bot.inline_query(  # pylint:disable=E0602
            lightningusername, light_help_strin
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except BaseException: # Help Taken From Telebot
            await event.edit(f"It Will   Wont Work {lightningusername} Is Wrong or Inline Is Turned Off")
            await asyncio.sleep(2)
            await event.edit(f"[It Will   Wont Work {lightningusername} Is Wrong Or Inline Is Turned Off](https://telegra.ph/file/ed8a9e7ee3e52cf5f2598.mp4)")
