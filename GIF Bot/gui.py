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
CHANNEL_ID = "" # blank until user gives input
GUILD_ID = "" # blank until user gives input
startup_gif_url = "https://tenor.com/view/awake-woke-elmo-i-has-awoken-wake-gif-16298489"
shutdown_gif_url = "https://tenor.com/view/fade-away-peace-out-bye-gif-11671828036190676036"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guild_messages = True

TARGETED_USERS = []

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
        if (message.channel.id == int(CHANNEL_ID)) and (str(message.author.id) in TARGETED_USERS):
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
        
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        self.start_button = tk.Button(button_frame, text="Start Bot", command=self.start_bot, bg="#32CD32")  # Lime Green
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = tk.Button(button_frame, text="Stop Bot", command=self.stop_bot, state=tk.DISABLED, bg="#FF6666")  # Lighter Red
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        self.options_button = tk.Button(button_frame, text="Options", command=self.open_options_window)
        self.options_button.pack(side=tk.LEFT, padx=5)
        
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
        self.stop_button.config(state=tk.DISABLED)
        
        bot.loop.stop()

    def run_bot(self):
        bot.run(TOKEN)

    def open_options_window(self):
        options_window = tk.Toplevel(self.root)
        options_window.title("Options")
        options_window.geometry("300x400")  # Set initial size of the options window

        tk.Label(options_window, text="GUILD_ID:").pack(pady=5)
        self.guild_id_entry = tk.Entry(options_window)
        self.guild_id_entry.pack(pady=5)
        self.guild_id_entry.insert(0, GUILD_ID)

        tk.Label(options_window, text="CHANNEL_ID:").pack(pady=5)
        self.channel_id_entry = tk.Entry(options_window)
        self.channel_id_entry.pack(pady=5)
        self.channel_id_entry.insert(0, CHANNEL_ID)

        tk.Label(options_window, text="TARGETED_USERS:").pack(pady=5)
        self.targeted_users_frame = tk.Frame(options_window)
        self.targeted_users_frame.pack(pady=5)

        self.targeted_user_entries = []
        self.add_targeted_user_entry()

        add_user_button = tk.Button(options_window, text="Add User", command=self.add_targeted_user_entry)
        add_user_button.pack(pady=5)

        save_button = tk.Button(options_window, text="Save", command=self.save_options, bg="#32CD32")  # Lime Green
        save_button.pack(pady=10)

    def add_targeted_user_entry(self):
        entry = tk.Entry(self.targeted_users_frame)
        entry.pack(pady=2)
        self.targeted_user_entries.append(entry)

    def save_options(self):
        global GUILD_ID, CHANNEL_ID, TARGETED_USERS
        GUILD_ID = self.guild_id_entry.get()
        CHANNEL_ID = self.channel_id_entry.get()
        TARGETED_USERS = [entry.get() for entry in self.targeted_user_entries if entry.get()]
        self.update_status(f"Updated GUILD_ID to {GUILD_ID}, CHANNEL_ID to {CHANNEL_ID}, and TARGETED_USERS to {TARGETED_USERS}")

root = tk.Tk()
app = BotApp(root)
root.mainloop()