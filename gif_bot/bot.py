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
USER_ID_NATHAN = os.getenv('USER_ID_NATHAN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
GUILD_ID = os.getenv('GUILD_ID')

startup_gif_url = "https://tenor.com/view/awake-woke-elmo-i-has-awoken-wake-gif-16298489"

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))
        if channel:
            await channel.send(startup_gif_url)
        print(f'Logged in as {self.user.name} - {self.user.id}')


    # @tasks.loop(minutes=10.0)
    # async def change_nickname(self):
    #     guild = await self.fetch_guild(GUILD_ID)
    #     member = await guild.fetch_member(int(USER_ID))
    #     nicknames = ['Little old me', 'Silly Aaron', 'My macro is lame', 'Goofball', 'Silly Aaron', 'Goofball', 'My macro is lame', 'Goofball', 'Silly Aaron', 'Goofball']
    #     try:
    #         await member.edit(nick=random.choice(nicknames))
    #     except Forbidden:
    #         print(f"Bot doesn't have permission to change the nickname of {member.name}")
        
    #     channel = self.get_channel(int(CHANNEL_ID))
    #     await channel.send('HAHA I changed your nickname' + ' ' + member.mention + ' to ' + member.display_name)

    # @change_nickname.before_loop
    # async def before_change_nickname(self):
    #     await self.wait_until_ready()  # wait until the bot logs in

    @commands.Cog.listener()
    async def on_message(self, message):
        # ensure the bot only responds to messages from a specific user inside a specific channel
        if (message.author.id == int(USER_ID_NATAN) or 
            message.author.id == int(USER_ID_ARSH) or
            message.author.id == int(USER_ID_NATHAN)
            ) and message.channel.id == int(CHANNEL_ID):
            gif_urls = [
                "https://tenor.com/bgPeD.gif", # goose dance
                "https://tenor.com/quxxSlANeOt.gif", # mario dance
                "https://tenor.com/bZtBe.gif", # luigi dab
                "https://tenor.com/xfl9.gif",  # come at me bro
                "https://tenor.com/bHpGx.gif", # sus cat
                "https://tenor.com/bRrTd.gif", # penguin push
                "https://tenor.com/bRCd8.gif", # dies of cringe
                "https://tenor.com/ZlGV.gif", # funny cat
                "https://tenor.com/bVIHA.gif", # cat mouth pop
                "https://tenor.com/mp4TybsNpUj.gif", # cat hit
                "https://tenor.com/qm750W9iGF3.gif", # cheerio cat
                "https://tenor.com/b02qH.gif", # cat huh
                "https://tenor.com/bVt9X.gif", # red guy dance
                "https://cdn.discordapp.com/attachments/1045048097572667422/1240894973184970815/image0.gif?ex=664e27c0&is=664cd640&hm=4b71008c2858100c6da86150442a3454d57796ad512730d01c92858704c8aa7f&",
                "https://tenor.com/bB4jn.gif", # kangaroo mhm
                "https://tenor.com/Fkeo.gif", # kangaroo kick
                "https://tenor.com/bbr7c.gif", # that's right pal
                "https://tenor.com/byzG3.gif", # duck drum
                "https://tenor.com/w7Pg.gif", # rightous! turtle
                "https://tenor.com/bRhdf.gif", # buzz floor
                "https://tenor.com/vf19.gif", # trust me, engineer
                "https://tenor.com/bw6fk.gif", # racoon plan
                "https://tenor.com/t4g9ejowwfH.gif", # slacking
                "https://tenor.com/bI3ur.gif", # sea noodles
                "https://tenor.com/sNvZYRVuoGE.gif", #bernie stare
                "https://tenor.com/XubA.gif", # gru, gorl please
                "https://tenor.com/bkyLS.gif", # eintein not impressed
                "https://tenor.com/3Sox.gif" # eintein, recursion

                # Add more gif URLs here
            ]
            gif_url = random.choice(gif_urls)
            await message.channel.send(gif_url)


intents = discord.Intents.default()  # Create a new Intents object with all flags set to False by default
intents.messages = True  # We want the bot to be able to read message content
intents.message_content = True
intents.guild_messages = True

bot = MyBot(command_prefix='$', intents=intents)  # Pass the Intents object when creating the bot
bot.run(TOKEN)