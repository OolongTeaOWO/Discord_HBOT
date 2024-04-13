import discord
from discord.ext import commands

from dotenv import load_dotenv
from mod.view import Index

from typing import Optional
import importlib.util
import inspect
import os

load_dotenv()
Token = os.getenv("TOKEN")
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=discord.Intents.all())

@bot.event
async def on_ready():
    game = discord.Game("花椰菜")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    await load_all_extensions()
    spec=importlib.util.spec_from_file_location("view", "mod/view.py")
    view_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(view_module)
    members = inspect.getmembers(view_module, inspect.isclass)
    for name, class_ in members:
        if class_.__module__ == view_module.__name__:
            bot.add_view(class_())
            print(f"{name} 類已添加到視圖中")
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

@bot.command(name='stop_bot', help='停止機器人運行')
async def stop_bot(ctx):
    await bot.close()
    
if __name__ == "__main__":
    bot.run(Token)