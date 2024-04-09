import discord
# slash command
from discord import app_commands

from discord.ext import commands

from mod.img_view import Preview
from mod.img_table import Generate_Table

import io

class WaitData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = "upload_file", description = "上傳檔案")
    async def GetData(self, interaction:discord.Interaction, file:discord.Attachment):
        if file.filename[-3:] == 'csv':
            csv_data = await file.read()
            csv_string = csv_data.decode('utf-8')
            data = Generate_Table(csv_string)
        else:
            await interaction.response.send_message("格式錯誤", ephemeral=True)

async def setup(bot):
    await bot.add_cog(WaitData(bot))