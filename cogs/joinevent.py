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
                people_joined = data.get('people_joined')
                storage_limit = userData.get('storage_limit')
                memory_limit = userData.get('memory_limit')
                cpu_limit = userData.get('cpu_limit')
                server_limit = userData.get('server_limit')
                
                # Check if the member is already in the people_joined list
                member_data = next((item for item in people_joined if item.get(member.name)), None)
                if member_data:
                    print(f"{member.name} is already in the people_joined list.")
                else:
                    # If not, add them to the list
                    people_joined.append({f'{member.name}': f'{str(member.id)}'})
                    await self.bot.jfrservers.update_by_custom({'guild_id': str(member.guild.id)}, {'people_joined': people_joined})
                    
                    # Update user limits
                    await self.bot.usersdb.update_by_custom({'username': member.name}, { 
                        'storage_limit': storage_limit+1000, 
                        'memory_limit': memory_limit+1000, 
                        'cpu_limit': cpu_limit+100, 
                        'server_limit': server_limit+1
                    })
            else:
                print("not registered to jfh")
        else:
            print("not a jfr server")

def setup(bot):
    bot.add_cog(joinevent(bot))
