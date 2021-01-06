# For UniBorg
# By Priyam Kalra
# Syntax (.hl <link>)

from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern="hl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input = event.pattern_match.group(1)
    await event.edit("[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")
