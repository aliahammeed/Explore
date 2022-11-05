from genericpath import commonprefix
from http import client
from tokenize import Token
from urllib import response
from discord.ext import commands
import discord
import os
import dotenv
from dotenv import load_dotenv

import joke_api

load_dotenv()
Token= os.getenv('Token')
intents=discord.Intents.default()
intents.message_content = True
intents.members = True
client=commands.Bot(command_prefix='!',intents=intents)
@client.event
async def onready():
       print(f"{client.user}is logged in ")




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!joke'):
        response= joke_api.get_joke()
        setup=response.get("setup")
        punchline=response.get("punchline")
        
        await message.channel.send(setup)
        await message.channel.send(punchline)



client.run(Token)
