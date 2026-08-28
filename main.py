import discord

# 1. Set up standard default intents
intents = discord.Intents.default()

# 2. Create the client instance
client = discord.Client(intents=intents)


# 3. Define the event for when the bot is ready
# (Hint: Use a decorator @client.event and an async function named on_ready)
@client.event
async def on_ready():
    # What would you print here to confirm which bot logged in?
    pass


# 4. Run the bot
# client.run('YOUR_BOT_TOKEN')
