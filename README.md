# The Aaron Annihilator (Discord Bot)

This is a simple Discord bot that was made to listen for messages from a specific user *cough* Aaron *cough*. If the message is a gif, the bot will randomly pick a gif from a collection and send it in the same channel.

Now you too can harness the power of "The Aaron Annihilator"!

## Setup

1. Invite The Aaron Annihilator bot to your server using [this link](https://discord.com/oauth2/authorize?client_id=1184186946818412554&permissions=67233856&integration_type=0&scope=bot).

2. Download `gui.exe` from `gif_bot/dist`

3. Run `gui.exe` and click "Options", then find the following IDs on Discord and paste them into their respective fields in the app:

   NOTE: Ensure you're in Discord's dev mode for this. If you do    n't know how to do that, check out [this guide](https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/).

   - Right click server  > Copy ID
   - Right click channel > Copy ID
   - Right click user    > Copy ID

## Dependencies

- Python 3.6+
- discord.py
- python-dotenv