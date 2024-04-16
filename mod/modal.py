import discord
from mod.dms.dm_mongo import add_member
class add_data(discord.ui.Modal,title="建立共享"):
    add_member = discord.ui.TextInput(
        label='新增成員',
        placeholder='Discord ID',
    )
    
    async def on_submit(self,interaction: discord.Interaction):
        try:
            add_member(interaction.user.id,int(self.add_member.value),1)
            embed = interaction.message.embeds[0]
            embed.set_footer(text=f'成功添加 {self.add_member.value}')
            await interaction.response.edit_message(embed=embed)
        except:
            embed = interaction.message.embeds[0]
            embed.set_footer(text=f'添加失敗')
            await interaction.response.edit_message(embed=embed)
            
