import discord
from discord.ext import commands
from discord.ui import Button, View

class EmbedModifier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # 如果訊息是由機器人發送的，則不執行任何操作
        
        # 刪除前一個機器人的訊息
        async for old_message in message.channel.history(limit=10):  # 檢查前10條訊息
            if old_message.author == self.bot.user and old_message.embeds:
                await old_message.delete()
                break
        
        new_embed = discord.Embed(
            title='Modified Embed',
            description='This embed has been modified.',
            color=discord.Color.green()
        )
        await message.channel.send(embed=new_embed, view=EmbedView())

class EmbedView(View):
    def __init__(self):
        super().__init__()
        self.add_item(Button(style=discord.ButtonStyle.green, label="提取資料", custom_id="extract_data"))
        self.add_item(Button(style=discord.ButtonStyle.green, label="建立共享", custom_id="create_share"))
        self.add_item(Button(style=discord.ButtonStyle.danger, label="反應回饋", custom_id="feedback"))

async def setup(bot):
    await bot.add_cog(EmbedModifier(bot))