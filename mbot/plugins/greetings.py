import os
from mbot import Mbot
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


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
    await message.reply_text(
        caption=start_cmd.format(message.from_user.first_name), 
        reply_markup=startbt,
    )
    await message.delete()
