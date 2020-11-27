from userbot import topfunc
from userbot.Config import Var, Config
from userbot.utils import admin_cmd


idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
issudousing = Var.SUDO_USERS
islogokay = Var.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdriveisshit = Var.AUTH_TOKEN_DATA
wttrapi = Var.OPEN_WEATHER_MAP_APPID
rmbg = Var.REM_BG_API_KEY
hmmok = Var.LYDIA_API
currentversion = "3.0"
if issudousing:
    amiusingsudo = "Active ✅"
else:
    amiusingsudo = "Inactive ❌"

if islogokay:
    logchat = "Connected ✅"
else:
    logchat = "Dis-Connected ❌"

if isherokuokay:
    riplife = "Connected ✅"
else:
    riplife = "Not Connected ❌"

if gdriveisshit:
    wearenoob = "Active ✅"
else:
    wearenoob = "Inactive ❌"

if rmbg:
    gendu = "Added ✅"
else:
    gendu = "Not Added ❌"

if wttrapi:
    starknoobs = "Added ✅"
else:
    starknoobs = "Not Added ❌"

if hmmok:
    meiko = "Added ✅"
else:
    meiko = "Not Added ❌"

if isdbfine:
    dbstats = "Fine ✅"
else:
    dbstats = "Not Fine ❌"

inlinestats = (
    f"✘ SHOWING Lightning STATS ✘\n"
    f"VERSION = {currentversion} \n"
    f"DATABASE = {dbstats} \n"
    f"SUDO = {amiusingsudo} \n"
    f"LOG-CHAT = {logchat} \n"
    f"HEROKU = {riplife} \n"
    f"G-DRIVE = {wearenoob}"
)