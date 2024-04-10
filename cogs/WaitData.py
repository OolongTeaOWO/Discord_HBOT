<<<<<<< HEAD
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

    @app_commands.command(name = "upload_file", description = "上傳檔案")
    async def GetData(self, interaction:discord.Interaction, file:discord.Attachment):
        if file.filename[-3:] == 'csv':
            csv_data = await file.read()
            csv_string = csv_data.decode('utf-8')
            
            base64_img = Generate_Table(csv_string)
            add_file(str(interaction.user.id),base64_img)
            await interaction.response.send_message("ok")
        else:
            await interaction.response.send_message("格式錯誤", ephemeral=True)

async def setup(bot):
=======
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

    @app_commands.command(name = "upload_file", description = "上傳檔案")
    async def GetData(self, interaction:discord.Interaction, file:discord.Attachment):
        if file.filename[-3:] == 'csv':
            csv_data = await file.read()
            csv_string = csv_data.decode('utf-8')
            
            base64_img = Generate_Table(csv_string)
            add_file(str(interaction.user.id),base64_img)
            await interaction.response.send_message("ok")
        else:
            await interaction.response.send_message("格式錯誤", ephemeral=True)

async def setup(bot):
>>>>>>> 4fc6f581afbb085ce78f142c6b396df41ca980c5
    await bot.add_cog(WaitData(bot))