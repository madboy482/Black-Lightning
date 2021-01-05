#    Copyright (C) 2020 KeinShin

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.



"""Thanks To 
@Midhun_xD
@krish1303y

@Shivam_Patel
"""


"""Only friday  Can Use This Inline WithOut Copyright (Just Give The Credits Pls)
Thanks"""




import os

import re
import json
from math import ceil
from userbot.thunderconfig import Config
from telethon.events import InlineQuery, callbackquery
from telethon import Button, custom, events, functions

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST, bot

from var import Var


LIGHT_LOGS = Config.PM_LOGGR_BOT_API_ID 
lightning_bot = Var.TG_BOT_USER_NAME_BF_HER
import asyncio

from datetime import datetime
from pathlib import Path


from userbot.utils import admin_cmd, load_module, remove_plugin

DELETE_TIMEOUT = 5


thumb_image_path = "./resources/541200.png"

LIGHTNINGUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lightning"
LIGHTNINGBOT = Var.TG_BOT_TOKEN_BF_HER



@borg.on(admin_cmd(pattern="install"))
async def install(lightning):
    if lightning.fwd_from:
        return
    if lightning.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await lightning.client.download_media(  # pylint:disable=E0602
                    await lightning.get_reply_message(),
                    "userbot/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                krish_blac = path1.stem
                load_module(krish_blac.replace(".py", ""))
                await lightning.edit(f"Wait Installing.... ")
                await asyncio.sleep(2)
                await lightning.edit(
                    "{}SucessFully Installed ....".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await lightning.edit("**Master You Already Have This Plugin \nPlz Try `.help <cmd name>` To See.**")
        except Exception as e:  # pylint:disable=C0103,W0703
            await lightning.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await lightning.delete()


@borg.on(admin_cmd(pattern=r"unload (?P<krish_blac>\w+)$"))
async def unload(lightning):
    if lightning.fwd_from:
        return
    krish_blac = lightning.pattern_match["krish_blac"]
    try:
        remove_plugin(krish_blac)
        await lightning.edit(f"Successfully unloaded {krish_blac}")
    except Exception as e:
        await lightning.edit(
            "Successfully unloaded {krish_blac}\n{}".format(krish_blac, str(e))
        )


@borg.on(admin_cmd(pattern=r"load (?P<krish_blac>\w+)$"))
async def load(lightning):
    if lightning.fwd_from:
        return
    krish_blac = lightning.pattern_match["krish_blac"]
    try:
        try:
            remove_plugin(krish_blac)
        except BaseException:
            pass
        load_module(krish_blac)
        await lightning.edit(f"Successfully loaded {krish_blac}")
    except Exception as e:
        await lightning.edit(
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


BOT_MSG = os.environ.get("BOT_MSG", None)
if BOT_MSG is None:
    BOT_LIT = f"Hello Sir MySelf Black Lightning Here For  {LIGHTNINGUSER}'s Protection "
else:
    BOT_LIT = BOT_MSG   


LIGHTNING_WARN = os.environ.get("LIGHTNING_WARN", None)
if LIGHTNING_WARN is None:
    WARNING = (
    f"**{BOT_LIT}"
    f"** Im Here To Protect {LIGHTNINGUSER} Dont Under Estimate Me 😂😂  **\n\n"
    f"**My Master {LIGHTNINGUSER} is Busy Right Now !** \n"
    f"{LIGHTNINGUSER} Is Very Busy Why Came Please Lemme Know Choose Your Deasired Reason"
    f"**Btw Dont Spam Or Get Banned** 😂 \n\n"
    f"**Choose Any Reason Then Get Lost**\n"
)
else:
    WARNING = LIGHTNING_WARN

LIGHTNING_BOT_PIC = os.environ.get("LIGHTNING_BOT_PIC", None)
if LIGHTNING_BOT_PIC is None:
    LIGHTNING_WARNING = "https://telegra.ph/file/07d55d71944a852ac6d5e.jpg"
else:
    LIGHTNING_WARNING = LIGHTNING_BOT_PIC



def lightnings_menu_for_help(b_lac_krish, lightning_plugs, lightning_lol):
    lightning_no_rows = 8
    lightning_no_coulmns = 7
    lightning_plugins = []
    for p in lightning_plugs:
        if not p.startswith("_"):
            lightning_plugins.append(p)
    lightning_plugins = sorted(lightning_plugins)
    plugins = [
        custom.Button.inline(
            "{} {} {}".format("⨵", x, "⨵"), data="_lightning_plugins_{}".format(x)
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
                    "🗡яιgнт ρℓυgιи", data="{}_prev({})".format(lightning_lol, lightning_plugins_pages)
                ),
               # Thanks To Friday For This Idea
               custom.Button.inline("Stats", data="stta"
               ),
               custom.Button.inline(
                    "ℓєfт ρℓυgιи🗡", data="{}_next({})".format(lightning_lol, lightning_plugins_pages)
                ),
                
            )
        ]
    return pairs


@tgbot.on(events.InlineQuery)
async def lightning_hands_button(lightning):
    builder = lightning.builder
    result = None
    query = lightning.text
    if lightning.query.user_id == bot.uid and query.startswith("fuk"):
        rev_text = query[::-1]
        buttons = lightnings_menu_for_help(0, CMD_HELP, "fukhim")
        result = builder.article(
            f"Hey {LIGHTNINGUSER} Heres The Help Menu",
            text="{}\nI Have Tottal  Loaded Plugins: {}".format(query, len(CMD_LIST)),
            buttons=buttons,
            link_preview=False,
        )
        await lightning.answer([result])

    elif lightning.query.user_id == bot.uid and query == "Help":
        result = builder.article(
            title="Help",
            text=f"**How If Face Problem \n{LIGHTNINGUSER}** \nChoose Your Problem For Help ",
            buttons=[
                [custom.Button.inline("Help", data="what?")],
                [Button.url("Commands Not Working🥺", "https://t.me/lightningsupport")],
                [Button.url("Help Article 🤓", "https://app.gitbook.com/@poxsisofficial/s/help/")],
                [
                    Button.url(
                
                    "Want To Learn CMDS😅",
                    "https://t.me/lightningsupport" ,
                    )
                ], 
            ],
        )
    elif lightning.query.user_id == bot.uid and query.startswith("**Hello Sir"):
        result = builder.photo(
            file=LIGHTNING_WARNING,
            text=WARNING,
            buttons=[
                [custom.Button.inline("Wanna Spam Some Porn Images?😉", data="lightning_is_here_cant_spam")],
                [
                    custom.Button.inline(
                        "My Friend❤️❤️",
                        data="he_sucks",
                    )
                ],
                [custom.Button.inline("Requesting🙏", data="fck_ask")],
                [
                    custom.Button.inline(
                        "Fuck Lemme In🖕", 
                        data="lol_u_think_so",
                        
                    )
                        
                ],

            ],
            )
    await lightning.answer([result])


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"fukhim_next\((.+?)\)")
    )
)



async def lightning_pugins_query_hndlr(lightning):
    if lightning.query.user_id == bot.uid:  # pylint:disable=E0602
        lightning_page = int(lightning.data_match.group(1).decode("UTF-8"))
        buttons = lightnings_menu_for_help(
            lightning_page + 1, CMD_HELP, "fukhim"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await lightning.edit(buttons=buttons)
    else:
        lightning_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"
        await lightning.answer(lightning_is_best, cache_time=0, alert=True)

@tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"_lightning_plugins_(.*)")
   )
)




@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"fukhim_prev\((.+?)\)")
    )
)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"what?")))
async def what(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"{LIGHTNINGUSER} Dont Use This Pls 🥺 "
        await lightning.answer(fck_bit, alert=True)
    else:
        txt = f"Ohh C'mon You Think That This Is For You?\n Ok I Will Complain To {LIGHTNINGUSER}👀👀"
        await lightning.answer(txt, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lightning_is_here_cant_spam")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    text1 = f"LOL **You Think So You Can**😂😂\n\n**[Nibba](tg://user?id={lightning_id}) Bye Goin To Block You Gay**😂😂"
    await lightning.edit("Off Course Go To Hell Dude")
    await bot.send_message(lightning.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))
    await lightning.edit("🖕")
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={lightning_id}) Tryin To Spam 😂\n\n**So Blocked**.",
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_u_think_so")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    text1 = f"LOL You Think So You Can😂😂\nGo and wait😂😂"
    await lightning.edit("Off Course Go To Hell Dude🖕")
    await bot.send_message(lightning.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={lightning_id}) Tryin To Enter With Out approval😂 \n.",
    )



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lightning_back_it")))
async def krish1303y(lightning):
    if lightning.query.user_id != bot.uid:
        fck_bit = "What You Think That This Back Button You Can Touch Bitch🖕!!!!"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.answer("Back", cache_time=0, alert=False)
    # This Is Copy of Above Code. (C) @SpEcHiDe
    buttons = lightnings_menu_for_help(0, CMD_HELP, "fukhim")
    krish1303y = f"""Black Lightning  Listed The Plugins Read This Info Pls!\n
{LIGHTNINGUSER}If You Faced Problem Regarding Pls Contact For Help  @lightningsupport \n**Btw**Currently Loaded Plugins: {len(CMD_LIST)}"""
    await lightning.edit(message=krish1303y, buttons=buttons)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"he_sucks")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    await lightning.edit("Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** **You Can Wait For My Master**")
    await asyncio.sleep(2)
    await lightning.edit(
        "Name Which Type Of Friend?", buttons= [
        [Button.inline("School", data="school")],
        [Button.inline("Tg Causal Friend", data="tg_okay")],
        ], 
    )
    light_text = "`Warning`- ❗️⚠️Dont Try Anything Stupid  Wait Kindly!!!❗️⚠️"
    await bot.send_message(lightning.query.user_id, light_text)
    await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Friend](tg://user?id={lightning_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={lightning_id}) Is Waiting.",
        buttons=[Button.url("Contact Him", f"tg://user?id={lightning_id}")],
    )
    
    
    
    
    
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))
async def yeahbaba(lightning):
        if lightning.query.user_id == bot.uid:
            lightning_id = lightning.query.user_id
            await asyncio.sleep(2)
            light_text = "**So You  Are TG Friend**Okay wait"
            await asyncio.sleep(2)
            await lightning.edit(f"`Informing To Master {LIGHTNINGUSER}`")
            await asyncio.sleep(2)
            await lightning.edit("`Done Informed`")
            await bot.send_message(lightning.query.user_id, light_text)
            await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Friend](tg://user?id={lightning_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={lightning_id}) Is Waiting.",
    
    )
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"School")))
async def yeahbaba(lightning):
        if lightning.query.user_id == bot.uid:
            lightning_id = lightning.query.user_id
            await asyncio.sleep(2)
            light_text = "**So You  Are School Friend**Okay wait"
            await asyncio.sleep(2)
            await lightning.edit(f"`Informing To Master {LIGHTNINGUSER}`")
            await asyncio.sleep(2)
            await lightning.edit("`Done Informed`")
            await bot.send_message(lightning.query.user_id, light_text)
            await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Friend](tg://user?id={lightning_id}). Your Casual Telegram Friend His Here To Chat pls See The Message [Tg Friend](tg://user?id={lightning_id}) Is Waiting.",
    
    )    



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_ask")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    await lightning.edit("Okay let Me Think🤫")
    await asyncio.sleep(2)
    await lightning.edit("Okay Giving You A Chance🤨")
    await asyncio.sleep(2)
    await lightning.edit(
        "You Will Spam?", buttons= [
        [Button.inline("Yes", data="lemme_ban")],
        [Button.inline("No", data="hmm")],
        ],
    )

    
    reqws = "`Warning`- ❗️⚠️Dont Try Anything Stupid  Wait Kindly!!!❗️⚠️"


    await bot.send_message(lightning.query.user_id, reqws)
    await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Nibba](tg://user?id={lightning_id}). Wants To Request Something.",
        buttons=[Button.url("Contact Him", f"tg://user?id={lightning_id}")],
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))
async def yes_ucan(lightning):
    if lightning.query.user_id == bot.uid:
           lmaoo = "You Are Not Requesting , Lol."
           await lightning.answer(lmaoo, cache_time=0, alert=True)
           return          
    await lightning.get_chat()
    await asyncio.sleep(2)
    await lightning.edit("Okay You Can Wait Till Wait")
    hmmmmm = "Okay Kindly wait  i will inform you"
    await bot.send_message(
              lightning.query.user_id, hmmmmm)
          
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
async def yes_ucan(lightning):
    if lightning.query.user_id == bot.uid:
           lmaoo = "You Are Not Requesting , Lol."
           await lightning.answer(lmaoo, cache_time=0, alert=True)
           return    
    await lightning.get_chat()
    await asyncio.sleep(2)
    await lightning.edit("Get Lost Retard")
    ban = "Get Lost Goin To Block You" 
    await bot.send_message(
         lightning.query.user_id, ban)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stta")))
async def hmm(lightning):
    if lightning.query.user_id == bot.uid:
        text = "🇲‌🇾‌ 🇭‌🇪‌🇱‌🇵‌ 🇸‌🇹‌🇦‌🇹‌🇸‌\n\n**ᴘʟᴜɢɪɴ**-- All Good ✔\nʜᴇʀᴏᴋᴜ - Connected ✔\nʟᴏɢs -- Looks Good :/"
        await lightning.answer(text, alert=True)
    else:
        txt = f"Stats For {LIGHTNINGUSER} Not For You :)"
        await lightning.answer(txt, alert=True)


# Some Inspiration From Telebot
async def lightning_pugins_query_hndlr(lightning):
        if lightning.query.user_id == bot.uid:
            lightning_plug_name = lightning.data_match.group(1).decode("UTF-8")
            lightning_help_strin = ""
            lightning_help_strin += f"Commands Available in {lightning_plug_name} - \n"
            try:
                if lightning_plug_name in CMD_HELP:
                    for i in CMD_HELP[lightning_plug_name]:
                        lightning_help_strin += i
                    lightning_help_strin += "\n"
                else:
                    for i in CMD_LIST[lightning_plug_name]:
                        lightning_help_strin += i
                        lightning_help_strin += "\n"
            except BaseException:
                await lightning.edit(
                    f"{LIGHTNINGUSER}'s  {LIGHTNINGBOT} Has Some Internal Problem Please Restart Dynos Or Ask [Lightning](https://t.me/lightningsupport)")  
            pass
            if lightning_help_strin == "":
                lightning_strike = "{} In Case In Problem.\nUse .help {}".format(
                    lightning_plug_name, lightning_plug_name
                ) # This Code Was Clashing My pm_permit 
            else:
                lightning_strike = lightning_help_strin
            lightning_strike += "\n Use .unload {} to remove this plugin\n\
                If In Case Some Problem Contact @lightningsupport\n From  [Here](https://t.me/lightningsupport)".format(
                lightning_plug_name
            ) # Some Inspiration From Telelbot
            if len(lightning_help_strin) >= 140:
                lightning = "Check your saved messages!"
                await lightning.answer(lightning, cache_time=0, alert=True)
                lightning_help_strin += f"\n\nIm Here With Detailed Help via {LIGHTNINGBOT} Of This Plugin😉"
                if bot is not None and lightning.query.user_id == bot.uid:
                    heh = await bot.send_message("him", lightning_help_strin)
                    await asyncio.sleep(60)
                    await heh.delete()
            else:
                await lightning.answer(lightning_strike, cache_time=0, alert=True)
        else:
            lightning_strike = f"Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"
            await lightning.answer(lightning_strike, cache_time=0, alert=True)

   



    
