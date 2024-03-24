import os
import asyncio
import base64
import os
from urllib.parse import quote

import requests
from pyrogram import Client
from pyrogram import filters


#
def carbon(code):
    url = f"https://api.safone.dev/carbon?code={quote(code)}"
    resp = requests.get(url)
    js = resp.json()["image"]
    return js


@Client.on_message(filters.command(["carbon"]))
async def make_carbon(bot, message):
    async def car_(bot, message):
        ok = await message.reply_text("__Making Carbon...__")
        try:
            code = None
            if message.reply_to_message:
                if message.reply_to_message.caption:
                    code = message.reply_to_message
                elif message.reply_to_message.text:
                    code = message.reply_to_message.text
            elif len(message.command) > 1:
                code = message.text.split(" ", 1)[1]

            if not code:
                return await ok.edit("__Nothing To Carbonize...__")

            x = carbon(code)
            decodeit = open('carbon.jpg', 'wb')
            decodeit.write(base64.b64decode(str(x)))
            decodeit.close()
            if message.from_user:
                user = message.from_user.mention
            else:
                user = message.sender_chat.title
            cap = f"__Carbonized By {user}__\n\n__By @GojoSatoru_Xbot | @Xbots_X__"
            await message.reply_document("carbon.jpg", caption=cap)
            await ok.delete()
            os.remove("carbon.jpg")
        except Exception as e:
            raise e
    try:
        await asyncio.wait_for(car_(bot, message), timeout=60)
    except asyncio.TimeoutError:
        return await message.reply_text("__Timeout Exceeded. Carbonization process took too long__")


@Client.on_message(filters.command(["icarbon"]))
async def carbonn(bot, message):
    ok = await message.reply_text("__Making Carbon...__")
    code = None
    if message.reply_to_message:
        if message.reply_to_message.caption:
            code = message.reply_to_message
        elif message.reply_to_message.text:
            code = message.reply_to_message.text
    elif len(message.command) > 1:
        code = message.text.split(" ", 1)[1]
    if not code:
        return await ok.edit("Nothing To Carbonize...")
    x = carbon(code)
    carbon_url = x
    decodeit = open('carbon.jpg', 'wb')
    decodeit.write(base64.b64decode(carbon_url))
    decodeit.close()
    if message.from_user:
        user = message.from_user.mention
    else:
        user = message.sender_chat.title
    cap = f"__Carbonized By {user}__\n\n__By @GojoSatoru_Xbot | @Xbots_X__"
    await bot.send_photo(message.chat.id, "carbon.jpg", caption=cap)
    await ok.delete()
    os.remove("carbon.jpg")
