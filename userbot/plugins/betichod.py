import asyncio
import html
import os
import random
import re
from math import ceil

from telethon import custom, events, functions
from telethon.tl.custom import Button

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST, bot
from userbot.plugins import inlinestats
from userbot.thunderconfig import Config

# ABEE O KANGAR  BACK OPEN CLSE BTN KANG KIYA TO YE LONE CHIPKA DENA AUR GLOBALS K BINA NAHI CHALAGA aur global 5 gaja diff name and manipulation se imported hai
# Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
from userbot.utils import load_module, remove_plugin

# Made With Efforts By Team DC and If Are Using This Give Credits TO Them

# DARK COBRAOriginal 🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍
# kangers Keep Credits 😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒
# Made by Dc-Team
# Don't remove these lines u fool ,,,
#
#
# hehehhe
# Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
# A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara
# Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
# aur  unload load back close open kang kara ya idea bhi le to credit dena pehli 6 line nahi to bhut bura hoga tumara sath


# Made With Efforts By Team DC and If Are Using This Give Credits TO Them

# DARK COBRAOriginal 🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍
# kangers Keep Credits 😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒
# Made by Dc-Team
# Don't remove these lines u fool ,,,
#
#
# hehehhe
# Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
# A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara
# Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
# aur  unload load back close open kang kara ya idea bhi le to credit dena pehli 6 line nahi to bhut bura hoga tumara sath

# Dark Cobra Original 🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍
# kangers Keep Credits 😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒
# Made by Dc-Team
# Don't remove these lines u fool ,,,
#
#
# hehehhe
# Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
# A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara
# Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
# aur  unload load back close open kang kara ya idea bhi le to credit dena pehli 6 line nahi to bhut bura hoga tumara sath


# Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
# A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara
# Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    # 🇦 🇦 🇵     🇾 🇦 🇭 🇦    🇦 🇦 🇾 🇪    🇰 🇮 🇸     🇱 🇮 🇾 🇪 ??

    # 🇨 🇭 🇦 🇱 🇴      🇸 🇮 🇷    🇵 🇱 🇪 🇦 🇸 🇪    🇬 🇪 🇹 🇴 🇺 🇹

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"open")))
    async def opner(event):
        if event.query.user_id == bot.uid:
            current_page_number = 0
            dc = paginate_help(current_page_number, CMD_LIST, "helpme")
            await event.edit(
                "`>>>\n\nReopened The Main Menu of \n©BlackLightning` ", buttons=dc
            )
        else:
            reply_pop_up_alert = "Please get your own Userbot,for more info visit !"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    #       🇮 🇹 🇳 🇦    🇰 🇾 🇺   🇸 🇵 🇾     🇰 🇷    🇷 🇭 🇪     🇭 🇴      🇸 🇭 🇦 🇦 🇩 🇮    🇰 🇷 🇳 🇮    🇭    🇰 🇾 🇦   🇧 🇸 🇩 🇰

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Userbot"):
            rev_text = query[::-1]
            dc = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© Black Lightning Userbot Help",
                text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=dc,
                link_preview=False,
            )
            await event.answer([result] if result else None)
        else:
            reply_pop_up_alert = "Noii Noii!!!! Dont Use This Sir ( ͡ಥ ͜ʖ ͡ಥ) ! "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\((.+?)\)")
        )
    )  # hehe
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))

            dc = paginate_help(current_page_number + 1, CMD_LIST, "helpme")

            await event.edit(buttons=dc)
        else:
            Cobra = "Noii Noii!!!! Dont Use This Sir ( ͡ಥ ͜ʖ ͡ಥ)"
            await event.answer(Cobra, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))

            dc = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )

            await event.edit(buttons=dc)
        else:
            TheDark = "Noii Noii!!!! Dont Use This Sir ( ͡ಥ ͜ʖ ͡ಥ) ! "
            await event.answer(TheDark, cache_time=0, alert=True)

    # hehehehehhehhehhehe
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            danish = custom.Button.inline("◤✞ 𝕺𝖕𝖊𝖓 𝕸𝖆𝖎𝖓 𝕸𝖊𝖓𝖚 𝕬𝖌𝖆𝖎𝖓 ✞◥", data="open")
            await event.edit("`Main Menu Has Been Closed`", buttons=danish)
        else:
            reply_pop_up_alert = "Noii Noii!!!! Dont Use This Sir ( ͡ಥ ͜ʖ ͡ಥ) ! "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if not event.query.user_id == bot.uid:
            atul = "Noii Noii!!!! Dont Use This Sir ( ͡ಥ ͜ʖ ͡ಥ) ! "
            await event.answer(atul, cache_time=0, alert=True)
            return
        plugin_name = event.data_match.group(1).decode("UTF-8")
        global shivam_sh1vam
        shivam_sh1vam = "{}".format(plugin_name)
        help_string = "Commands found in {}:\n".format(plugin_name)
        k = "💠🔮💎"
        u = 0
        for i in CMD_LIST[plugin_name]:
            u += 1
            help_string += str(k[u % 3]) + " " + i + "\n\n"
        if plugin_name in CMD_HELP:
            help_string += (
                f"**📤 PLUGIN NAME 📤 :** `{plugin_name}` \n\n{CMD_HELP[plugin_name]}"
            )
        else:
            help_string += "😁"

        reply_pop_up_alert = help_string
        reply_pop_up_alert += "\n\n __Click on buttons below to load or unload them..report us if you find any bug__\n\n **©BlackLightning USERBOT**".format(
            plugin_name
        )
        try:
            if event.query.user_id == bot.uid:
                dc = [
                    custom.Button.inline(" 𝕭𝖆𝖈𝖐 ", data="back({})".format(shivam)),
                    custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="close"),
                    custom.Button.inline(
                        " 𝖀𝖓𝖑𝖔𝖆𝖉 ", data="unload({})".format(shivam_sh1vam)
                    ),
                ]
                await event.edit(reply_pop_up_alert, buttons=dc)
            else:
                reply_pop_up_alert = "Noii Noii!!!! Dont Use This Sir ( ͡ಥ ͜ʖ ͡ಥ)"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)  # hehe
        except:
            if event.query.user_id == bot.uid:
                sh1vam = [
                    custom.Button.inline(
                        "◤✞ 𝕲𝖔 𝕭𝖆𝖈𝖐 ✞◥", data="back({})".format(shivam)
                    ),
                    custom.Button.inline("◤✞ 𝕮𝖑𝖔𝖘𝖊 ✞◥", data="close"),
                ]
                halps = "Do .help {} to get the list of commands.".format(plugin_name)
                await event.edit(halps, buttons=sh1vam)
            else:
                reply_pop_up_alert = "Noii Noii!!!! Dont Use This Sir ( ͡ಥ ͜ʖ ͡ಥ)"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"load\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:

            #  🇦 🇷 🇪      🇧 🇸 🇩 🇰      🇮 🇸 🇸 🇪    🇰 🇦 🇳 🇬  🇲 🇦 🇹   🇰 🇷    🇷 🇪   🇲 🇨

            try:
                fcix = [
                    custom.Button.inline("  𝕭𝖆𝖈𝖐 ", data="back({})".format(shivam)),
                    custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="close"),
                    custom.Button.inline(
                        " 𝖀𝖓𝖑𝖔𝖆𝖉 ", data="unload({})".format(shivam_sh1vam)
                    ),
                ]
                load_module(
                    event.data_match.group(1).decode("UTF-8")
                )  # kyu sir kang krne m musil aa rhi h kya ... Bolo help kr du kya 😂😂😂
                await event.edit(
                    "`Your Black Lightning Has Successfully loaded` >>>"
                    + str(event.data_match.group(1).decode("UTF-8")),
                    buttons=fcix,
                )
            except Exception as e:
                await event.edit(
                    "Error{}".format(shortname, str(e))
                    + "BlackLightning Has Successfully loaded"
                    + str(event.data_match.group(1).decode("UTF-8")),
                    buttons=fcix,
                )
        else:
            event.data_match.group(1).decode("UTF-8")
            fcix = [
                custom.Button.inline("  𝕭𝖆𝖈𝖐 ", data="back({})".format(shivam)),
                custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="close"),
                custom.Button.inline(
                    " 𝖀𝖓𝖑𝖔𝖆𝖉 ", data="unload({})".format(shivam_sh1vam)
                ),
            ]
            reply_pop_up_alert = "Please get your own Userbot,for more info visit !"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"unload\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:

            try:
                fcix = [
                    custom.Button.inline(" 𝕭𝖆𝖈𝖐 ", data="back({})".format(shivam)),
                    custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="close"),
                    custom.Button.inline(
                        " 𝕷𝖔𝖆𝖉 ", data="load({})".format(shivam_sh1vam)
                    ),
                ]
                remove_plugin(
                    event.data_match.group(1).decode("UTF-8")
                )  # kyu sir kang krne m muskil ho rhi h kya bologe toh help krdu 😂😂
                await event.edit(
                    "`Your BlackLightning Has Successfully unloaded` >>>"
                    + str(event.data_match.group(1).decode("UTF-8")),
                    buttons=fcix,
                )
            except Exception as e:
                await event.edit(
                    "Error{}".format(shortname, str(e))
                    + "BlackLightning Has Successfully unloaded"
                    + str(event.data_match.group(1).decode("UTF-8")),
                    buttons=fcix,
                )
        else:
            event.data_match.group(1).decode("UTF-8")
            fcix = [
                custom.Button.inline("  𝕭𝖆𝖈𝖐 ", data="back({})".format(shivam)),
                custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="close"),
                custom.Button.inline(" 𝕷𝖔𝖆𝖉 ", data="load({})".format(shivam_sh1vam)),
            ]
            reply_pop_up_alert = "Please get your own Userbot,for more info visit !"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)  # hehehe

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):

        if event.query.user_id == bot.uid:
            try:
                current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(current_page_number - 2, CMD_HELP, "helpme")
                await event.edit(
                    ">>> Here Is The Main Menu of\n Currently Loaded Plugins 485\n\n©BlackLightning",
                    buttons=buttons,
                )
            except:
                buttons = paginate_help(0, CMD_HELP, "helpme")
                await event.edit(
                    "`>>> Here Is The Main Menu Of\n\n©BlackLightning`", buttons=buttons
                )
        else:
            reply_pop_up_alert = "Please get your own Userbot,for more info visit !"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = Config.NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD
    multi = Config.EMOJI_TO_DISPLAY_IN_HELP
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline(
            "{} {}".format(random.choice(list(multi)), x), data="us_plugin_{}".format(x)
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    global shivam
    modulo_page = page_number % max_num_pages
    shivam = modulo_page
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "◃:✮𝙿𝚁𝙴𝚅.❃", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("⋇⋆𝙲𝙻✦𝚂𝙴⋆⋇", data="close"),
                custom.Button.inline(
                    "❃.𝙽𝙴𝚇𝚃✮:▹", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


# chal nikal
# gtfo
# SED aagye aap😂

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/63abc60224dc567e3d441.jpg"
else:
    WARN_PIC = PMPERMIT_PIC
LOG_CHAT = Config.PRIVATE_GROUP_ID
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Black"


#    TeleBot - UserBot
#    Copyright (C) 2020 TeleBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from telethon import Button
from telethon.tl.functions.users import GetFullUserRequest

from userbot import CUSTOM_PMPERMIT, bot
from userbot.Config import Var
from userbot.plugins import inlinestats

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
TELEPIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/92cfbab6598148837c2e4.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
mybot = Var.TG_BOT_USER_NAME_BF_HER
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Var.PRIVATE_GROUP_ID
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "`ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ PM security! Please wait for me to approve you. 😊"
)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ User"
USER_BOT_WARN_ZERO = "`I had warned you not to spam. Now you have been blocked and reported until further notice.`\n\n**GoodBye!** "

if Var.LOAD_MYBOT == "True":
    USER_BOT_NO_WARN = (
        "**PM Security of [{}](tg://user?id={})**\n\n"
        "{}\n\n"
        "For immediate help, PM me via {}"
        "\nPlease choose why you are here, from the available options\n\n".format(
            DEFAULTUSER, myid, MESAG, botname
        )
    )
elif Var.LOAD_MYBOT == "False":
    USER_BOT_NO_WARN = (
        "**PM Security of [{}](tg://user?id={})**\n\n"
        "{}\n"
        "\nPlease choose why you are here, from the available options\n".format(
            DEFAULTUSER, myid, MESAG
        )
    )

CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "⨵")
HELP_ROWS = int(os.environ.get("HELP_ROWS", 5))
HELP_COLOUMNS = int(os.environ.get("HELP_COLOUMNS", 3))

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("`Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ Help",
                text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ Stats For [{DEFAULTUSER}](tg://user?id={myid})**\n\n__Bot is functioning normally, master!__\n\n(c) @lightningsupport",
                buttons=[
                    [custom.Button.inline("Stats", data="statcheck")],
                    [Button.url("Repo", "https://github.com/KeinShin/Black-Lightning")],
                    [
                        Button.url(
                            "Deploy Now!",
                            "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FKeinShin%2FBlack-Lightning&template=https%3A%2F%2Fgithub.com%2FKeinShin%2FBlack-Lightning",
                        )
                    ],
                ],
            )
        elif event.query.user_id == bot.uid and query.startswith("**PM"):
            TELEBT = USER_BOT_NO_WARN.format(DEFAULTUSER, myid, MESAG)
            result = builder.photo(
                file=TELEPIC,
                text=TELEBT,
                buttons=[
                    [
                        custom.Button.inline("Request ", data="req"),
                        custom.Button.inline("Chat 💭", data="chat"),
                    ],
                    [custom.Button.inline("To spam 🚫", data="heheboi")],
                    [custom.Button.inline("What is this ❓", data="pmclick")],
                ],
            )
        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ - Telegram Userbot.",
                buttons=[
                    [
                        Button.url(
                            "Repo", "https://github.com/KeinShin/Black-Lightning"
                        ),
                        Button.url(
                            "Deploy",
                            "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FKeinShin%2FBlack-Lightning&template=https%3A%2F%2Fgithub.com%2FKeinShin%2FBlack-Lightning",
                        ),
                    ],
                    [Button.url("Support", "https://t.me/lightningsupport")],
                ],
            )
        else:
            result = builder.article(
                "Source Code",
                text="**Welcome to ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ**\n\n`Click below buttons for more`",
                buttons=[
                    [custom.Button.url("Creator👨‍🦱", "https://t.me/krish1303y")],
                    [
                        custom.Button.url(
                            "👨‍💻Source Code‍💻",
                            "https://github.com/KeinShin/Black-Lightning",
                        ),
                        custom.Button.url(
                            "Deploy 🌀",
                            "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FKeinShin%2FBlack-Lightning&template=https%3A%2F%2Fgithub.com%2FKeinShin%2FBlack-Lightning",
                        ),
                    ],
                    [
                        custom.Button.url(
                            "Updates and Support Group↗️",
                            "https://t.me/lightningsupport",
                        )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Noi Noi!!! Not For You Sar( ͡ಥ ͜ʖ ͡ಥ) "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Noi Noi!!! Not For You Sar( ͡ಥ ͜ʖ ͡ಥ) "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"This is the PM Security for {DEFAULTUSER} to keep away spammers and retards.\n\nProtected by [ʙʟᴀᴄᴋ ʟɪɢʜᴛɴɪɴɢ](t.me/lightningsupport)"
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"reopen")))
    async def megic(event):
        if event.query.user_id == bot.uid:
            buttons = paginate_help(0, CMD_LIST, "helpme")
            await event.edit("Menu Re-opened", buttons=buttons)
        else:
            reply_pop_up_alert = "This bot ain't for u!!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Noi Noi!!! Not For You Sar( ͡ಥ ͜ʖ ͡ಥ) "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Okay, `{DEFAULTUSER}` would get back to you soon!\nTill then please **wait patienly and don't spam here.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) is **requesting** something in PM!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Noi Noi!!! Not For You Sar( ͡ಥ ͜ʖ ͡ಥ) "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oho, you want to chat...\nPlease wait and see if {DEFAULTUSER} is in a mood to chat, if yes, he will be replying soon!\nTill then, **do not spam.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to PM you for **Random Chatting**!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"plshelpme")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Noi Noi!!! Not For You Sar( ͡ಥ ͜ʖ ͡ಥ) "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oh!\n{DEFAULTUSER} would be glad to help you out...\nPlease leave your message here **in a single line** and wait till I respond 😊"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to PM you for **help**!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"heheboi")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Noi Noi!!! Not For You Sar( ͡ಥ ͜ʖ ͡ಥ) "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oh, so you are here to spam 😤\nFuck Off and Dont Come .\n\n**Btw Your message has been read and successfully ignored**."
            )
            await borg(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await tgbot.send_message(
                LOG_GP,
                f"[{first_name}](tg://user?id={ok}) tried to **spam** your inbox.\nHenceforth, **blocked**",
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"statcheck")))
    async def rip(event):
        text = inlinestats
        await event.answer(text, alert=True)

    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Noi Noi!!! Not For You Sar( ͡ಥ ͜ʖ ͡ಥ) "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            help_string += f"Commands Available in {plugin_name} - \n"
            try:
                if plugin_name in CMD_HELP:
                    for i in CMD_HELP[plugin_name]:
                        help_string += i
                    help_string += "\n"
                else:
                    for i in CMD_LIST[plugin_name]:
                        help_string += i
                        help_string += "\n"
            except BaseException:
                pass
            if help_string == "":
                reply_pop_up_alert = "{} has no detailed info.\nUse .help {}".format(
                    plugin_name, plugin_name
                )
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                © Black Lightning".format(
                plugin_name
            )
            if len(help_string) >= 140:
                oops = "List too long!\nCheck your saved messages!"
                await event.answer(oops, cache_time=0, alert=True)
                help_string += "\n\nThis will be auto-deleted in 1 minute!"
                if bot is not None and event.query.user_id == bot.uid:
                    ok = await bot.send_message("me", help_string)
                    await asyncio.sleep(60)
                    await ok.delete()
            else:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "Noi Noi!!! Not For You Sar( ͡ಥ ͜ʖ ͡ಥ) "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


async def userinfo(event):
    target = await event.client(GetFullUserRequest(event.query.user_id))
    first_name = html.escape(target.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    return first_name
