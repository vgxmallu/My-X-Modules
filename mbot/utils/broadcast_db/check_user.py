import datetime
from config import DB_URL, DB_NAME, LOG_CHANNEL
import logging
from mbot.utils.broadcast_db.database import Database

db = Database(DB_URL, DB_NAME)
async def handle_user_status(bot, cmd):
    chat_id = cmd.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await bot.send_message(
                LOG_CHANNEL,
                f"🆕**×NEW•🈲•USER×**🆕\n\n⬇️**User Info:**\n\n👤 **New User:** [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\n🔄 **User Name**: @{cmd.from_user.username}\n🆔 **User ID:** `{cmd.from_user.id}`\n🤖 **Started bot:** @{BOT_USERNAME}!!",
            )
        else:
            logging.info(f"😹NewUser🥳 :- Name : {cmd.from_user.first_name} ID : {cmd.from_user.id}")
    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (
            datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text("Your Banned from This BOT❗", quote=True) #You are Banned to Use This Bot 
            return
    await cmd.continue_propagation()
