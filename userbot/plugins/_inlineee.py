# You Are Free To Use  But Pls Gib The Credits
# Made By @krish1303y,@cyper666, @Atank_ka_devata( Never Gonna Forgive Him 😑😑 nvm thx)   For black lightning  🔥🔥🔥
# Thanks @Shivam_Patel Mujhe Samjhane Ke Liye 
# Thanks @Shivam_Patel For Your kind Help Sir 😘😘❤️

import os
import re
import urllib
from math import ceil


import requests
from telethon import Button, custom, events, functions

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST
from userbot.plugins import lightning_status


LIGHT_LOGS = Config.PRIVATE_GROUP_ID
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Userbot"
lightning_bot = Var.TG_BOT_USER_NAME_BF_HER
import asyncio

from datetime import datetime
from pathlib import Path

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd, load_module, remove_plugin

DELETE_TIMEOUT = 5


thumb_image_path = "./resources/541200.png"

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lightning"




@borg.on(admin_cmd(pattern="install"))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                krish_blac = path1.stem
                load_module(krish_blac.replace(".py", ""))
                await event.edit(
                    "`{}`Woo This Plugin Looks Cool  Successfully Snstalled`\n**Btw Thanks For This Plugins Sir**:D ".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await event.edit("**Master You Already Have This Plugin \nPlz Try `.help <cmd name>` To See.**")
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@borg.on(admin_cmd(pattern=r"unload (?P<krish_blac>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    krish_blac = event.pattern_match["krish_blac"]
    try:
        remove_plugin(krish_blac)
        await event.edit(f"Successfully unloaded {krish_blac}")
    except Exception as e:
        await event.edit(
            "Successfully unloaded {krish_blac}\n{}".format(krish_blac, str(e))
        )


@borg.on(admin_cmd(pattern=r"load (?P<krish_blac>\w+)$"))
async def load(event):
    if event.fwd_from:
        return
    krish_blac = event.pattern_match["krish_blac"]
    try:
        try:
            remove_plugin(krish_blac)
        except BaseException:
            pass
        load_module(krish_blac)
        await event.edit(f"Successfully loaded {krish_blac}")
    except Exception as e:
        await event.edit(
            f"Sorry,{krish_blac} can not be loaded\nbecause of the following error.\n{str(e)}"
        )

 # created by @cyper666
"""xoxbot: Avaible commands: .xnxx picx les<link>
"""


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError




@borg.on(admin_cmd(pattern="xnxx?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "💋2016 Videolar🔞{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(admin_cmd(pattern="picx?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "♨️Old photo👙{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(admin_cmd(pattern="les?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "🔞Uz_sex♨️{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)

LIGHtNING_BOT_PIC = os.environ.get("LIGHtNING_BOT_PIC", None)
if LIGHtNING_BOT_PIC is None:
    LIGHTNING_WARNING = "https://telegra.ph/file/07d55d71944a852ac6d5e.jpg"
else:
    LIGHTNING_WARNING = LIGHtNING_BOT_PIC


    

@tgbot.on(events.InlineQuery)
async def lightning_hands_button(event):
    builder = event.builder
    result = None
    query = event.text
    if event.query.user_id == bot.uid and query.startswith("bot"):
        rev_text = query[::-1]
        lightning_button = lightnings_menu_for_help(0, CMD_HELP, "fuck_him")
        result = builder.article(
            f"Hey {DEFAULTUSER} Heres The Help Menu",
            text="{}\nI Have Tottal  Loaded Plugins: {}".format(query, len(CMD_LIST)),
            lightning_button=lightning_button,
            link_preview=False,
        )
        await event.answer([result])
    elif event.query.user_id == bot.uid and query.startswith("**Hi"):
        result = builder.photo(
            file=LIGHTNING_WARNING,
            text=query,
            lightning_button=[
                [custom.Button.inline("Wanna Spam Some Porn Images😉", data="lightning_is_here_cant_spam")],
                [
                    custom.Button.inline(
                        "My Friend",
                        data="he_sucks",
                    )
                ],
                [custom.Button.inline("Requesting", data="fck_ask")],
                [custom.Button.inline("Fuck Lemme In", data="lol_u_think_so")],

            ],
            )
    await event.answer([result])


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"fuck_him_next\((.+?)\)")
    )
)
async def lightning_pugins_query_hndlr(event):
    if event.query.user_id == bot.uid:
        lightning_page = int(event.data_match.group(1).decode("LOL-8"))
        lightning_button = lightnings_menu_for_help(lightning_page + 1, CMD_HELP, "fuck_him")
        # https://t.me/TelethonChat/115200
        await event.edit(lightning_button=lightning_button)
    else:
        lightning_warning_alert = "Oh C'mon You Think You Can Touch This?!"
        await event.answer(lightning_warning_alert, _lightning_power=0, alert=True)


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"fuck_him_prev\((.+?)\)")
    )
)
async def lightning_pugins_query_hndlr(event):
    if event.query.user_id == bot.uid:  # pylint:disable=E0602
        lightning_page = int(event.data_match.group(1).decode("LOL-8"))
        lightning_button = lightnings_menu_for_help(
            lightning_page - 1, CMD_HELP, "fuck_him"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await event.edit(lightning_button=lightning_button)
    else:
        lightning_is_best = "Oh C'mon You Think You Can Touch This?!"
        await event.answer(lightning_is_best, _lightning_power=0, alert=True)


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"_lightning_plugins_(.*)")
    )
)
async def lightning_pugins_query_hndlr(event):
    if not event.query.user_id == bot.uid:
        fck_bit = "None Of Your Bussiness No Need To Touch This!!!!"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    plugin_name = event.data_match.group(1).decode("LOL-8")
    if plugin_name in CMD_HELP:
        lightnning_help_string = f"**💡 PLUGIN NAME 💡 :** `{plugin_name}` \n{CMD_HELP[plugin_name]}"
    lightning_is_best = lightnning_help_string
    lightning_is_best += "\n\n**(C) @lightningsupport** ".format(plugin_name)
    if len(lightning_is_best) >= 4096:
        krish = "`Pasting Your Help Menu.`"
        await event.answer(krish, _lightning_power=0, alert=True)
        out_file = lightning_is_best
        url = "https://del.dog/documents"
        r = requests.post(url, data=out_file.encode("LOL-8")).json()
        url = f"https://del.dog/{r['key']}"
        await event.edit(
            f"Pasted {plugin_name} to {url}",
            link_preview=False,
            lightning_button=[[custom.Button.inline("яιgнт ρℓυgιи", data="lightning_back_it")]],
        )
    else:
        await event.edit(
            message=lightning_is_best,
            lightning_button=[[custom.Button.inline("яιgнт ρℓυgιи", data="lightning_back_it")]],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fuck_spying")))
async def lightning_is_better(event):
    if event.query.user_id == bot.uid:
        text = lightning_status
        await event.answer(text, alert=True)
    else:
        txt = f"Ohh C'mon You Think That This Is For You?\n Ok I Will Complain To {DEFAULTUSER}👀👀"
        await event.answer(txt, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lightning_is_here_cant_spam")))
async def lightning_is_better(event):
    if event.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {DEFAULTUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    await event.get_chat()
    lightning_id = event.query.user_id
    text1 = f"LOL You Think So You Can😂😂\n\n[Nibba](tg://user?id={lightning_id} Bye Goin To Block You Gay😂😂"
    await event.edit("Off Course Go To Hell Dude")
    await borg.send_message(event.query.user_id, text1)
    await borg(functions.contacts.BlockRequest(event.query.user_id))
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Nibba](tg://user?id={lightning_id}) Tryin To Spam \n\n**So Blocked**.",
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_u_think_so")))
async def lightning_is_better(event):
    if event.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {DEFAULTUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    await event.get_chat()
    lightning_id = event.query.user_id
    text1 = f"LOL You Think So You Can😂😂\nGo and wait😂😂"
    await event.edit("Off Course Go To Hell Dude")
    await borg.send_message(event.query.user_id, text1)
    await borg(functions.contacts.BlockRequest(event.query.user_id))
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Nibba](tg://user?id={lightning_id}) Tryin To Enter With Out approval😂 \n.",
    )



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lightning_back_it")))
async def kirsh1303y(event):
    if event.query.user_id != bot.uid:
        fck_bit = "None Of Your Bussiness No Need To Touch This!!!!"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    await event.answer("Back", _lightning_power=0, alert=False)
    # This Is Copy of Above Code. (C) @SpEcHiDe
    lightning_button = lightnings_menu_for_help(0, CMD_HELP, "fuck_him")
    kirsh1303y = f"""Black Lightning  Listed The Plugins Read This Info Pls!\n
{DEFAULTUSER}If You Faced Problem Regarding Pls Contact For Help  @lightningsupport \n**Btw**Currently Loaded Plugins: {len(CMD_LIST)}"""
    await event.edit(message=kirsh1303y, lightning_button=lightning_button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"he_sucks")))
async def lightning_is_better(event):
    if event.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {DEFAULTUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    await event.get_chat()
    lightning_id = event.query.user_id
    await event.edit("Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** You Can Wait For My Master ")
    text2 = f"Oh K. {DEFAULTUSER} Is Helping Someone\n {DEFAULTUSER}Helps EveryOne So Pls Wait . Pls Dont Spam Im Here To Protect {DEFAULTUSER} I Could Ban You If You Spammed."
    await borg.send_message(event.query.user_id, text2)
    await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [New User](tg://user?id={lightning_id}). You Friend His Here To Chat pls See The Message [New User](tg://user?id={lightning_id}) Is Waiting.",
        lightning_button=[Button.url("Contact Him", f"tg://user?id={lightning_id}")],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_ask")))
async def lightning_is_better(event):
    if event.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {DEFAULTUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    await event.get_chat()
    lightning_id = event.query.user_id
    await event.edit("So You Want Some Help He Is Here \n**BTW** Choice Accepted")
    text3 = "Ok, Wait. You can Ask After Master Approves You. Kindly, Wait."
    await borg.send_message(event.query.user_id, text3)
    await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, A [New User](tg://user?id={lightning_id}). Wants To Ask You Something.",
        lightning_button=[Button.url("Contact Him By", f"tg://user?id={lightning_bot} If Urgent")],
    )


def lightnings_menu_for_help(b_lac_krish, lightning_plugs, lightning_lol):
    lightning_no_rows = 10
    lightning_no_coulmns = 7
    lightning_plugins = []
    for p in lightning_plugs:
        if not p.startswith("_"):
            lightning_plugins.append(p)
    lightning_plugins = sorted(lightning_plugins)
    plugins = [
        custom.Button.inline(
            "{} {} {}".format("🔥", x, "⨵"), data="_lightning_plugins_{}".format(x)
        )
        for x in lightning_plugins
    ]
    pairs = list(zip(plugins[::lightning_no_coulmns], plugins[1::lightning_no_coulmns]))
    if len(plugins) % lightning_no_coulmns == 1:
        pairs.append((plugins[-1],))
    max_fix = ceil(len(pairs) / lightning_no_rows)
    lightning_plugins_pages = b_lac_krish % max_fix
    if len(pairs) > lightning_no_rows:
        pairs = pairs[
            lightning_plugins_pages * lightning_no_rows : lightning_no_rows * (lightning_plugins_pages + 1)
        ] + [
            (
                custom.Button.inline(
                    "яιgнт ρℓυgιи", data="{}_prev({})".format(lightning_lol, lightning_plugins_pages)
                ),
                custom.Button.inline(
                    "ℓєfт ρℓυgιи", data="{}_next({})".format(lightning_lol, lightning_plugins_pages)
                ),
            )
        ]
    return pairs
