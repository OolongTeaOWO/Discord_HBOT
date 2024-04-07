import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from mod.view import Index

from mod.dms.dm_mongo import mongo_dm
from typing import Optional

load_dotenv()
Token = os.getenv("TOKEN")
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=discord.Intents.all())

@bot.event
async def on_ready():
    game = discord.Game("with the API")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    await load_all_extensions()
    print(f">>{bot.user}上線<<")
    game = discord.Game("機器人製作ing...")
    # bot.add_view(Index())

async def load_all_extensions():
    for filename in os.listdir(os.path.join(os.path.dirname(__file__), 'cogs')):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f"{filename} load")
    print('on Ready')
    slash = await bot.tree.sync()
    print(f"載入 {len(slash)} 個斜線指令")

if __name__ == "__main__":
    bot.run(Token)