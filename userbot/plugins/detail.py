from userbot import CMD_HELP, bot
from userbot.utils import friday_on_cmd, sudo_cmd


@bot.on(sudo_cmd(pattern="ahelp ?(.*)", allow_sudo=True))
@bot.on(friday_on_cmd(pattern="ahelp ?(.*)"))
async def _(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(f"Here is some help for the {CMD_HELP[args]}")
        else:
            await event.edit(
                f"Help string for {args} not found! Type `.help` to see valid module names."
            )
    else:
        string = ""
        for i in CMD_HELP.values():
            string += f"`{str(i[0])}`, "
        string = string[:-2]
        await event.edit(
            "Please specify which module you want help for!\n\n" f"{string}"
        )from userbot import CMD_HELP, bot
from userbot.utils import admin_cmd, sudo_cmd
import asyncio

@bot.on(sudo_cmd(pattern="detailed ?(.*)", allow_sudo=True))
@bot.on(admin_cmd(pattern="detailed ?(.*)"))
async def _(event):
    help_plugs = event.pattern_match.group(1).lower()
    if help_plugs:
        if help_plugs in CMD_HELP:
            await event.edit(f"Details For 🗡 {CMD_HELP[help_plugs]}")
        else:
            await event.edit(
                f"Nothign Is Named as {help_plugs} `.help` to see valid plugs"
            )
    else:
        help_string = ""
        for i in CMD_HELP.values():
            help_string += f"`{str(i[0])}`, "
        help_string = help_string[:-2]
        await event.edit(
            "`Are You Commedy Me?`!\n\n" f"{help_string}"
        )
        await asyncio.sleep(2)
        await event.edit("`Specify A Plugin`")
