import os
from mbot import Mbot
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


from config import LOG_CHANNEL, AUTH_USERS, DB_URL, DB_NAME
from handlers.database import Database


db = Database(DB_URL, DB_NAME)

start_cmd = """
Hello {} Welcome to Gojo Satoru 𝕏 Bot
"""
startbt = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('📣 My Channel', url='https://t.me/XBots_X')
            ]
        ]
)


@Mbot.on_message(filters.private & filters.command(["start", "help"]))
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
    await message.reply_text(
        text=start_cmd.format(message.from_user.first_name), 
        reply_markup=startbt,
    )
    await message.delete()
