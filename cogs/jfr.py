import discord
# Adds a new JFR server to the database
from discord.ext import commands

class JFR(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="addjfr", description="Adds a JFR server to the database. MAKE SURE THE BOT IS ALREADY IN THAT GUILD")
    @commands.has_role(1160344631075160114)
    async def addjfr(self, ctx : commands.Context, guild_id: discord.Option(str, description="The guild ID of the server.", required=True), guild_name: discord.Option(str, description="The name of the guild.", required=True)):
        await ctx.defer()
        guild = self.bot.get_guild(int(guild_id))
        if guild.icon.url == None:
            guild_icon = "https://imgur.com/a/Uyo6hfv"
        else:
            guild_icon = guild.icon.url
        default_channel = guild.system_channel
        invite = await default_channel.create_invite(max_age=0, max_uses=0)
        link = str(invite)
        await self.bot.jfrservers.insert({'guild_id': guild_id, 'guild_name': guild_name, 'avatar_url': guild_icon, 'invite_code': link})
        await ctx.followup.send("JFR Server has been added.")
def setup(bot):
    bot.add_cog(JFR(bot))