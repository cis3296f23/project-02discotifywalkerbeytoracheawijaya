import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
   
# Create an instance of the Intents class
intents = discord.Intents.default()

# Enable the intents you need
intents.message_content = True 

# Create an instance of the bot with the specified intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Replace 'YOUR_TOKEN' with your bot's token
token = os.getenv('TOKEN')
bot.run(token)