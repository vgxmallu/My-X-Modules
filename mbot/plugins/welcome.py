import os
from unidecode import unidecode
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from mbot import LOGGER
from pyrogram.types import Message


from mbot import SUDO_USERS as SUDOERS
from mbot import Mbot as app
#from mbot.utils.Database import *
#from config import LOG_CHANNEL

LOGGER = getLogger(__name__)


class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(450, 450)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chat, id, uname):
    background = Image.open("mbot/assets/WELL2.PNG")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize(
        (450, 450)
    ) 
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('mbot/assets/font.ttf', size=50)
    font2 = ImageFont.truetype('mbot/assets/font.ttf', size=90)
    draw.text((65, 250), f'NAME : {unidecode(user)}', fill=(255, 255, 255), font=font)
    draw.text((65, 340), f'ID : {id}', fill=(255, 255, 255), font=font)
    draw.text((65, 430), f"USERNAME : {uname}", fill=(255,255,255),font=font)
    pfp_position = (767, 133)  
    background.paste(pfp, pfp_position, pfp)  
    background.save(
        f"downloads/welcome#{id}.png"
    )
    return f"downloads/welcome#{id}.png"

"""
@app.on_message(filters.command("swel") & ~filters.private)
async def auto_state(_, message):
    usage = "**✦ ᴜsᴀɢᴇ ➠** /swel [ᴇɴᴀʙʟᴇ|ᴅɪsᴀʙʟᴇ]"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
      A = await wlcm.find_one({"chat_id" : chat_id})
      state = message.text.split(None, 1)[1].strip()
      state = state.lower()
      if state == "enable":
        if A:
           return await message.reply_text("✦ Special Welcome Already Enabled")
        elif not A:
           await add_wlcm(chat_id)
           await message.reply_text(f"✦ Enabled Special Welcome in {message.chat.title}")
      elif state == "disable":
        if not A:
           return await message.reply_text("✦ Special Welcome Already Disabled")
        elif A:
           await rm_wlcm(chat_id)
           await message.reply_text(f"✦ Disabled Special Welcome in {message.chat.title}")
      else:
        await message.reply_text(usage)
    else:
        await message.reply("✦ Only Admins Can Use This Command")
"""
#bhag 

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(bot, member: ChatMemberUpdated):
    chat_id = member.chat.id
    count = await bot.get_chat_members_count(member.chat.id)
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await bot.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "assets/NODP.PNG"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await bot.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption= f"""
**
**⁣✦ WELCOME TO ♣️MUSIC🎵GALAXY♣️ ✦**

× Name : {user.mention}
× User name : @{user.username}
× User id : {user.id}
× Total members : {count}

๏ Powered by : **๛ @GojoSatoru_Xbot**
""",
reply_markup=InlineKeyboardMarkup(
[
[InlineKeyboardButton(f"Read rules!", url=f"http://t.me/Hydra_Maneger_bot?start=regole_-1001671054664"),
]
]
))

    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass
  
