import discord
# slash command
from discord import app_commands

from discord.ext import commands

from mod.view import OldpeopleUI
from mod.img_table import Generate_Table

from mod.dms.dm_mongo import add_file

class WaitData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name= "old_people_ui", description = "老人模式")
    async def OldUI(self, interaction:discord.Interaction):
        embed = discord.Embed(title="老人模式介面", description="# 如有相關資訊會顯示於此", color=discord.Color.green())
        await interaction.response.send_message(embed=embed, view=OldpeopleUI())

    @app_commands.command(name = "upload_file", description = "上傳檔案")
    async def GetData(self, interaction:discord.Interaction, file:discord.Attachment):
        if file.filename[-3:] == 'csv':
            csv_data = await file.read()
            csv_string = csv_data.decode('utf-8')
            
            try:
                png = Generate_Table(csv_string)
                add_file(str(interaction.user.id),png)
                await interaction.response.send_message("ok",ephemeral=True)
            except:
                await interaction.response.send_message("錯誤!",ephemeral=True)
        else:
            await interaction.response.send_message("格式錯誤", ephemeral=True)

async def setup(bot):
    await bot.add_cog(WaitData(bot))