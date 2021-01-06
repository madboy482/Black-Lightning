"""
ThankYou @pureindialover
added speciality for sudos if u kang give me credits
"""
import asyncio

from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd, edit_or_reply, sudo_cmd


# @command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
@borg.on(lightning_cmd(pattern=r"gmute ?(\d+)?", outgoing=True))
@borg.on(sudo_cmd(pattern=r"gmute ?(\d+)?", allow_sudo=True))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    user_id = reply.from_id
    if user_id == (await borg.get_me()).id:
        await event.reply(r"LoL. Why would I Gmute u. You are my owner")
        return
    if user_id in Config.BEST_USERS:
        await event.reply(
            "*Abbe gandu tu jisse mute krr rha h.... vo tera baap h baap ko mute ni krte.**\nPerhaps I can't gmute him.\n\n"
            "**Tip:** He iz my Tera Baaap."
        )
        return
    if user_id in Config.WHITELIST_USERS:
        await event.reply(
            "**He has more immunity.**\nPerhaps I can't gmute him.\n\n"
            "**Tip:** He iz a Developer Of Black Lightning."
        )
        return
    if user_id in Config.SUPPORT_USERS:
        await event.reply(
            "**Lol, Dont be fool He has more connections and He Is My Developer Friend.**\nPerhaps I can't gmute him.\n\n"
            "**Tip:** He iz a My Developer Friend."
        )
        return
    if user_id in Config.DEVLOPERS:
        await event.reply(
            "**Abbe gandu tu jisse mute krr rha h.... vo tera baap h baap ko mute ni krte.**\nPerhaps I can't gmute him.\n\n"
            "**Tip:** He iz The Developer Of Black Lightning ."
        )
        return
    elif event.is_private:
        await edit_or_reply(event, "Putting Duct Tape on that person's mouth!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please reply to a user or add their into the command to gmute them."
        )
    event.chat_id
    await event.get_chat()
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event, "Duct Tape is already availabe on this user's mouth"
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(
            event, "Successfully putted Duct Tape on that person's mouth"
        )


# @command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
@borg.on(lightning_cmd(pattern=r"ungmute ?(\d+)?", outgoing=True))
@borg.on(sudo_cmd(pattern=r"ungmute ?(\d+)?", allow_sudo=True))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await edit_or_reply(event, "Removed Duct Tape from that person's mouth!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event,
            "Please reply to a user or add their into the command to ungmute them.",
        )
    event.chat_id
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, "Duct Tape is not on this user's mouth")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(
            event, "Successfully Removed Duct Tape from that person's mouth"
        )


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
