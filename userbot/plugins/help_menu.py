# Rewritten by @krish1303y

from  userbot import CMD_LIST, ALIVE_NAME
from userbot.utils import admin_cmd
from telethon import  functions
import asyncio


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Pls Go To Heroku Vars Then in  `ALIVE_NAME`place You Telegram `Username` "

@borg.on(admin_cmd(pattern="help ?(.*)"))
async def lightning_cmd_list(lightning):
    if not lightning.text[0].isalpha() and lightning.text[0] not in ("/", "#", "@", "!"):
        lightningusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = lightning.pattern_match.group(1)
        if lightningusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "ℹ️ " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                await bot.send_message(lightning.chat_id, lig_hmm=True, light_c=False, lightn_cap="**Some Help :)**", reply_to=reply_to_id,)
                await lightning.delete()
            else:
                await lightning.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:\n".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await lightning.edit(string)
            else:
                await lightning.edit("`Wait Checking..`")
                await asyncio.sleep(2)
                await lightning.edit(input_str + "  ☹️ is not a valid plugin😞😞!")
               
    else:
        lightning_help_strin = f"""Black Lightning Heres With The Detailed Help For This CMD 😉😉 !\n
{DEFAULTUSER}Sir Like If Faced Any Bug Please Give The Feed Back at @lightningsupport"""
        try:
            lightningusername = Var.TG_BOT_USER_NAME_BF_HER
            results = await bot.inline_query(  # pylint:disable=E0602
                lightningusername,
                lightning_help_strin
            )
            # Some Help Here From Telebot
            
            await results[0].click(
                lightning.chat_id, reply_to=lightning.reply_to_msg_id, hide_via=True
            )
            await lightning.delete()

           
           
@borg.on(admin_cmd(pattern="lightningconfig"))  # pylint:disable=E0602
async def config(lightning):
    if lightning.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await lightning.edit("Telethon UserBot powered by Black Lightning")
