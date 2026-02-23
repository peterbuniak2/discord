# Run with: .venv/bin/python discord_only.py
from dotenv import load_dotenv
load_dotenv()

import os
import ssl
import certifi

# Fix SSL certificate verification on macOS (Python.org installs)
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
