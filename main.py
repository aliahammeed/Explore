from genericpath import commonprefix
from http import client
from tokenize import Token
from discord.ext import commands
import discord
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()
Token= os.getenv('Token')
intents=discord.Intents.default()
intents.message_content = True
intents.members = True
client=commands.Bot(command_prefix='!',intents=intents)
@client.event
async def onready():
       print(f"{client.user}is logged in ")
@client.command()
async def hi(ctx):
    await ctx.reply("hello")

@client.command()
async def joke(ctx):
    await ctx.reply("Get ready to LOL")
client.run(Token)
