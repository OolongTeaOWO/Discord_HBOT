import discord
from discord.ext import commands
from discord import app_commands
from typing import List, Optional, Union
import json
import os

class SetShare(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.guild = self.bot.get_guild(1226035497042972772)
        # os.system('start chrome "https://www.youtube.com/watch?v=5CEiwddPKyE"')

    @app_commands.command(name="添加共享列表成員", description="將用戶加入共享列表")
    @app_commands.describe(member = "選擇你想加入的成員")
    @app_commands.rename(member="成員")
    async def sharer(self, interaction: discord.Interaction, member: Optional[Union[discord.Member, discord.User]] = None):
        user_id = str(member.id)

        # 讀取 JSON 檔案
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                share_list = json.load(f)
        else:
            share_list = {}

        # 檢查成員是否已存在
        if "a" in share_list and user_id in share_list["a"]:
            await interaction.response.send_message("該成員已經在共享列表中！", ephemeral=True)
            return

        # 添加新成員
        if "a" not in share_list:
            share_list["a"] = []
        share_list["a"].append(user_id)

        # 寫回 JSON 文件
        with open(self.file_path, "w") as f:
            json.dump(share_list, f, indent=4)

        await interaction.response.send_message("成功添加成員到共享列表中！", ephemeral=True)

async def setup(bot):
    await bot.add_cog(SetShare(bot)) 