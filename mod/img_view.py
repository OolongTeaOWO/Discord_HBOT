import discord

class Preview(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='返回', style=discord.ButtonStyle.green, custom_id='1')
    async def comeback(self, interaction:discord.Interaction, button: discord.ui.Button):
        pass

    @discord.ui.button(label='提取代碼', style=discord.ButtonStyle.green, custom_id='2')
    async def gettoken(self, interaction:discord.Interaction, button:discord.ui.Button):
        interaction.response.send_message("該檔案提取代碼為00000", ephemeral=True)
