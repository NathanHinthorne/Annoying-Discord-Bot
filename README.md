# The Aaron Annihilator (Discord Bot)

This is a simple Discord bot that was made to listen for messages from a specific user *cough* Aaron *cough*. If the message is a gif, the bot will randomly pick a gif from a collection and send it in the same channel.

Now you too can harness the power of "The Aaron Annihilator"!

## Setup

1. Clone this repository to your local machine.

2. Install the required Python dependencies by running `pip install -r requirements.txt`.

3. Create a bot on the Discord developer portal, get the bot token, and add the bot to your server.

4. Make a `.env` file that looks like the following:

``` env
DISCORD_TOKEN=PLACEHOLDER123
CHANNEL_ID=PLACEHOLDER123
GUILD_ID=PLACEHOLDER123
```

5. Replace the placeholders in the `.env` file with your actual values. The `DISCORD_TOKEN` is the bot token from the Discord developer portal. The `USER_ID` is the ID of the user that the bot should listen to.

6. Run the bot by executing `python bot.py` or use the GUI with `python gui.py`.

7. Send a message in the Discord server and see the bot in action!

## Usage

Once the bot is running, it will listen for messages from the user specified in the `.env` file. If the user sends a gif, the bot will randomly pick a gif from the `gifs` directory and send it in the same channel.

## Dependencies

- Python 3.6+
- discord.py
- python-dotenv