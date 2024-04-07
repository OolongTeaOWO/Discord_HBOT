import discord
# from mod.dms.dm_sqlite import create_table,update_added_members

class add_data(discord.ui.Modal,title="建立共享"):
    add_member = discord.ui.TextInput(
        label='新增成員',
        placeholder='Discord ID',
    )
    
    async def on_submit(self,interaction: discord.Interaction):
        try:
            # update_added_members(interaction.user.id,int(self.add_member.value))
            await interaction.response.send_message(f'已添加!', ephemeral=True)
        except:
            await interaction.response.send_message(f'ID 錯誤')
# class reaction_feedback(Modal):
#     def __init__(self):
#         super().__init__(title="反應回饋")
#         self.add_item(TextInput(label="你想說的~",style=discord.TextInput.placeholder))