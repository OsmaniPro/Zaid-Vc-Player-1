## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5253002724:AAHvqxxpWE-fvmQe5F8DBvRE7OQC_6J5Um0")
BOT_NAME = getenv("BOT_NAME", "Osmani")

API_ID = int(getenv("API_ID", "14547608"))
API_HASH = getenv("API_HASH", "c6c5e34f44bc5dd80dd2a4b894c7bcff")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Osmani_Player_Bot:ribaj@cluster0.780ql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "OsmaniBot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ribajosmani")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "Mss_Rosan_Bot)
OWNER_ID = getenv("OWNER_ID", "1008271006")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ribmusic")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "osmanigroupbot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "teamosmani")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1008271006").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/67ed559f31924bdc34976.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/2393b93e9d7c5f3ec68f8.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "45000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
