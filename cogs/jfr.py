import discord
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
        await self.bot.jfrservers.insert({'guild_id': guild_id, 'guild_name': guild_name, 'avatar_url': guild_icon})
        await ctx.followup.send("JFR Server has been added.")
def setup(bot):
    bot.add_cog(JFR(bot))