# You Are Free To Use  But Pls Gib The Credits
# Made By @krish1303y,@cyper666, @Atank_ka_devata( Never Gonna Forgive Him 😑😑 nvm thx)   For black lightning  🔥🔥🔥
# Thanks @Shivam_Patel Mujhe Samjhane Ke Liye 
# Thanks @Shivam_Patel For Your kind Help Sir 😘😘❤️
# Special Credits to @Shivam_Patel For Helping Us
import os
import re
import json
from math import ceil
import time

from telethon import Button, custom, events, functions

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST, bot
from userbot.plugins import lightning_status


LIGHT_LOGS = Config.PRIVATE_GROUP_ID
LIGHTNINGUSER = str(ALIVE_NAME) if ALIVE_NAME else "Userbot"
lightning_bot = Var.TG_BOT_USER_NAME_BF_HER
import asyncio

from datetime import datetime
from pathlib import Path


from userbot.utils import admin_cmd, load_module, remove_plugin

DELETE_TIMEOUT = 5


thumb_image_path = "./resources/541200.png"

LIGHTNINGUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lightning"




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
                await event.edit(f"Wait Installing.... ")
                await asyncio.sleep(2)
                await event.edit(
                    "{}SucessFully Installed ....".format(
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
            f"Hey {LIGHTNINGUSER} Heres The Help Menu",
            text="{}\nI Have Tottal  Loaded Plugins: {}".format(query, len(CMD_LIST)),
            lightning_button=lightning_button,
            link_preview=False,
        )
        await event.answer([result])
    elif event.query.user_id == bot.uid and query == "Help":
        result = builder.article(
            title="Help",
            text=f"**How If Face Problem \n{LIGHTNINGUSER}** \nChoose Your Problem For Help ",
            buttons=[
                [custom.Button.inline("Help", data="what?")],
                [Button.url("Commands Not Working🥺", "https://t.me/lightningsupport")],
                [Button.url("Help Article 🤓", "https://t.me/lightningsupport")],
                [
                    Button.url(
                
                    "Want To Learn CMDS😅",
                    "https://t.me/lightningsupport" ,
                    )
                ], 
            ],

        )
        await event.answer([result])
    elif event.query.user_id == bot.uid and query.startswith("**Black L"):
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
                [
                    custom.Button.inline(
                        "Fuck Lemme In", 
                        data="lol_u_think_so",
                        
                    )
                        
                ],

            ],
            )
    await event.answer([result]) if result else None


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


# Some Inspiration From Telelbot
async def lightning_pugins_query_hndlr(event):
        if event.query.user_id == bot.uid:
            lightning_plug_name = event.data_match.group(1).decode("LOL-8")
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
                pass
            if lightning_help_strin == "":
                lightning_strike = "{} In Case In Problem.\nUse .help {}".format(
                    lightning_plug_name, lightning_plug_name
                ) # This Code Was Clashing My pm_permit 
            else:
                lightning_strike = lightning_help_strin
            lightning_strike += "\n Use .unload {} to remove this plugin\n\
                If In Case Some Problem Contact @lightningsupport".format(
                lightning_plug_name
            ) # Some Inspiration From Telelbot
            if len(lightning_help_strin) >= 200:
                lightning = "Check your saved messages!"
                await event.answer(lightning, _lightning_power=0, alert=True)
                lightning_help_strin += "\n\nThis will be auto-deleted in 1 minute!"
                if bot is not None and event.query.user_id == bot.uid:
                    ok = await bot.send_message("Whaa", lightning_help_strin)
                    await asyncio.sleep(60)
                    await ok.delete()
            else:
                await event.answer(lightning_strike, _lightning_power=0, alert=True)
        else:
            lightning_strike = f"Please Dont Touch This {LIGHTNINGUSER} Im Tryin To Get Rid Of This !!"
            await event.answer(lightning_strike, _lightning_power=0, alert=True)



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"what?")))
async def lightning_is_better(event):
    if event.query.user_id == bot.uid:
        fck_bit = f"{LIGHTNINGUSER} Dont Use This Pls 🥺 "
        await event.answer(fck_bit, alert=True)
    else:
        txt = f"Ohh C'mon You Think That This Is For You?\n Ok I Will Complain To {LIGHTNINGUSER}👀👀"
        await event.answer(txt, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lightning_is_here_cant_spam")))
async def lightning_is_better(event):
    if event.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    await event.get_chat()
    lightning_id = event.query.user_id
    text1 = f"LOL You Think So You Can😂😂\n\n[Nibba](tg://user?id={lightning_id} Bye Goin To Block You Gay😂😂"
    await event.edit("Off Course Go To Hell Dude")
    await bot.send_message(event.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(event.query.user_id))
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Nibba](tg://user?id={lightning_id}) Tryin To Spam \n\n**So Blocked**.",
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_u_think_so")))
async def lightning_is_better(event):
    if event.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    await event.get_chat()
    lightning_id = event.query.user_id
    text1 = f"LOL You Think So You Can😂😂\nGo and wait😂😂"
    await event.edit("Off Course Go To Hell Dude")
    await bot.send_message(event.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(event.query.user_id))
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Nibba](tg://user?id={lightning_id}) Tryin To Enter With Out approval😂 \n.",
    )



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lightning_back_it")))
async def krish1303y(event):
    if event.query.user_id != bot.uid:
        fck_bit = "None Of Your Bussiness No Need To Touch This!!!!"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    await event.answer("Back", _lightning_power=0, alert=False)
    # This Is Copy of Above Code. (C) @SpEcHiDe
    lightning_button = lightnings_menu_for_help(0, CMD_HELP, "fuck_him")
    krish1303y = f"""Black Lightning  Listed The Plugins Read This Info Pls!\n
{LIGHTNINGUSER}If You Faced Problem Regarding Pls Contact For Help  @lightningsupport \n**Btw**Currently Loaded Plugins: {len(CMD_LIST)}"""
    await event.edit(message=krish1303y, lightning_button=lightning_button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"he_sucks")))
async def lightning_is_better(event):
    if event.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    await event.get_chat()
    lightning_id = event.query.user_id
    await event.edit("Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** You Can Wait For My Master ")
    text2 = f"Oh K. {LIGHTNINGUSER} Is Helping Someone\n {LIGHTNINGUSER}Helps EveryOne So Pls Wait . Pls Dont Spam Im Here To Protect {LIGHTNINGUSER} I Could Ban You If You Spammed."
    await bot.send_message(event.query.user_id, text2)
    await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [New User](tg://user?id={lightning_id}). You Friend His Here To Chat pls See The Message [New User](tg://user?id={lightning_id}) Is Waiting.",
        lightning_button=[Button.url("Contact Him", f"tg://user?id={lightning_id}")],
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_ask")))
async def lightning_is_better(event):
    if event.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await event.answer(fck_bit, _lightning_power=0, alert=True)
        return
    await event.get_chat()
    lightning_id = event.query.user_id
    await event.edit("So You Want Some Help He Is Here \n**BTW** Choice Accepted")
    text3 = "Ok, Wait. You can Ask After Master Approves You. Kindly, Wait."
    await bot.send_message(event.query.user_id, text3)
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
                                                              
    
"""inline wspr

Credits to Javes and @Shivam_Patel a
Special Thanks To @criminaL786 For Giving Me This Inline Wspr
"""
@tgbot.on(events.InlineQuery)  
async def inline_handler(event):
  me = await bot.get_me()  
  builder = event.builder
  query = event.text
  split = query.split(' ', 1) 
  result = None 
  what = re.compile("wspr (.*) (.*)") 
  match = re.findall(what, query)
  if event.query.user_id == me.id and match:
            query = query[7:]
            user, txct = query.split(" ", 1)
            builder = event.builder
            secret = os.path.join("./userbot", "secrets.txt")
            try:
                jsondata = json.load(open(secret))
            except:
                jsondata = False
            try:
                # if u is user id
                u = int(user)
                try:
                    u = await event.client.get_entity(u)
                    if u.username:
                        krish = f"@{u.username}"
                    else:
                        krish = f"[{u.first_name}](tg://user?id={u.id})"
                except ValueError:
                    # ValueError: Could not find the input entity
                    krish = f"[user](tg://user?id={u})"
            except ValueError:
                # if u is username
                try:
                    u = await event.client.get_entity(user)
                except ValueError:
                    return
                if u.username:
                    krish = f"@{u.username}"
                else:
                    krish = f"[{u.first_name}](tg://user?id={u.id})"
                u = int(u.id)
            except:
                return
            timestamp = int(time.time() * 2)
            newsecret = {str(timestamp): {"userid": u, "text": txct}}

            buttons = [
                custom.Button.inline("Show Message 🔐", data=f"secret_{timestamp}")
            ]
            result = builder.article(
                title=f"Whisper To {krish}",
                text=f"🔒 A whisper message to {krish}, Only {krish} can open it.",
                buttons=buttons,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(newsecret)
                json.dump(jsondata, open(secret, "w"))
            else:
                json.dump(newsecret, open(secret, "w"))  
 
    
    #some codes taken form Cat bot Fixing them to javes was a task #Shivam
