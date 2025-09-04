import os
import traceback
import logging
import random
import asyncio
import pytz, datetime
import time 

from pyrogram import filters, StopPropagation,  __version__ as pyrover
from pyrogram.types import WebAppInfo, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup 
#from pyrogram.errors import UserNotParticipant
from config import LOG_CHANNEL, AUTH_USERS, DB_URL, DB_NAME, PICS, Telegram
#from pyrogram.types import Message
from handlers.broadcast import broadcast
from handlers.check_user import handle_user_status
from handlers.database import Database
from random import choice
#from config import Telegram
from mbot import Mbot, CMD #botStartTime
#from mbot.utils.upt import get_readable_time
#from mbot.utils.tm import ISTIME
from mbot.cor import pyro_cooldown
db = Database(DB_URL, DB_NAME)
#from gtts import gTTS
#f_sub = "songdownload_group"
#photo = f"https://telegra.ph/file/fcd069fccdcf4d74eb5fb.jpg"
#CMD = ["/", ".", "?", "#", "+", "mg"]


"""
Hello {}, I am Music 𝕏 dl 

I am simple and faster music downloader bot for TG,
&
I can download music from Spotify, YouTube | YouTube Music, Deezer, SoundCloud, MixCloud and Facebook platform's.


        if time < 12:
            get="Good Morning🌄"
        elif time < 15:
            get="Good Afternoon🏞️"
        elif time < 19:
            get="Good Evening🌅"
        else:
            get="Good Night🌌"

     m = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
    time = m.hour
    if time < 12:
        get="❤️☺️🌟"
    elif time < 3:
        get="💝😒😽"
    elif time < 4:
        get="🖤😗💨"
    elif time < 5:
        get="💔😔🌠"
    elif time < 6:
        get="🧡🌝🌱"
    elif time < 7:
        get="❤️‍🩹🙀👯"
    elif time < 8:
        get="💛🤗✨"
    elif time < 9:
        get="❣️🌬️🥶"
    elif time < 10:
        get="💚😻🌀"
    elif time < 11:
        get="❤️‍🔥😎🍁"
    elif time < 13:
        get="💙🕺💃"
    elif time < 14:
        get="💟😱🗿"
    elif time < 15:
        get="💜🌞🍃"
    elif time < 16:
        get="🤎🧐🏖️"
    elif time < 17:
        get="♥️🤪🚶"
    elif time < 18:
        get="💘😶‍🌫️❄️"
    elif time < 19:
        get="🤍🥰🌈"
    else:
        get="💓💤😴"

And I can download music from Spotify, YouTube | YouTube Music, Deezer, SoundCloud and MixCloud platform's.

@Client.on_message(filters.command("time"))
async def india_time(bot, hydrix):
    await hydrix.reply_text(f"{ISTIME}")

InlineKeyboardButton("Deezer ⤵️", callback_data="hmm")
            ],[
                InlineKeyboardButton("Search Track 🎧", switch_inline_query_current_chat="dt "),
                InlineKeyboardButton("Search Album 💽", switch_inline_query_current_chat="da ")
            ],[
                InlineKeyboardButton("Search Playlist 🗂️",  callback_data="soon"),
                InlineKeyboardButton("Search Artist 🗣️",  callback_data="soon")
            ],[
                InlineKeyboardButton("Spotify ⤵️", callback_data="hmm")
            ],[
                InlineKeyboardButton("Search Track 🎧", switch_inline_query_current_chat="st "),
                InlineKeyboardButton("Search Album 💽",  switch_inline_query_current_chat="sa ")
            ],[
                InlineKeyboardButton("Search Playlist 🗂️",  switch_inline_query_current_chat="sp "),
                InlineKeyboardButton("Search Artist 🗣️",  switch_inline_query_current_chat="ar ")
            ],[
               InlineKeyboardButton("YouTube ⤵️",  callback_data="hmm")
            ],[
               InlineKeyboardButton("YouTube Search 🔎",  switch_inline_query_current_chat="yt "),
               InlineKeyboardButton("YouTube Playlist 🗂️",  callback_data="soon")


   InlineKeyboardButton("🟦 Facebook", callback_data="fb"),
        InlineKeyboardButton("🟪 Instagram", callback_data="ig")
        ],[
        InlineKeyboardButton("🟥 Pinterest", callback_data="pt"),
        InlineKeyboardButton("⬛ TikTok", callback_data="tt")
        ],[
"""


#========================START_CMD===============================
start_cmd = """
__Hi {}

My name is 𝗠ᴜsɪᴄ•𝕏•𝗗ʟ Bot🤗
I can download songs from Spotify, YouTube, Deezer and Soundcloud platforms🎙️📼. You can also use Search🔍 songs in my inline quarys anywhere🌐, and Listen Tens Of Millions Of Tracks And Albums From Your Favourite Artists.

Click help for more know me__
"""

ms_stt = """
Some times bot will be slow, because of Server Overload :(
"""
#InlineKeyboardButton('🎺 Web Stream', callback_data="wba"),
startbt = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📣 My Channel', url='https://t.me/XBots_X'),
                InlineKeyboardButton('🎵 My Group', url='https://t.me/songdownload_group')
            ],[
                InlineKeyboardButton('🪩 [SM] x Dl', url='https://t.me/SocialMediaX_dlbot'),
                InlineKeyboardButton('♐ Log Channel', url='https://t.me/music_database_tg')
            ],[
                InlineKeyboardButton('👾 About', callback_data='about'),
                InlineKeyboardButton('📚 Help', callback_data='cmds'),
                InlineKeyboardButton('✈️ Share', callback_data='shr'),
                InlineKeyboardButton("🌀 Inline", switch_inline_query_current_chat="") 
            ],[
                InlineKeyboardButton('❌', callback_data='close')
            ]
        ]
  )
#for tts
#Disclaimer = """ This Audio Is Generated by Music X dl bot, Join My Music Galaxy group on Telegram."""

str2 = """
Hello user! my name is Music X Dl Bot, i can download songs from Spotify, YouTubez, Deezer and Soundcloud platforms.   You can also use Search songs in my inline quarys anywhere, and Listen Tens Of Millions Of Tracks And Albums From Your Favourite Artists. Click help for more know me...
"""

#Thanks = """ And Thanks for Using Music X Dl Bot powered by lofi."""
#=======================================================

x = ["❤️", "💛", "💚", "🤍", "💙", "💜", "🖤", "💟", "♥️", "🎧", "💝", "💖", "💞", "❤️‍🔥", "💋"]
gg = random.choice(x)

h = ["Hi", "Hello", "Hey", "Hey there!", "Hola", "Greetings!", "Ciao!"]
hy = random.choice(h)

SPY = (
    "https://telegra.ph/file/a9670492ac8868116eb08.jpg",
    "https://telegra.ph/file/913335a9c41f74d1f7efb.jpg",
    "https://telegra.ph/file/4d25224ea391746af1211.jpg",
)

MSX_STRINGS = (
    "CAACAgEAAxkDAAKg8mT-4wY-Picz1BhLV91MSZ6IYaFPAALnAgACQs_QR2mt6ItVf91dHgQ",
    "CAACAgEAAxkBAAKg9WT-4xx-YmF9FavJjY9Og30xH9ULAAJYBAAC8-HQRwbl78wzp30UHgQ",
    "CAACAgEAAxkBAAKg-GT-4y7W5FD-vOxDoelqvRHkO0gHAAJCAwACiuHIR-Yb6lOLJFnxHgQ",
    "CAACAgEAAxkBAAKg-2T-41hWDWtUShZxnAABQNeqNeK8fAACEwMAArL2yEefMTswpMAzOB4E",
    "CAACAgEAAxkBAAKg_mT-43PKThW9OxcvYHgHszdbGm1TAALdBgACdV_JR8Sz2xVsNFpBHgQ",
    "CAACAgEAAxkBAAKhBWT-46StidBW7KgGowHLDWkNr5LGAAIzBAAC6VDQR6KOjBf2IYtqHgQ",
    "CAACAgUAAxkBAAKhC2T-4_1LO-PfNM720t9YGU-TYGy3AAJADQACoziQV-Vajy9Y9zIGHgQ",
    "CAACAgUAAxkBAAKhDmT-5CBERt_0WiXajfAX6YS5IjI1AALeCQACwOaRV2BaVuJ5tL5_HgQ",
    "CAACAgUAAxkBAAKhEWT-5E3Tamp_zOCJBFBntvRQ7lpIAAJXCgACBnGRV4Cs2r7NpkGHHgQ",
    "CAACAgUAAxkBAAKhFGT-5F-_QjCO9oah8yxIDLTnKb9dAAIeDAACt6GJVzg-6d0FA0JUHgQ",
    "CAACAgUAAxkBAAKhF2T-5IJs6uCsa_zIfAAB1ngjLONiYgACYQoAAh13kFfBIMtI1JSHPB4E",
    "CAACAgEAAxkDAAEBZJFlR6ZXkOpYmI2oLpLBfg3zZr38mAACUwMAAl0cYUR-BTPriW-AUh4E",
    "CAACAgUAAxkBAAKhGmT-5JwGbLs9b_x_w1IXfjVG317vAAIRCwACMU_QV80e0JCtD8pRHgQ",
    "CAACAgIAAxkBAAEBmHdlV6gtZLqQJLq2Zy1eV02KpwQEtQAC7RoAApYxkEh50_wVYXBNVR4E",
    "CAACAgIAAxkDAAEBmHxlV6hNuA3Ic_qvldvTxnyu9-y6YAACsSIAAs25kEhsSC8vbUU96x4E",
    "CAACAgIAAxkBAAEBmTtlV6i3smjlD5qFFfS01GigsAcfeQACFhsAAhjWsUhN252rlRG2qB4E",
    "CAACAgIAAxkBAAEBmXhlV6jVdSGzMv7njqi6_2v-BW5UCgAC_SIAArNDeEo_ZBDXk999UR4E",
    "CAACAgUAAxkBAAEBmd1lV6kJQxKCc16I1bAadMkCirkUIQACOQwAAp7yGFUcW_DlBBLLsh4E",
    "CAACAgUAAxkBAAEBmi5lV6kz0HD5Z4mrvITXzZqXuCkKHgACnwcAAvQIGFWBaY4JiDuoCB4E",
    "CAACAgUAAxkBAAEBmldlV6lGvB84R1MqT7svjvlncG3A7wACGwkAAt-qGFXZljaP--_RNR4E",
    "CAACAgUAAxkBAAEBmo5lV6lh0Vtqz1FxE6qUmB5azGdCxwACJgkAAs6AGVXIVWa6C6V34B4E",
    "CAACAgUAAxkBAAEBmyhlV6m0vnlx0xTeggh05rD_OjH7DwACHgoAAsmuGVVnKBvEVZZMvB4E",
    "CAACAgUAAxkBAAEBm1FlV6nMhFGOuNK0K7YAAZQLMfo5LMEAAowJAAKyCRlVFsgYIWfnVfseBA",
    "CAACAgUAAxkBAAEBm2xlV6nlXloVF3ztER4SOBG7FF9xrgACqQoAAnmvGFWxfDyUI6qURR4E",
)
stickers_ran = random.choice(MSX_STRINGS)

@Mbot.on_message(filters.command("alive", CMD) & pyro_cooldown.wait(10))
async def check_alive(_, message):
    await message.reply_text("ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് /start ചെയ്തു നോക്ക്..🙂")
    await message.reply_text("I am not dead😒, im here.. You have no love for me now🥺. Good.. 😔 You're not as changed..Just try to do a little bit of /start ...🙂🙃😁")

STT = """
📣 **LOG ALERT** 📣

📛**Triggered Command** : /settings
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @Musicx_dlbot

#settings
"""

SPO = """
📣 **LOG ALERT** 📣

📛**Triggered Command** : /Spotify 
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @Musicx_dlbot

#spotify
"""
#@Mbot.on_message(filters.regex("@Musicx_dlbot"x))
#async def spin(bot, message):
#    text = "🔎 Please Select The Type Of The Search:"
#    spotbutton = InlineKeyboardMarkup(
#        [
#            [
#                InlineKeyboardButton("🎧Track", switch_inline_query_current_chat="st "),
#                InlineKeyboardButton("💽Album",  switch_inline_query_current_chat="sa "),
#                InlineKeyboardButton("🗣️Artist",  switch_inline_query_current_chat="ar "),
#                InlineKeyboardButton("💿Playlist",  switch_inline_query_current_chat="sp ")
#            ],[
#                InlineKeyboardButton("❌", callback_data="close")
#            ]
#        ]
#    )
#    msd = await message.reply_photo(
#        photo="https://te.legra.ph/file/36fa349d4092f1bdcdaa9.jpg", 
#        caption=text, 
#        reply_markup=spotbutton,
#    )
#    await message.react(choice(Telegram.EMOJIS))
#    await msd.react(choice(Telegram.EMOJIS))


#filters.regex("@Musicx_dlbot") | 
@Mbot.on_message(filters.command("spotify", CMD) & pyro_cooldown.wait(10))
async def spotify(bot, message):
    text = "Spotify :"
    spotbutton = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Spotify ⤵️", callback_data="spw")
            ],[
                InlineKeyboardButton("🎧Track", switch_inline_query_current_chat="st "),
                InlineKeyboardButton("💽Album",  switch_inline_query_current_chat="sa "),
                InlineKeyboardButton("🗣️Artist",  switch_inline_query_current_chat="ar "),
                InlineKeyboardButton("💿Playlist",  switch_inline_query_current_chat="sp ")
            ],[
                InlineKeyboardButton("❌", callback_data="close")
            ]
        ]
    )
    await bot.send_message(LOG_CHANNEL, SPO.format(message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
    sps = await message.reply_photo(
        photo=random.choice(SPY), 
        caption=text, 
        reply_markup=spotbutton,
    )
    
    await message.react(choice(Telegram.EMOJIS))
    await sps.react(choice(Telegram.EMOJIS))

#=======================÷÷÷÷===÷÷÷÷÷÷÷÷÷
@Mbot.on_message(filters.command("settings", CMD) & pyro_cooldown.wait(10))
async def settig_cmd(bot, message):
    caption = "Choose:"
    settigButton = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Spotify ⤵️", callback_data="spw")
            ],[
                InlineKeyboardButton("Search Track 🎧", switch_inline_query_current_chat="st "),
                InlineKeyboardButton("Search Album 💽",  switch_inline_query_current_chat="sa ")
            ],[
                InlineKeyboardButton("Search Playlist 🗂️",  switch_inline_query_current_chat="sp "),
                InlineKeyboardButton("Search Artist 🗣️",  switch_inline_query_current_chat="ar ")
            ],[
                InlineKeyboardButton("Spotify🟢", callback_data="inlsp"),
                InlineKeyboardButton("YouTube", callback_data="inlyt"),
                InlineKeyboardButton("Deezer", callback_data="inldz")
            ],[
                InlineKeyboardButton("❌", callback_data="close")
            ]
        ]
    )
    await bot.send_message(LOG_CHANNEL, STT.format(message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
    stt = await message.reply_text(caption, reply_markup=settigButton)
    await message.react(choice(Telegram.EMOJIS))
    await stt.react(choice(Telegram.EMOJIS))

INSP_TEXT = """
Choose:
"""
INSP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Spotify ⤵️", callback_data="spw")
        ],[
        InlineKeyboardButton("Search Track 🎧", switch_inline_query_current_chat="st "),
        InlineKeyboardButton("Search Album 💽",  switch_inline_query_current_chat="sa ")
        ],[
        InlineKeyboardButton("Search Playlist 🗂️",  switch_inline_query_current_chat="sp "),
        InlineKeyboardButton("Search Artist 🗣️",  switch_inline_query_current_chat="ar ")
        ],[
        InlineKeyboardButton("Spotify🟢", callback_data="inlsp"),
        InlineKeyboardButton("YouTube", callback_data="inlyt"),
        InlineKeyboardButton("Deezer", callback_data="inldz")
        ],[
        InlineKeyboardButton("❌", callback_data="close")
        ]]
    )
INDZ_TEXT = """
Choose:
"""
INDZ_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Deezer ⤵️", callback_data="dzw")
        ],[
        InlineKeyboardButton("Search Track 🎧", switch_inline_query_current_chat="dt "),
        InlineKeyboardButton("Search Album 💽", switch_inline_query_current_chat="da ")
        ],[
        InlineKeyboardButton("Search Playlist 🗂️", switch_inline_query_current_chat="dp "),
        InlineKeyboardButton("Search Artist 🗣️", switch_inline_query_current_chat="dr ")
        ],[
        InlineKeyboardButton("Spotify", callback_data="inlsp"),
        InlineKeyboardButton("YouTube", callback_data="inlyt"),
        InlineKeyboardButton("Deezer🟣", callback_data="inldz")
        ],[
        InlineKeyboardButton("❌", callback_data="close")
        ]]
    )
INYT_TEXT = """
Choose:
"""
INYT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("YouTube ⤵️",  callback_data="ytw")
        ],[
        InlineKeyboardButton("YouTube Search 🔎",  switch_inline_query_current_chat="yt "),
        InlineKeyboardButton("YouTube Playlist 🗂️",  callback_data="soon")
        ],[
        InlineKeyboardButton("Spotify", callback_data="inlsp"),
        InlineKeyboardButton("YouTube🔴", callback_data="inlyt"),
        InlineKeyboardButton("Deezer", callback_data="inldz")
        ],[
        InlineKeyboardButton("❌", callback_data="close")
        ]]
    )
#======================={{==≠=====

captions = """
hi {}
"""

MS = """
📣 **LOG ALERT** 📣

📛**Triggered Command** : /start, /m_start
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @Musicx_dlbot
"""

@Mbot.on_message(filters.private)
async def _(bot, cmd):
    await handle_user_status(bot, cmd)
@Mbot.on_message(filters.private & filters.command("start", CMD) & pyro_cooldown.wait(10))
async def start_command(bot, message): 
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await client.get_me()
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"🥳NEWUSER🥳 \n\n😼New User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) 😹started @spotifysavetgbot !!",
            )
        else:
            logging.info(f"🥳NewUser🥳 :- 😼Name : {message.from_user.first_name} 😹ID : {message.from_user.id}")
    #await message.react(choice(Telegram.EMOJIS))
    await bot.send_message(LOG_CHANNEL, MS.format(message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
    rac = await message.reply_photo(
        photo=random.choice(PICS), 
        caption=start_cmd.format(message.from_user.first_name), 
        reply_markup=startbt,
    )
    await message.delete()
    await rac.react(choice(Telegram.EMOJIS))
    #output_text = Disclaimer + str2 + Thanks
    #chat_id = message.chat.id
    #language = 'en-uk'
    #tts_file = gTTS(text=output_text, lang=language, slow=False) 
    #tts_file.save(f"{message.chat.id}.mp3")
    #with open(f"{message.chat.id}.mp3", "rb") as speech:
        #vc = await bot.send_voice(chat_id, speech, caption="🎤 Voice message from: @Musicx_dlbot.")
    #ab = await message.reply_text(ms_stt)
    a = await message.reply_sticker(stickers_ran)
    await asyncio.sleep(50)
    #await vc.delete()
    await a.delete()
    raise StopPropagation


#=======CALLBACK==================
@Mbot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "start":
        await update.message.edit_text(
            text=start_cmd.format(update.from_user.first_name), #update.from_user.first_name
            reply_markup=startbt,
            disable_web_page_preview=True
        )
        await update.answer("👋Hey i am 𝗠ᴜsɪᴄ•𝕏•𝗗ʟ 🎧")
        
    elif update.data == "cmds":
        await update.message.edit_text(
            text=CMDS_TEXT.format(update.from_user.first_name),
            reply_markup=CMDS_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("👋Hey i am 𝗠ᴜsɪᴄ•𝕏•𝗗ʟ 🎧")
#====================
    elif update.data == "inlsp":
        await update.message.edit_text(
            text=INSP_TEXT,
            reply_markup=INSP_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Search Spotify 🔎")
    elif update.data == "inldz":
        await update.message.edit_text(
            text=INDZ_TEXT,
            reply_markup=INDZ_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Search Deezer 🔎")
    elif update.data == "inlyt":
        await update.message.edit_text(
            text=INYT_TEXT,
            reply_markup=INYT_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Search YouTube 🔎")
  #====================
    elif update.data == "mc":
        await update.message.edit_text(
            text=MC_TEXT,
            reply_markup=MC_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To Music Dl 🎵")
    
    elif update.data == "yt":
        await update.message.edit_text(
            text=YOUTUB_TEXT,
            reply_markup=YOUTUB_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To YouTube Music 🎵")
        
    elif update.data == "sp":
        await update.message.edit_text(
            text=SPOTY_TEXT,
            reply_markup=SPOTY_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To Spotify Music 🎵")
        
    elif update.data == "dz":
        await update.message.edit_text(
            text=DEEZER_TEXT,
            reply_markup=DEEZER_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To Deezer Music 🎵")
        
    elif update.data == "sv":
        await update.message.edit_text(
            text=SAAVN_TEXT,
            reply_markup=SAAVN_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To Saavn Music 🎵")
        
    elif update.data == "sc":
        await update.message.edit_text(
            text=SOUNDC_TEXT,
            reply_markup=SOUNDC_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To SoundCloud Music 🎵")
        
    elif update.data == "mx":
        await update.message.edit_text(
            text=MIXC_TEXT,
            reply_markup=MIXC_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To MixCloud Music 🎵")
        
    elif update.data == "lg":
        await update.message.edit_text(
            text=LOGC_TEXT,
            reply_markup=LOGC_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "wba":
        await update.message.edit(
            text=WBA_TEXT,
            reply_markup=WBA_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To Web Stream.📱")
            
    elif update.data == "ig":
        await update.message.edit_text(
            text=IGDL_TEXT,
            reply_markup=IGDL_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To Instagram Download 📱")
    elif update.data == "tt":
        await update.message.edit_text(
            text=TTDL_TEXT,
            reply_markup=TTDL_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To TikTok Download 👻")
    elif update.data == "pt":
        await update.message.edit_text(
            text=PTDL_TEXT,
            reply_markup=PTDL_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To Pinterest Download 🏞️")
    elif update.data == "ly":
        await update.message.edit_text(
            text=LY_TEXT,
            reply_markup=LY_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("Wc To Lyrics 📝🎶")
        
    elif update.data == "ex": 
        await update.message.edit_text(
            text=EX_TEXT,
            reply_markup=EX_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("More... 😋")

    elif update.data == "shr": 
        await update.message.edit_text(
            text=SHR_TEXT,
            reply_markup=SHR_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("✈️ Share with Your friends")
        
    elif update.data == "nxt":
        await update.message.edit_text(
            text=EX2_TEXT,
            reply_markup=EX2_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "shz":
        await update.message.edit_text(
            text=SHZ_TEXT,
            reply_markup=SHZ_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("🔎 Shazam Recognising")
    elif update.data == "own":
        await update.message.edit_text(
            text=OWN_TEXT,
            reply_markup=OWN_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("👋 Hoi")
            
            
#========
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
        await update.answer("My About ℹ️")
        
    elif update.data == "close":
        await update.message.delete()
        await update.answer("Successfully Closed ❌")
        
    elif update.data == "exa":
        await update.answer("More music Request:\n➻ You can download songs by sending the Youtube, Spotify, SoundCloud, Deezer links to the group. It helps to get the proper song.\nThank you, I hope you understand. 😊", show_alert=True)

    elif update.data == "emt":
        await update.answer("Why, its empty 😹")
    elif update.data == "hmm":
        await update.answer("😌")
    elif update.data == "spw":
        await update.answer("🟢🟢⟨‹SPOTIFY›⟩🟢🟢")
    elif update.data == "dzw":
        await update.answer("🟣🟣⟨‹DEEZER›⟩🟣🟣")
    elif update.data == "ytw":
        await update.answer("🔴🔴⟨‹YOUTUBE›⟩🔴🔴")
    elif update.data == "done":
        await update.answer("Your Music has been successfully Uploaded.✅\nThank you for using me💖", show_alert=True) 
    elif update.data == "soon":
        await update.answer("Soon...", show_alert=True) 

    #else:
        #await update.message.delete()
#=========CALLBACK========

CMDS_TEXT = """
__Hello {}
I'm here to download your music's 🎵 and more thing's...__

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
CMDS_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('▶️ Web Play', callback_data="wba"),
        ],[
        InlineKeyboardButton("🎵 Deezer", callback_data="dz"),
        InlineKeyboardButton("🎵 Spotify", callback_data="sp")
        ],[
        InlineKeyboardButton("🎵 YouTube", callback_data="yt"),
        InlineKeyboardButton("🎵 SoundCloud", callback_data="sc")
        ],[
        InlineKeyboardButton("📝 Lyrics", callback_data="ly"),
        InlineKeyboardButton("♬ Music×Dl", callback_data="mc")
        ],[
        InlineKeyboardButton("🪬 Shazam", callback_data="shz"),
        InlineKeyboardButton("➕ More...", callback_data="ex")
        ],[
        InlineKeyboardButton("⬅️", callback_data="start"),
        InlineKeyboardButton("ㅤㅤㅤㅤ", callback_data="emt"),
        InlineKeyboardButton("❌", callback_data="close")
        ]]
    )
#=============Bottons==========
SHR_TEXT = """
❤️ __Invite Your Friends To Start This Bot.__

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
SHR_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("📨 Telegram", url="https://t.me/share/url?url=Check+Out+@musicx_dlbot%2C+The+Telegram+Music+Bot+That+Lets+You+Search%2C+Listen+And+Download+Tens+Of+Millions+Of+Tracks+And+Albums+From+Your+Favourite+Artists%2C+In+A+Few+Seconds.++https://t.me/musicx_dlbot"),
        InlineKeyboardButton("📨 Twitter", url="http://twitter.com/share?text=Check+Out+MusicXdl%2C+The+Telegram+Bot+That+Lets+You+Search%2C+Listen+And+Download+Tens+Of+Millions+Of+Tracks+And+Albums+From+Your+Favourite+Artists%2C+In+A+Few+Seconds.&url=https://t.me/musicx_dlbot")
        ],[
        InlineKeyboardButton("📨 WhatsApp", url="https://api.whatsapp.com/send?phone=&text=Check+Out+MusicXdlbot%2C+The+Telegram+Bot+That+Lets+You+Search%2C+Listen+And+Download+Tens+Of+Millions+Of+Tracks+And+Albums+From+Your+Favourite+Artists%2C+In+A+Few+Seconds.+https://t.me/musicx_dlbot"), 
        InlineKeyboardButton("📨 Facebook", url="https://www.facebook.com/sharer/sharer.php?u=https://t.me/musicx_dlbot")
        ],[
        InlineKeyboardButton("⬅️", callback_data="start"),
        InlineKeyboardButton("ㅤㅤㅤㅤ", callback_data="emt"),
        InlineKeyboardButton("❌", callback_data="close")
        ]]
    ) 

LY_TEXT = """
**Genius Lyrics**

__I Can Find Any Song Lyrics, To Search Using Commands Mode. You Can Even Search By Lyrics__

**Examples:**
  × `/lyrics beggin`
  × `/lyrics hope alen walker`
  × `/lyrics` [artist_name + song_name]

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
LY_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("⬅️", callback_data="cmds"), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("🏠", callback_data="start")
        ]]
    ) 

MC_TEXT = """
**Help for Music downloads**

__just Send me song name with `/mp3` `/song` comments To download Music 🎶...
and I'll send you song on Telegram__

Examples:
  × `/song hope`
  × `/mp3 hope`

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
MC_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("⬅️", callback_data="cmds"),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("🏠", callback_data="start")
        ]]
    ) 

SHZ_TEXT = """
__Start This [**@Shazam_Xrobot**] bot to recognize a song from voice message, 
video or Audio files and give you info about the song. 
You can either  download it directly or stream it on Spotify, Youtube, Instagram and More...__

Or you can us this command here `/shazam` 
`/shazam` reply to Audio / video to Recognise Which Music is that🎵

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
SHZ_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Shazam Web', 
                url="http://t.me/Musicx_dlbot/webshaaz"
                )
        ],[
        InlineKeyboardButton('⬅️', callback_data='cmds'), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
)

YOUTUB_TEXT = """
**Help for YouTube & YouTube Music Dl**

__Send **Youtube** Link in Chat to Download Music |Or `/vsong` Then [song_name | Yt_link] to download **Video & Audio** in defferent Qualitys.
Also you can search music from YouTube in my Inline search query 🔽.__

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
YOUTUB_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Inline Buttons ⤵️", callback_data="ytw")
        ],[
        InlineKeyboardButton("YouTube Search 🔎",  switch_inline_query_current_chat="yt "),
        InlineKeyboardButton("YouTube Playlist 🗂️",  callback_data="soon")
        ],[
        InlineKeyboardButton("⬅️", callback_data="cmds"), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton("🏠", callback_data="start")
        ]]
    ) 

SPOTY_TEXT = """
**Help for Spotify Music Dl**

__Send **Spotify** Track/Playlist/Album Link. I'll Download It For You.
Only 100 playlist can download from Spotify.
Or you can search `Tracks, Album, Playlist, Artist` from Spotify in my Inline search query 🔽.__

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
SPOTY_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Inline Buttons ⤵️", callback_data="spw")
        ],[
        InlineKeyboardButton("Search Track 🎧", switch_inline_query_current_chat="st "),
        InlineKeyboardButton("Search Album 💽",  switch_inline_query_current_chat="sa ")
        ],[
        InlineKeyboardButton("Search Playlist 🗂️",  switch_inline_query_current_chat="sp "),
        InlineKeyboardButton("Search Artist 🗣️",  switch_inline_query_current_chat="ar ")
        ],[
        InlineKeyboardButton('⬅️', callback_data='cmds'), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
    )

DEEZER_TEXT = """
**Help for Deezer Music Dl**

__Send Deezer Playlist/Album/Track Link. I'll Download It For You.
Or you can search Tracks, Albums, Playlists and Artist from Deezer in my Inline search query 🔽.__

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
DEEZER_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Inline Buttons ⤵️", callback_data="dzw")
        ],[
        InlineKeyboardButton("Search Track 🎧", switch_inline_query_current_chat="dt "),
        InlineKeyboardButton("Search Album 💽", switch_inline_query_current_chat="da ")
        ],[
        InlineKeyboardButton("Search Playlist 🗂️", switch_inline_query_current_chat="dp "),
        InlineKeyboardButton("Search Artist 🗣️", switch_inline_query_current_chat="dr ")
        ],[
        InlineKeyboardButton('⬅️', callback_data='cmds'), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
    )

SAAVN_TEXT = """
**Help for Saavn Music Dl**

__Send /saavn [song name] - To download song from Saavn.**

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
SAAVN_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⬅️', callback_data='cmds'), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
    )

SOUNDC_TEXT = """
**Help for SoundCloud Music Dl**

__Send **Sound Cloud** Track Link. I'll Download It For You. 
**Example:** `https://soundcloud.com/djalvaro/aya-nakamura-djadja-alvaro-x-trobi-rmx?si=8fc58b6906d14a629d77db2b4dc80e9b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing`

If you not work above example, ok you can send link like this🔽
**Example 2**: `https://soundcloud.com/soavedusk/take-it-easy`__

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
SOUNDC_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⬅️', callback_data='cmds'), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
    )

MIXC_TEXT = """
**Help for MixCloud Music Dl**

__Send **Mix Cloud** Track Link. I'll Download It For You.__

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
MIXC_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⬅️', callback_data='cmds'), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
    )

#=====================================
ytl = "https://t.me/Musicx_dlbot/Webytm"
WBA_TEXT = """
__Stream Music Using Web Music Player 📱🎺__
"""
WBA_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Spotify',
                url="https://t.me/Musicx_dlbot/webspoti"
            ),
               
            InlineKeyboardButton('Sound Cloud',
                url="https://t.me/Musicx_dlbot/websoundc"
            )
            
        ],[
            InlineKeyboardButton('Wynk', 
                url="https://t.me/Musicx_dlbot/webwynk"
                ),
               
            InlineKeyboardButton('Saavn', 
                url="https://t.me/Musicx_dlbot/webSaavn"
                )
            
        ],[
            InlineKeyboardButton('Apple Music', 
                url="https://t.me/Musicx_dlbot/webAppleM"
                ),
               
            InlineKeyboardButton('YouTube Music',
                url=f"{ytl}"
                )
        ],[
            InlineKeyboardButton('Amezon Music', 
                url="https://t.me/Musicx_dlbot/webamazon"
                ),
               
            InlineKeyboardButton('Gaana Music',
                url="https://t.me/Musicx_dlbot/webgaana"
                )
        ],[
            InlineKeyboardButton('⬅️', callback_data='cmds'),
            InlineKeyboardButton("❌", callback_data="close"),
            InlineKeyboardButton('🏠', callback_data='start')
        ]]
    )
#web_app=WebAppInfo(
#reward_info_Keyboard = InlineKeyboardMarkup(
#                [[
#                    InlineKeyboardButton('LAUNCh WEBAPP', web_app=WebAppInfo(url="YOUR_URL")),
#                ]]
#)
IGDL_TEXT = """
Help for **Instagram** Posts/Reels/Photos download,

Send `/igdl` then your Instagram video link
eg: `/igdl` [link]
"""
IGDL_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⬅️', callback_data='ex'), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
) 
TTDL_TEXT = """
Help for **TikTok** Reels download,

Send `/ttdl` then your Tiktok video link
eg: `/ttdl` [link]
"""
TTDL_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⬅️', callback_data='ex'), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
)

#==================={{={{{{{===

LOGC_TEXT = """
**Log channel**

My Music Database @music_database_tg
"""
LOGC_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⬅️', callback_data='cmds'), 
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
    )

EX_TEXT = """
**Here is the list for more commands.**


__× `/ping` `/alive` - Use to ping me whenever i am dead or not. 
╭× `/id` `/info` `/stickerid` `/dc` - Use to get information about you.
╰× Forward me any message from any user/bot/channel or anonymous admins to get ID.
× `/yt_search` - search a YouTube Videos gives 10 results.
× `/spotify_tracks` - search a Spotify Tracks gives 10 results.
× `/spotify_album` -search a Spotify Album gives 10 results.
× `/spotify_playlist` - search a Spotify Playlist gives 10 results.
× `/spotify_artist` - search a Spotify Artists gives 10 results.
× `/thumbdl` - Download Thumbnail from Spotify, Deezer, Soundcloud, YouTube, Saavn platforms and more..
× `/saavn` [song name] - To download song from Saavn. 
× `/deezer_tracks` - Search A Deezer Tracks gives 10 results.

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
#× `/pvdl` - then your Pinterest 📹video link.
#× `/pidl` - then your Pinterest 🖼️Image link.
EX_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("🧑‍🔧 Only for my Owner", callback_data="own")
        ],[
        InlineKeyboardButton('⬅️', callback_data='cmds'),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
    )

OWN_TEXT = """
**🔺This only for my Owner🔻**

× `/restart`
× `/log`
× `/stats`
× `/broadcast`
× `/ban_user`
× `/unban_user`
× `/banned_users`
× `/leave`
× `/send`

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
OWN_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⬅️', callback_data='ex'),
        InlineKeyboardButton("❌", callback_data="close"),
        InlineKeyboardButton('🏠', callback_data='start')
        ]]
)


#=================
ABOUT_TEXT = """
__About Me__
 
🤖 **Name** : [𝗠ᴜsɪᴄ•𝕏•𝗗ʟ](https://t.me/Musicx_dlbot)

🎯 **Bot Version** : `2.0.23`

🧔🏼 **My Father** : [Bot Father](https://t.me/BotFather)

📝 **Language** : [Python3](https://python.org)
╰─×  **Python version** : `3.10.11`

📚 **Library** : [Pyrogram](https://pyrogram.org)
╰─× **Pyrogram version** : `2.0.28`

📡 **Hosted On** : [Digital Ocean 🌊](https://www.digitalocean.com)

🗄 **Database** : [MongoDB Local](https://mongodb.com)

✴️ **Base Docker** : Debian 12

📋 **License** : [MIT](https://choosealicense.com/licenses/mit/)

<blockquote>©️ @Musicx_dlbot</blockquote>
"""
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⬅️', callback_data='start'),
        InlineKeyboardButton('🌐 Source Code', url='https://github.com/rozari0/NeedMusicRobot')
        ],[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )

#==================•BROADCAST•==================
@Mbot.on_message(filters.private & filters.command("broadcast", CMD))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.delete()
    else:
        await broadcast(m, db)

@Mbot.on_message(filters.private & filters.command("stats", CMD))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    sat = await m.reply_text(
        text=f"**Total Users in Database 📂:** `{await db.total_users_count()}`\n\n**Total Users with Notification Enabled 🔔 :** `{await db.total_notif_users_count()}`",
        quote=True
    )
    await m.delete()
    await asyncio.sleep(180)
    await sat.delete()

@Mbot.on_message(filters.private & filters.command("ban_user", CMD))
async def ban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban 🛑 any user from the bot 🤖.\n\nUsage:\n\n`/ban_user user_id ban_duration ban_reason`\n\nEg: `/ban_user 1234567 28 You misused me.`\n This will ban user with id `1234567` for `28` days for the reason `You misused me`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = " ".join(m.command[3:])
        ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."

        try:
            await c.send_message(
                user_id,
                f"You are Banned 🚫 to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin 🤠**",
            )
            ban_log_text += "\n\nUser notified successfully!"
        except BaseException:
            traceback.print_exc()
            ban_log_text += (
                f"\n\n ⚠️ User notification failed! ⚠️ \n\n`{traceback.format_exc()}`"
            )
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(ban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )

@Mbot.on_message(filters.private & filters.command("unban_user", CMD))
async def unban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to unban 😃 any user.\n\nUsage:\n\n`/unban_user user_id`\n\nEg: `/unban_user 1234567`\n This will unban user with id `1234567`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user 🤪 {user_id}"

        try:
            await c.send_message(user_id, f"Your ban was lifted!")
            unban_log_text += "\n\n✅ User notified successfully! ✅"
        except BaseException:
            traceback.print_exc()
            unban_log_text += (
                f"\n\n⚠️ User notification failed! ⚠️\n\n`{traceback.format_exc()}`"
            )
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(unban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"⚠️ Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True,
        )

@Mbot.on_message(filters.private & filters.command("banned_users", CMD))
async def banned_usrs(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += f"🆔**User_id** : `{user_id}`\n⏱️**Ban Duration** : `{ban_duration}`\n\n📆**Banned on** : `{banned_on}`\n\n💁**Reason**: `{ban_reason}`\n\n😌 @Musicx_dlbot"
    reply_text = f"Total banned user(s) 🤭: `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open("banned-users.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-users.txt", True)
        os.remove("banned-users.txt")
        return
    await m.reply_text(reply_text, True)
