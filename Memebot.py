import discord
from api import *
from dotenv import load_dotenv
import os

load_dotenv()

class Myclient(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('!meme'):
            await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = Myclient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN'))