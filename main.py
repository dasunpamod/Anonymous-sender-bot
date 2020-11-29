from telethon.sync import TelegramClient, events, Button
from telethon import errors
from telethon.tl.types import InputPeerChat
from telethon.errors import FloodWaitError
from telethon.tl.types import ChatEmpty
import os
import uuid
import shutil
import asyncio
import logging
logging.basicConfig(level=logging.INFO)

from creds import Credentials

client = TelegramClient('Telethon Anonymous Bot',
                    api_id = Credentials.API_ID,
                    api_hash=Credentials.API_HASH).start(bot_token=Credentials.BOT_TOKEN)

DEFAULT_START = ("Hi, I am ANONYMOUS SENDER BOT.\n\n"
                 "Just Forward me Some messages or\n"
                 "media and I will Anonymize the\n"
                 "sender.\n\n"
                 "**Note -** __We Dont Promote Circulation of\n__"
                 "__Copyright Contents. This Bot is\n__"
                 "__Created for Educational Purpose\n__"
                 "__Only !!\n\n__"
                 "Please Support The Developer\n"
                 "By Joining the Support Channel👇👇")


if Credentials.START_MESSAGE is None:
  START_TEXT = DEFAULT_START
else:
  START_TEXT = Credentials.START_MESSAGE
  
@client.on(events.NewMessage)
async def startmessage(event):
  try:
    if '/start' in event.raw_text:
      ok = event.chat_id
      await client.send_message(event.chat_id,f"{START_TEXT}",
                                buttons=[[Button.url("✤ SUPPORT CHANNEL ✤","t.me/Prothinkergang")]])                                                                 
    if event.message.media:
      await client.send_message(event.chat_id,file=event.message.media)
    else:
      await client.send_message(event.chat_id,event.message)
  except FloodWaitError as e:
    pass
    

with client:
  client.run_until_disconnected() 
