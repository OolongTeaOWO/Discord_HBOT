import discord
# slash command
from discord import app_commands
from typing import Optional

from discord.ext import commands
from discord.ui import Button, View

from mod.view import Index

class EmbedModifier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = "start", description = "開始使用")
    async def start(self,ctx):
        new_embed = discord.Embed(
            title='歡迎使用 ひぴ 您的健康小幫手',
            description='ひぴ 已經準備好了\n快點擊下面的功能按鈕!',
            color=discord.Color.green()
        )
        new_embed.set_author(name=ctx.user.display_name,icon_url=ctx.user.display_avatar)
        await ctx.response.send_message(embed=new_embed, view=Index())
        
    # @app_commands.command(name = "test", description = "test")
    # @app_commands.describe(a = "id", b = "id",t ="type")
    # async def test(self,ctx,a: str, b: str,t:int):
    #     val = mongo_dm(a,b,t).add_member()
    #     await ctx.response.send_message(val)

async def setup(bot):
    await bot.add_cog(EmbedModifier(bot))