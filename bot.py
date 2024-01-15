import discord 
import responses

import os
from dotenv import load_dotenv
load_dotenv()

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)