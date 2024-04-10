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
            title=f'歡迎{ctx.user.name}',
            description='這是HIPB-ひぴ的首頁，不妨試試下面的功能?',
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