from pyrogram import filters
from pymongo import MongoClient
from mbot import Mbot as app
from config import DB_URL
from pyrogram.types import *
from pyrogram.errors import MessageNotModified
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import InputMediaPhoto
from typing import Union

import asyncio
import random
from pyrogram import Client, filters
import requests
import os
import time 
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message



mongo_client = MongoClient(DB_URL)
db = mongo_client["natu_rankings"]
collection = db["ranking"]

user_data = {}

today = {}

MISHI = [
    "https://telegra.ph/file/059611caea9ef749feb5d.jpg",
    "https://telegra.ph/file/b198b080d7a6408ff340b.jpg",
    "https://telegra.ph/file/b5b64413f6235e4beaafe.jpg",
    "https://telegra.ph/file/0e6924b678e0e92a62370.jpg",
    "https://telegra.ph/file/91e4f4082c61318f9eb67.jpg",
    "https://telegra.ph/file/22c20f5256dea9006111a.jpg",
    "https://telegra.ph/file/f333abc3500868b56cc99.jpg",
    "https://telegra.ph/file/890802c4d2ac2c6a0a8af.jpg"
    "https://telegra.ph/file/f60186ce2c83dc5c98948.jpg",
    "https://telegra.ph/file/16f957e795a6d3e35a87c.jpg",
    "https://telegra.ph/file/2348c377ed47034ab38a8.jpg",
    "https://telegra.ph/file/2720c796a1a27eb018e3d.jpg",
    "https://telegra.ph/file/d7d665e0785f2681ca35b.jpg",
    "https://telegra.ph/file/e1f5f90c52cd2e568f699.jpg",
]


#watcher

@app.on_message(filters.group & filters.group, group=6)
def today_watcher(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_id in today and user_id in today[chat_id]:
        today[chat_id][user_id]["total_messages"] += 1
    else:
        if chat_id not in today:
            today[chat_id] = {}
        if user_id not in today[chat_id]:
            today[chat_id][user_id] = {"total_messages": 1}
        else:
            today[chat_id][user_id]["total_messages"] = 1


@app.on_message(filters.group & filters.group, group=11)
def _watcher(_, message):
    user_id = message.from_user.id    
    user_data.setdefault(user_id, {}).setdefault("total_messages", 0)
    user_data[user_id]["total_messages"] += 1    
    collection.update_one({"_id": user_id}, {"$inc": {"total_messages": 1}}, upsert=True)


# ------------------- ranks ------------------ #

@app.on_message(filters.command("today"))
async def today_(bot, message):
    chat_id = message.chat.id
    if chat_id in today:
        users_data = [(user_id, user_data["total_messages"]) for user_id, user_data in today[chat_id].items()]
        sorted_users_data = sorted(users_data, key=lambda x: x[1], reverse=True)[:10]

        if sorted_users_data:
            response = "**✦ 📈 ᴛᴏᴅᴀʏ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ**\n\n"
            for idx, (user_id, total_messages) in enumerate(sorted_users_data, start=1):
                try:
                    user_name = (await bot.get_users(user_id)).first_name
                except:
                    user_name = "Unknown"
                user_info = f"**{idx}**.   {user_name} ➠ {total_messages}\n"
                response += user_info
            button = InlineKeyboardMarkup(
                [[    
                   InlineKeyboardButton("ᴏᴠᴇʀᴀʟʟ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ", callback_data="overall"),
                ]])
            await message.reply_photo(random.choice(MISHI), caption=response, reply_markup=button)
        else:
            await message.reply_text("❅ ɴᴏ ᴅᴀᴛᴀ ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛᴏᴅᴀʏ.")
    else:
        await message.reply_text("❅ ɴᴏ ᴅᴀᴛᴀ ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛᴏᴅᴀʏ.")



@app.on_message(filters.command("ranking"))
async def ranking(bot, message):
    top_members = collection.find().sort("total_messages", -1).limit(10)

    response = "**✦ 📈 ᴄᴜʀʀᴇɴᴛ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ**\n\n"
    for idx, member in enumerate(top_members, start=1):
        user_id = member["_id"]
        total_messages = member["total_messages"]
        try:
            user_name = (await bot.get_users(user_id)).first_name
        except:
            user_name = "Unknown"

        user_info = f"**{idx}**.   {user_name} ➠ {total_messages}\n"
        response += user_info 
    button = InlineKeyboardMarkup(
            [[    
               InlineKeyboardButton("ᴛᴏᴅᴀʏ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ", callback_data="today"),
            ]])
    await message.reply_photo(random.choice(MISHI), caption=response, reply_markup=button)



# -------------------- regex -------------------- # 

@app.on_callback_query(filters.regex("today"))
async def today_rank(bot, query):
    chat_id = query.message.chat.id
    if chat_id in today:
        users_data = [(user_id, user_data["total_messages"]) for user_id, user_data in today[chat_id].items()]
        sorted_users_data = sorted(users_data, key=lambda x: x[1], reverse=True)[:10]

        if sorted_users_data:
            response = "**✦ 📈 ᴛᴏᴅᴀʏ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ**\n\n"
            for idx, (user_id, total_messages) in enumerate(sorted_users_data, start=1):
                try:
                    user_name = (await bot.get_users(user_id)).first_name
                except:
                    user_name = "Unknown"
                user_info = f"**{idx}**.   {user_name} ➠ {total_messages}\n"
                response += user_info
            button = InlineKeyboardMarkup(
                [[    
                   InlineKeyboardButton("ᴏᴠᴇʀᴀʟʟ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ", callback_data="overall"),
                ]])
            await query.message.edit_text(response, reply_markup=button)
        else:
            await query.answer("❅ ɴᴏ ᴅᴀᴛᴀ ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛᴏᴅᴀʏ.")
    else:
        await query.answer("❅ ɴᴏ ᴅᴀᴛᴀ ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛᴏᴅᴀʏ.")



@app.on_callback_query(filters.regex("overall"))
async def overall_rank(bot, query):
    top_members = collection.find().sort("total_messages", -1).limit(10)

    response = "**✦ 📈 ᴏᴠᴇʀᴀʟʟ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ**\n\n"
    for idx, member in enumerate(top_members, start=1):
        user_id = member["_id"]
        total_messages = member["total_messages"]
        try:
            user_name = (await bot.get_users(user_id)).first_name
        except:
            user_name = "Unknown"

        user_info = f"**{idx}**.   {user_name} ➠ {total_messages}\n"
        response += user_info 
    button = InlineKeyboardMarkup(
            [[    
               InlineKeyboardButton("ᴛᴏᴅᴀʏ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ", callback_data="today"),
            ]])
    await query.message.edit_text(response, reply_markup=button)
