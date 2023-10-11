import discord
from discord.ext import commands

class joinevent(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        data = await self.bot.jfrservers.find_by_custom({'guild_id': str(member.guild.id)})
        if data:
            userData = await self.bot.usersdb.find_by_custom({'username': member.name})
            if userData:
                storage_limit = userData.get('storage_limit')
                memory_limit = userData.get('memory_limit')
                cpu_limit = userData.get('cpu_limit')
                server_limit = userData.get('server_limit')
                await self.bot.usersdb.update_by_custom({'username': member.name}, { 'storage_limit': storage_limit+1000, 'memory_limit': memory_limit+1000, 'cpu_limit': cpu_limit+100, 'server_limit': server_limit+1 })
            else:
                print("not registered to jfh")
        else:
            print("not a jfr server")

def setup(bot):
    bot.add_cog(joinevent(bot))