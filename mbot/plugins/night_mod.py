import random 
from pyrogram import filters,Client,enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions

from mbot import Mbot as app
from mbot.utils.Database.nightmodedb import nightdb,nightmode_on,nightmode_off,get_nightchats 



CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages = False,
    can_send_other_messages = False,
    can_send_polls = False,
    can_change_info = False,
    can_add_web_page_previews = False,
    can_pin_messages = False,
    can_invite_users = False )


OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages = True,
    can_send_other_messages = True,
    can_send_polls = True,
    can_change_info = True,
    can_add_web_page_previews = True,
    can_pin_messages = True,
    can_invite_users = True )
    
buttons = InlineKeyboardMarkup([[InlineKeyboardButton("🟢ENABLE🟢", callback_data="add_night"),InlineKeyboardButton("🔴DISABLE🔴", callback_data="rm_night")]])         
@app.on_message(filters.command("nightmod") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg", caption="🌅__Click on the below button to Enable | Disable Night Mode in this Chat.__🌌",reply_markup=buttons)
              
     
@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query : CallbackQuery):
    data = query.data 
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id" : chat_id})
    administrators = []
    if data == "add_night":
        if check_night:        
            await query.message.edit_caption("__Night Mod is already enable in this chat__")
        elif not check_night:
            await nightmode_on(chat_id)
            await query.message.edit_caption("__Added to my Database. This group will be closed on 12Am [IST] and will opened on 06Am [IST] .__") 
    if data == "rm_night":
        if check_night:  
            await nightmode_off(chat_id)      
            await query.message.edit_caption("__Night Mod is removed from my database.__")
        elif not check_night:
            await query.message.edit_caption("__Night Mod is already disable in this chat__") 
            
async def start_nightmode() :
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for add_chat in chats:
        try:
            await app.send_photo(
                add_chat,
                photo="https://telegra.ph/file/439776047f545a22fa817.jpg",
                caption= f"__Group is closing! Good night 🥱😴🌌__")
            
            await app.set_chat_permissions(add_chat,CLOSE_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To close Group {add_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59) #hour=23, minute=59
scheduler.start()

async def close_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for rm_chat in chats:
        try:
            await app.send_photo(
                rm_chat,
                photo="https://telegra.ph/file/e1ecea4a99b1a0d45d1d8.jpg",
                caption= f"__Group is Opened Now Avery one can message again 😊! Good morning 🌞 🌄__")
            
            await app.set_chat_permissions(rm_chat,OPEN_CHAT)

        except Exception as e:
            print(f"[bold red] Unable To open Group {rm_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1) #hour=6, minute=1
scheduler.start()
