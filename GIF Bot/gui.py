import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
import random
from discord.errors import Forbidden
from discord import Embed
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USER_ID_NATAN = os.getenv('USER_ID_NATAN')
USER_ID_ARSH = os.getenv('USER_ID_ARSH')
USER_ID_NATHAN = os.getenv('USER_ID_NATHAN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
GUILD_ID = os.getenv('GUILD_ID')
startup_gif_url = "https://tenor.com/view/awake-woke-elmo-i-has-awoken-wake-gif-16298489"
shutdown_gif_url = "https://tenor.com/view/fade-away-peace-out-bye-gif-11671828036190676036"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guild_messages = True

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))
        if channel:
            await channel.send(startup_gif_url)
        print(f'Logged in as {self.user.name} - {self.user.id}')
        app.update_status(f'Logged in as {self.user.name} - {self.user.id}')

    @commands.Cog.listener()
    async def on_message(self, message):
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
            ]
            gif_url = random.choice(gif_urls)
            await message.channel.send(gif_url)
            app.update_status(f'Sent GIF: {gif_url}')

bot = MyBot(command_prefix='$', intents=intents)

class BotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF Bot")
        
        self.status_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.status_text.pack(padx=10, pady=10)
        
        self.start_button = tk.Button(root, text="Start Bot", command=self.start_bot)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop Bot", command=self.stop_bot, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        
        self.bot_thread = None

    def update_status(self, message):
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.yview(tk.END)

    def start_bot(self):
        self.update_status("Starting bot...")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.bot_thread = Thread(target=self.run_bot)
        self.bot_thread.start()

    def stop_bot(self):
        self.update_status("Stopping bot...")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)\
        
        # asyncio.run_coroutine_threadsafe(self.send_shutdown_gif(), bot.loop).result()

        bot.loop.stop()

    #! function is not working
    async def send_shutdown_gif(self):
        channel = bot.get_channel(int(CHANNEL_ID))
        if channel:
            await channel.send(shutdown_gif_url)
            self.update_status(f'Sent shutdown GIF: {shutdown_gif_url}')

    def run_bot(self):
        bot.run(TOKEN)

root = tk.Tk()
app = BotApp(root)
root.mainloop()