import time
import os
from os import getenv
from dotenv import load_dotenv
from os import environ
if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}

#MOMGO_DATABASE
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME" , "GojoSatoru_Xbot")

#LOGS_CHANNEL_&_GROUP
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001784386455"))
LOG_GROUP_ID = environ.get("LOG_GROUP_ID")
CHANNEL_FORWARD_TO = int(os.environ.get("CHANNEL_FORWARD_TO"))
#AUTHENTICATED_USERS
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
OWNER_ID = int(getenv("OWNER_ID", "784589736"))
SUDO = list(
    {
        int(x)
        for x in environ.get(
            "SUDO",
            "784589736",
        ).split()
    }
)

#BORADCAST
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))

#RANDOM_VARIABELS
CHROME_BIN = os.environ.get("CHROME_BIN",  "/usr/bin/google-chrome-stable")

#API_MODULS
CURRENCY_API = environ.get("CURRENCY_API")
GPT_API = os.environ.get("GPT_API")
DAXX_API = os.environ.get("DAXX_API")
DEEP_API = os.environ.get("DEEP_API")
