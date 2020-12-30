import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, CUSTOM_PMPERMIT
from userbot.thunderconfig import Config

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Userbot"
from userbot.utils import lightning_cmd

LIGHTNING_WRN = {}
LIGHTNING_REVL_MSG = {}

LIGHTNING_PROTECTION = Config.LIGHTNING_PRO



CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
if CUSTOM_PMPERMIT is None:
    CUSTOM_LIGHTNING_PM_PIC = "https://telegra.ph/file/53aed76a90e38779161b1.jpg"
else:
    CUSTOM_LIGHTNING_PM_PIC = CUSTOM_PMPERMIT
FUCK_OFF_WARN = "You Have Attempted To Spam Masters Inbox So Inorder To Avoid Over Spam , You Have Been Blocked By Userbot"

lol = Var.TG_BOT_USER_NAME_BF_HER

OVER_POWER_WARN = (
    f"**Hello Sir Im Here To Protect {DEFAULTUSER} Dont Under Estimate Me 😂😂  **\n\n"
    f"`My Master {DEFAULTUSER} is Busy Right Now !` \n"
    f"{DEFAULTUSER} Is Very Busy Why Came Please Lemme Know Choose Your Deasired Reason"
    f"**Btw Dont Spam Or Get Banned** 😂😂 \n\n"
    f"**{CUSTOM_LIGHTNING_PM_PIC}**"
)
if Var.PRIVATE_GROUP_ID is not None:

    @borg.on(lightning_cmd(pattern="(a|approve)"))
    async def block(event):
        if event.fwd_from:
            return
        replied_user = await borg(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chats = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chats.id):
                if chats.id in LIGHTNING_WRN:
                    del LIGHTNING_WRN[chats.id]
                if chats.id in LIGHTNING_REVL_MSG:
                    await LIGHTNING_REVL_MSG[chats.id].delete()
                    del LIGHTNING_REVL_MSG[chats.id]
                pmpermit_sql.approve(chats.id, "Wow lucky You {DEFAULTUSER} Approved You")
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(firstname, chats.id)
                )
                await asyncio.sleep(3)
                await event.delete()

    @borg.on(lightning_cmd(pattern="block$"))
    async def lightning_approved_pm(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
            await event.edit("Blocked [{}](tg://user?id={})".format(firstname, chat.id))
            await event.client(functions.contacts.BlockRequest(chat.id))

    @borg.on(lightning_cmd(pattern="(da|disapprove)"))
    async def lightning_approved_pm(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        chat = await event.get_chat()
        if event.is_private:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    "Disapproved User [{}](tg://user?id={})".format(firstname, chat.id)
                )
                await event.delete()

    @bot.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if not chat.id in LIGHTNING_WRN:
                    pmpermit_sql.approve(chat.id, "outgoing")
                    bruh = "Auto-approved bcuz outgoing 😄😄"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()  

    @borg.on(lightning_cmd(pattern="listapproved$"))
    async def lightning_approved_pm(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot.on(events.NewMessage(incoming=True))
    async def lightning_new_msg(event):
        if event.sender_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not event.is_private:
            return

        lightning_chats = event.message.message
        chat_ids = event.sender_id

        lightning_chats.lower()
        if OVER_POWER_WARN == lightning_chats:
            # lightning should not reply to other lightning
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(event.sender_id)
        if chat_ids == bot.uid:
            # don't log Saved Messages
            return
        if sender.bot:
            # don't log bots
            return
        if sender.verified:
            # don't log verified accounts
            return
        if LIGHTNING_PROTECTION == "NO":
            return
        if pmpermit_sql.is_approved(chat_ids):
            return
        if not pmpermit_sql.is_approved(chat_ids):
            # pm permit
            await lightning_goin_to_attack(chat_ids, event)

    async def lightning_goin_to_attack(chat_ids, event):
        if chat_ids not in LIGHTNING_WRN:
            LIGHTNING_WRN.update({chat_ids: 0})
        if LIGHTNING_WRN[chat_ids] == 5:
            r = await event.reply(FUCK_OFF_WARN)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_ids))
            if chat_ids in LIGHTNING_REVL_MSG:
                await LIGHTNING_REVL_MSG[chat_ids].delete()
            LIGHTNING_REVL_MSG[chat_ids] = r
            lightn_msg = ""
            lightn_msg += "#BLOCKED_PMs\n\n"
            lightn_msg += f"[User](tg://user?id={chat_ids}): {chat_ids}\n"
            lightn_msg += f"Message Counts: {LIGHTNING_WRN[chat_ids]}\n"
            # lightn_msg += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=lightn_msg,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except BaseException:
                return
        lightningusername = Var.TG_BOT_USER_NAME_BF_HER
        tap = await bot.inline_query(lightningusername, OVER_POWER_WARN)
        sed = await tap[0].click(event.chat_id)
        LIGHTNING_WRN[chat_ids] += 1
        if chat_ids in LIGHTNING_REVL_MSG:
            await LIGHTNING_REVL_MSG[chat_ids].delete()
        LIGHTNING_REVL_MSG[chat_ids] = sed



@bot.on(events.NewMessage(incoming=True, from_users=(1232461895)))
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, "**Heya @hacker11000.You Are My Co Dev Pls Come In**"
            )


@bot.on(
    events.NewMessage(incoming=True, from_users=(1311769691))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @krish1303y. How Can I Disapprove You Come In Sir**😄😄"
            )
@bot.on(
    events.NewMessage(incoming=True, from_users=(1105887181))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @THE_B_LACK_HAT. How Can I Disapprove You Come In Sir**😄😄"
            )            
@bot.on(
    events.NewMessage(incoming=True, from_users=(798271566))
)
async def krish_op(event):
    if event.fwd_from:
        return
    chats = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chats.id):
            pmpermit_sql.approve(chats.id, "**Heya Sir**")
            await borg.send_message(
                chats, f"**Good To See You @Hackintush. How Can I Disapprove You Come In Sir**😄😄"
            )               
