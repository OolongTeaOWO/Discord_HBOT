import discord

from mod.modal import add_data
from mod.dms.dm_mongo import fetch_member
# from mod.dms.dm_sqlite import get_added_members

class Index(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.button(label="個人頁面",style=discord.ButtonStyle.green)
    async def call_share(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.message.edit(view=Profile())
        await interaction.response.send_message("頁面更換完成",ephemeral=True)
    
    @discord.ui.button(label="預覽",style=discord.ButtonStyle.green)
    async def call_preview(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.message.edit(view=Preview())
        await interaction.response.send_message("頁面更換完成",ephemeral=True)
        
    @discord.ui.button(label='反應回饋',style=discord.ButtonStyle.danger,emoji='❗',custom_id="error_reaction")
    async def error_reaction(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('this is fetch_data', ephemeral=True)

class Profile(discord.ui.View):
    def __init__(self):
        super().__init__()
    
    @discord.ui.button(label='共享列表',style=discord.ButtonStyle.green,custom_id="fetch_list")
    async def fetch_list(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = fetch_member(str(interaction.user.id))
        if response == None:
            response = "沒有資料"
        await interaction.response.send_message(f'{response}', ephemeral=True)
    
    @discord.ui.button(label='建立共享',style=discord.ButtonStyle.green,custom_id="share_data")
    async def share_data(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(add_data())
    
    @discord.ui.button(label='你的資料',style=discord.ButtonStyle.green,custom_id="fetch_data")
    async def fetch_data():
        pass
        
    @discord.ui.button(label="回上一頁",style=discord.ButtonStyle.green)
    async def back(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.message.edit(view=Index())
        await interaction.response.send_message("頁面更換完成",ephemeral=True)

#喔耶
class Preview(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='提取代碼', style=discord.ButtonStyle.green, custom_id='2')
    async def gettoken(self, interaction:discord.Interaction, button:discord.ui.Button):
        interaction.response.send_message("該檔案提取代碼為00000", ephemeral=True)
    
    @discord.ui.button(label="回上一頁",style=discord.ButtonStyle.green)
    async def back(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.message.edit(view=Index())
        await interaction.response.send_message("頁面更換完成",ephemeral=True)