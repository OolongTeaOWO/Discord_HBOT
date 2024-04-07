import discord

from mod.modal import add_data
from mod.dms.dm_mongo import fetch_member
# from mod.dms.dm_sqlite import get_added_members

class Index(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @discord.ui.button(label='提取資料',style=discord.ButtonStyle.green,custom_id="1")
    async def fetch_data(self, interaction: discord.Interaction, button: discord.ui.Button):
        # data = get_added_members(interaction.user.id)
        response = fetch_member(str(interaction.user.id))
        if response == None:
            response = "沒有資料"
        await interaction.response.send_message(f'{response}', ephemeral=True)
    
    @discord.ui.button(label='建立共享',style=discord.ButtonStyle.green,custom_id="2")
    async def share_data(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(add_data())
    
    @discord.ui.button(label='反應回饋',style=discord.ButtonStyle.danger,emoji='❗',custom_id="3")
    async def reaction(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('this is fetch_data', ephemeral=True)