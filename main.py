import discord
from discord.ext import commands
import dotenv, os

def initialize_secrets():
    # 1. Handle missing .env file
    try:
        # raise_error_if_not_found=True forces an error if the file doesn't exist
        dotenv.load_dotenv(raise_error_if_not_found=True) 
    except FileNotFoundError:
        print("Error: .env file not found")
        sys.exit(1)
    # 2. Handle empty values or any ValueError
    try:
        my_bot_token = os.getenv("MY_BOT_TOKEN")
        if my_bot_token is None or my_bot_token.strip() == "":
            raise ValueError("MY_BOT_TOKEN is empty in the .env file")
    except ValueError as e:
        print(f"Error: {e}")
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
