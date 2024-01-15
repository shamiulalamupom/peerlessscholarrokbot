import os
from dotenv import load_dotenv
load_dotenv()
import discord
from discord.ext import commands

from bot import send_message

client = commands.Bot(command_prefix='=', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('SUCCESS!!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
        
    username = str(message.author)
    img_url = str(message.attachments[0])
    channel = str(message.channel)

    print(f"{username} said: '{img_url}' ({channel})")

    await send_message(message, img_url)

@client.command()
async def ping(ctx):
    await ctx.send('Pong')

client.run(os.getenv('DISCORD_API_KEY'))