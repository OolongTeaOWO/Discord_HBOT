import discord

from mod.modal import add_data, get_data, get_message
from mod.dms.dm_mongo import fetch_member
# from mod.dms.dm_sqlite import get_added_members

class Index(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="資料共享",style=discord.ButtonStyle.green, custom_id="data_share")
    async def call_preview(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.set_footer(text="資料共享")
        await interaction.response.edit_message(view=Preview(),embed=embed)
    
    @discord.ui.button(label="共享功能",style=discord.ButtonStyle.green, custom_id="own_data")
    async def call_share(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.set_footer(text="共享功能")
        await interaction.response.edit_message(view=Profile(),embed=embed)
            
    @discord.ui.button(label='反應回饋',style=discord.ButtonStyle.danger,emoji='❗',custom_id="error_reaction")
    async def error_reaction(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(get_message())

class Profile(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label='共享列表',style=discord.ButtonStyle.green,custom_id="share_list")
    async def fetch_list(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = fetch_member(str(interaction.user.display_name))
        embed = interaction.message.embeds[0]
        text = ""
        if response == None:
            embed.set_footer(text="沒有資料")
        for item in response:
            text += item + "\n"
        if embed.fields:
            embed.set_field_at(index=0, name="共享列表", value=text)
        else:
            embed.insert_field_at(index=0, name="共享列表", value=text)
        await interaction.response.edit_message(view=Profile(),embed=embed)
    
    @discord.ui.button(label='建立共享',style=discord.ButtonStyle.green,custom_id="set_share")
    async def share_data(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(add_data())
    
    @discord.ui.button(label='提取資料',style=discord.ButtonStyle.green,custom_id="get_data")
    async def get_data(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(get_data())
        
    @discord.ui.button(label="回上一頁",style=discord.ButtonStyle.green, custom_id="back")
    async def back(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.remove_footer()
        if embed.fields:
            embed.remove_field(index=0)
        await interaction.response.edit_message(view=Index(),embed=embed)

#喔耶
class Preview(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='提取代碼', style=discord.ButtonStyle.green, custom_id='get_code')
    async def gettoken(self, interaction:discord.Interaction, button:discord.ui.Button):
        interaction.response.send_message("該檔案提取代碼為00000", ephemeral=True)
    
    @discord.ui.button(label="回上一頁",style=discord.ButtonStyle.green, custom_id="backs")
    async def back(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.remove_footer()
        await interaction.response.edit_message(view=Index(),embed=embed)
