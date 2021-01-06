# Rewritten by @krish1303y
import io
from  userbot import CMD_LIST, ALIVE_NAME, bot as light
from userbot.utils import lightning_cmd
import asyncio
from var import Var

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Pls Go To Heroku Vars Then in  `ALIVE_NAME`place You Telegram `Username` "

@light.on(lightning_cmd(pattern="help ?(.*)"))
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
                # Some Help From Telebot
                with io.BytesIO(str.encode(string)) as out_file:
                    out_file.name = "Some_cmds.txt"  # Some Help Here From Telebot
                await light.send_message(lightning.chat_id, out_file, force_document=True, allow_cache=False, caption="**Some Help :)**", reply_to=reply_to_id,)
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
        lightning_help_strin = f"""Black"""
        lightningusername = Var.TG_BOT_USER_NAME_BF_HER
        try:
            results = await light.inline_query(  # pylint:disable=E0602
                lightningusername, lightning_help_strin
            )
            await results[0].click(
                lightning.chat_id, reply_to=lightning.reply_to_msg_id, hide_via=True
            )
            await lightning.delete()                                   
        except BaseException:
            await lightning.edit("`hmm`")
            await asyncio.sleep(2)
            await lightning.edit(
                f"Seems That Your {lightningusername} Is Wrong Check once"
                )
            
