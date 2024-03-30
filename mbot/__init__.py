import logging
from os import environ, mkdir, path, sys
from dotenv import load_dotenv
from pyrogram import Client
import time
from telethon import TelegramClient, events, functions, types
#from httpx import AsyncClient, Timeout
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import telebot

CMD = ["/", ".", "?", "#", "!", "mg", "mx", ","]


formatter = logging.Formatter('%(levelname)s %(asctime)s - %(name)s - %(message)s')

fh = logging.FileHandler(f'{__name__}.log', 'w')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.addHandler(ch)

telethon_logger = logging.getLogger("telethon")
telethon_logger.setLevel(logging.WARNING)
telethon_logger.addHandler(ch)
telethon_logger.addHandler(fh)

botStartTime = time.time()
load_dotenv()



# Log
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

# Mandatory Variable
try:
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    BOT_TOKEN = environ["BOT_TOKEN"]
    OWNER_ID = int(environ["OWNER_ID"])
except KeyError:
    LOGGER.debug("One or More ENV variable not found.")
    sys.exit(1)
# Optional Variable
SUDO_USERS = environ.get("SUDO_USERS", str(OWNER_ID)).split()
SUDO_USERS = [int(_x) for _x in SUDO_USERS]
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)
AUTH_CHATS = environ.get("AUTH_CHATS", "-1001954979279").split()
AUTH_CHATS = [int(_x) for _x in AUTH_CHATS]
#LOG_GROUP = environ.get("LOG_GROUP", None)
#if LOG_GROUP:
#    LOG_GROUP = int(LOG_GROUP)


#TELETHON BOT RUNNER
bot = TelegramClient(__name__, API_ID, API_HASH, base_logger=telethon_logger).start(bot_token=BOT_TOKEN)
logger.info("TELETHON BOT STARTED BROO")

# TELE BOT RUNNER
tbot = telebot.TeleBot(BOT_TOKEN) 

#PYTHON BOT RUNNER
class Mbot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir="./cache/",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            sleep_threshold=30,
        )
    async def start(self):
      #  os.system(f"rm -rf ./cache/")
     #   os.system(f"mkdir ./cache/")
        global BOT_INFO
        await super().start()
        BOT_INFO = await self.get_me()
        if not path.exists('/tmp/thumbnails/'):
            mkdir('/tmp/thumbnails/')
        for chat in AUTH_CHATS:
            await self.send_photo(chat,"https://telegra.ph/file/d72fe4abc50fbe5787672.jpg","**Bot is ReStarted**")
        LOGGER.info(f"X Bot Module Started As {BOT_INFO.username}\n")
        
    async def stop(self, *args):
        await super().stop()
        LOGGER.info("\n__________             ._.\n\______   \___.__. ____| |\n|    |  _<   |  |/ __ \ |\n|    |   \\\___  \  ___/\|\n|______  // ____|\___  >_\n        \/ \/         \/\/\n\nBot Stopped, Bye.")
