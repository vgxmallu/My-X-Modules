import os
import requests
from config import UNSPLASH_ACCESS_KEY
from pyrogram import Client,filters,types
from mbot import Mbot as Bot

access_key = UNSPLASH_ACCESS_KEY  
api = 'https://api.unsplash.com/photos?client_id={}'
random_photos = 'https://api.unsplash.com/photos/random/?count={}&client_id={}'
search_photos = 'https://api.unsplash.com/search/photos/?query={}&client_id={}'




# Checking whether Unsplash-Access-key is valid.If not, Quitting...
if isinstance(d:=requests.get(api.format(access_key)).json(),dict) and bool(d['errors']):
    print(f"\033[0;31m{d['errors'][0]}\n\nQuitting...\033[0m")
    exit(0)




# Search Photos on Unsplash
@Bot.on_message(filters.command(['photo','sea','ima','img'],['/','!']))
async def searchPhoto(c,msg: types.Message):
    if len(msg.command) == 1:
        await msg.reply('__Please specify the query.__')
        return

    q = '+'.join(msg.command[1:])
    #print(q)
    re = await msg.reply('__Searching...__')

    results = requests.get(search_photos.format(q,access_key)).json()['results']
    #print(results)

    if not results:
        await re.edit('__No photo for your query.Try with deferent keywords.__')
        return


    with open(n:=f"{results[0]['id']}.jpg",'wb') as img:
        img.write(requests.get(results[0]['urls']['raw']).content)
    
    cap = results[0]['alt_description']

    await msg.reply_photo(n,caption=(f'__{cap}__' if isinstance(cap,str) else ""))
    await re.delete()
    os.remove(n)


# Get random photos from Unsplash
@Bot.on_message(filters.command(['random','rand'],['/','!']))
async def randomPhoto(c,msg: types.Message):
    if len(msg.command) == 1:
        count = 1
    elif len(msg.command) > 2:
        await msg.reply('__Only 1 parameter or none required.But {} were given.__'.format(len(msg.command)-1))
        return
    else:
        try:
            count = int(msg.command[1])
        except ValueError:
            await msg.reply('__[ValueError]: Only integer can accept.__')
            return


    re = await msg.reply('__Getting a random photo...__')
    results = requests.get(random_photos.format(count,access_key)).json()
    
    if not results:                                     # I think this three lines are not need...
        await re.edit('__Nothing Found.__')             # But just in case :)
        return




    with open(n:=f"{results[0]['id']}.jpg",'wb') as img:
        img.write(requests.get(results[0]['urls']['raw']).content)
    
    cap = results[0]['alt_description']

    await msg.reply_photo(n,caption=(f'__{cap}__' if isinstance(cap,str) else ""))
    await re.delete()
    os.remove(n)
   
