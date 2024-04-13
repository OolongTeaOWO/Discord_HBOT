import discord
# slash command
from discord import app_commands

from discord.ext import commands

from mod.view import Preview
from mod.img_table import Generate_Table

from mod.dms.dm_mongo import add_file

import io

class WaitData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = "upload_files", description = "上傳檔案")
    async def getdata(self, interaction:discord.Interaction, code:int, file:discord.Attachment):
        if file.filename[-3:] == 'csv':
            csv_data = await file.read()
            csv_string = csv_data.decode('utf-8')
            
            try:
                png = Generate_Table(csv_string)
                add_file(str(interaction.user.id), png, code)
                await interaction.response.send_message("ok",ephemeral=True)
            except:
                await interaction.response.send_message("錯誤!",ephemeral=True)
        else:
            await interaction.response.send_message("格式錯誤", ephemeral=True)

async def setup(bot):
    await bot.add_cog(WaitData(bot))