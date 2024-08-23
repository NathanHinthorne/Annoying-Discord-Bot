import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
import random
from discord.errors import Forbidden
from discord import Embed
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USER_ID_NATAN = os.getenv('USER_ID_NATAN')
USER_ID_ARSH = os.getenv('USER_ID_ARSH')
CHANNEL_ID = os.getenv('CHANNEL_ID')
GUILD_ID = os.getenv('GUILD_ID')


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @commands.Cog.listener()
    async def on_message(self, message):
        # ensure the bot only responds to messages from a specific user inside a specific channel
        if (message.author.id == int(USER_ID_NATAN) or message.author.id == int(USER_ID_ARSH)) and message.channel.id == int(CHANNEL_ID):
            response = ""
            #
            # feed message.content into an open-source LLM models to generate a response
            #
            #
            await message.channel.send(response)


intents = discord.Intents.default()  # Create a new Intents object with all flags set to False by default
intents.messages = True  # We want the bot to be able to read message content
intents.message_content = True
intents.guild_messages = True

bot = MyBot(command_prefix='$', intents=intents)  # Pass the Intents object when creating the bot
bot.run(TOKEN)