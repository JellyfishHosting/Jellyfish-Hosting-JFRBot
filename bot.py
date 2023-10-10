import discord
# Main bot file that imports dependencies, initializes bot, connects to database, loads cogs, and runs bot.

from discord.ext import commands
import os
import config
import motor.motor_asyncio
from utils.mongo import Document


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready!")
    
if __name__ == "__main__":
    bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(config.mongo_uri))
    bot.db = bot.mongo['jellyfishhost']
    bot.jfrservers = Document(bot.db, 'jfrservers')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            print("Cog Loaded")
        else:
            continue
    bot.run(config.token)