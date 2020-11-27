import os

from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os


    class Var(object):
        APP_ID = int(os.environ.get("APP_ID", 6))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(
        int(x) for x in os.environ.get(
            "SUDO_USERS",
            "1097131648").split())
    WHITELIST_USERS = set(
        int(x) for x in os.environ.get(
            "WHITELIST_USERS",
            "832241419").split())
    BLACKLIST_USERS = set(
        int(x) for x in os.environ.get(
            "BLACKLIST_USERS", "").split())
    DEVLOPERS = set(
        int(x) for x in os.environ.get(
            "DEVLOPERS",
            "1105887181").split())
    OWNER_ID = set(
        int(x) for x in os.environ.get(
            "OWNER_ID",
            "1311769691").split())
    SUPPORT_USERS = set(
        int(x) for x in os.environ.get(
            "SUPPORT_USERS", "").split())
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    PMBOT_START_MSSG = os.environ.get("PMBOT_START_MSSG", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "\.")
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    BOT_HANDLER = os.environ.get("BOT_HANDLER", "^/")
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    MAX_FLOOD_IN_P_M_s = os.environ.get("MAX_FLOOD_IN_P_M_s", "3")
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    PMSECURITY = os.environ.get("PMSECURITY", "ON")
    OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
    OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
    # for autopic
    AUTOPIC_TEXT = os.environ.get(
        "AUTOPIC_TEXT",
        "Life Is too Short.\n And so is your Light account.")
    AUTO_PIC_FONT = os.environ.get("AUTOPIC_FONT", "DejaVuSans.ttf")
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", None)
    if AUTH_TOKEN_DATA is not None:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
    if PRIVATE_GROUP_ID is not None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")


class Development(Var):
    LOGGER = True
    # Here for later purposes


if ENV:
    class Config(object):
        LOGGER = True
    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(
        int(x) for x in os.environ.get(
            "SUDO_USERS",
            "1097131648").split())
    WHITELIST_USERS = set(
        int(x) for x in os.environ.get(
            "WHITELIST_USERS",
            "832241419").split())
    BLACKLIST_USERS = set(
        int(x) for x in os.environ.get(
            "BLACKLIST_USERS", "").split())
    DEVLOPERS = set(
        int(x) for x in os.environ.get(
            "DEVLOPERS",
            "1105887181").split())
    OWNER_ID = set(
        int(x) for x in os.environ.get(
            "OWNER_ID",
            "1311769691").split())
    SUPPORT_USERS = set(
        int(x) for x in os.environ.get(
            "SUPPORT_USERS", "").split())
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    PMBOT_START_MSSG = os.environ.get("PMBOT_START_MSSG", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "\.")
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    BOT_HANDLER = os.environ.get("BOT_HANDLER", "^/")
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    MAX_FLOOD_IN_P_M_s = os.environ.get("MAX_FLOOD_IN_P_M_s", "3")
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    PMSECURITY = os.environ.get("PMSECURITY", "ON")
    OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
    OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
    # for autopic
    AUTOPIC_TEXT = os.environ.get(
        "AUTOPIC_TEXT",
        "Life Is too Short.\n And so is your Light account.")
    AUTO_PIC_FONT = os.environ.get("AUTOPIC_FONT", "DejaVuSans.ttf")
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", None)
    if AUTH_TOKEN_DATA is not None:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
    if PRIVATE_GROUP_ID is not None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")

else:
    class Config(object):
        DB_URI = None
        # Add your extra vars if any here
