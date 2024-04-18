import discord

from mod.modal import add_data,show_member_in_list
from mod.dms.dm_mongo import fetch_member

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
            
    @discord.ui.button(label='緊急呼叫',style=discord.ButtonStyle.danger,emoji='❗',custom_id="error_reaction")
    async def error_reaction(self, interaction: discord.Interaction, button: discord.ui.Button):
        owner = interaction.guild.owner
        await interaction.response.defer()
        await owner.send("緊急呼叫")

class Profile(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label='共享列表',style=discord.ButtonStyle.green,custom_id="share_list")
    async def fetch_list(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = fetch_member(str(interaction.user.id))
        embed = interaction.message.embeds[0]
        text = ""
        if response == None:
            embed.set_footer(text="沒有資料")
        for item in response:
            user = await interaction.client.fetch_user(item)
            text += str(user.name) +f" :  {user.id}" + "\n"
        if embed.fields:
            embed.set_field_at(index=0, name="共享列表", value=text)
        else:
            embed.insert_field_at(index=0, name="共享列表", value=text)
        embed.set_footer(text='共享列表')
        await interaction.response.edit_message(view=Profile(),embed=embed)
    
    @discord.ui.button(label='建立共享',style=discord.ButtonStyle.green,custom_id="set_share")
    async def share_data(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(add_data())
    
    @discord.ui.button(label='提取資料',style=discord.ButtonStyle.green,custom_id="get_data")
    async def get_data(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = fetch_member(str(interaction.user.id))
        embed = interaction.message.embeds[0]
        text = ""
        if response == None:
            embed.set_footer(text="沒有資料")
        for item in response:
            user = await interaction.client.fetch_user(item)
            text += str(user.name) +f" :  {user.id}" + "\n"
        if embed.fields:
            embed.set_field_at(index=0, name="共享列表", value=text)
        else:
            embed.insert_field_at(index=0, name="共享列表", value=text)
        embed.set_footer(text='共享列表')
        await interaction.response.edit_message(view=Data_Options(),embed=embed)
        
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

class OldpeopleUI(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='心跳', style=discord.ButtonStyle.green, custom_id='heart')
    async def heart(self, interaction:discord.Interaction, button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.description = "# 心跳正常"
        await interaction.response.edit_message(embed=embed)
    
    @discord.ui.button(label="血氧",style=discord.ButtonStyle.green, custom_id="blood_air")
    async def ox(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.description = "# 血氧濃度正常"
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label='步數', style=discord.ButtonStyle.green, custom_id='walk')
    async def walk(self, interaction:discord.Interaction, button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.description = "# 近期步數不足, 運動量偏少, 請多加注意"
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="心律",style=discord.ButtonStyle.green, custom_id="heart_d")
    async def heart_d(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.description = "# 心律近期有異常 請注意"
        await interaction.response.edit_message(embed=embed)

class Data_Options(discord.ui.View):
    def __init__(self):
        super().__init__()
                
    @discord.ui.button(label="選擇使用者",style=discord.ButtonStyle.green, custom_id="user_choice")
    async def user_choice(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.response.send_modal(show_member_in_list())
    
    @discord.ui.button(label="回上一頁",style=discord.ButtonStyle.green, custom_id="backs")
    async def back(self,interaction:discord.Interaction,button:discord.ui.Button):
        embed = interaction.message.embeds[0]
        embed.remove_footer()
        if embed.fields:
            embed.remove_field(index=0)
        await interaction.response.edit_message(view=Profile(),embed=embed)