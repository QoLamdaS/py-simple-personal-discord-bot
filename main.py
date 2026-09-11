import discord
from discord.ext import commands
import dotenv, os, sys

def initialize_secrets():
    # 1. First, check if the variable is already loaded in environment (Docker / System)
    my_bot_token = os.getenv("MY_BOT_TOKEN")
    # 2. If not found, fall back to loading from .env file
    if not my_bot_token:
        try:
            dotenv.load_dotenv(dotenv.find_dotenv(raise_error_if_not_found=True))
            my_bot_token = os.getenv("MY_BOT_TOKEN")
        except OSError:
            print("Error: .env file not found and MY_BOT_TOKEN not set in environment.")
            sys.exit(1)
    if not my_bot_token or my_bot_token.strip() == "":
        print("Error: MY_BOT_TOKEN is empty.")
        sys.exit(1)
    return my_bot_token

my_bot_token = initialize_secrets()

# 1. Set up standard default intents
intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True  # Allows the bot to read message content

# 2. Initialize the bot instance with a prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# 3. Define the event for when the bot is ready
# (Hint: Use a decorator @bot.event and an async function named on_ready)
@bot.event
async def on_ready():
    print(f'Successfully logged in as {bot.user}')
    print(f'Connected servers: {[guild.name for guild in bot.guilds]}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# 4. Run the bot
bot.run(my_bot_token)
