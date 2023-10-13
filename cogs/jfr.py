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
        channel = self.bot.get_channel(1147869001326792798)
        embed = discord.Embed(title="New JFR Server added!", description="Head to https://my.jellyfishhosting.xyz/joinforresources for more info.", color=discord.Color.blue())
        embed.add_field(name="Storage:", value="1000MB", inline=False)
        embed.add_field(name="Memory:", value="1000MB", inline=False)
        embed.add_field(name="CPU:", value="100%", inline=False)
        embed.add_field(name="Server Limit:", value="1", inline=False)
        await channel.send('<@&1161668411986804807>', embed=embed)
        await ctx.followup.send("JFR Server has been added.")

    @commands.slash_command(name="removejfr", description="Removes a JFR server from the database. RUN THIS COMMAND THEN REMOVE THE BOT FROM THE GUILD.")
    @commands.has_role(1160344631075160114)
    async def removejfr(self, ctx : commands.Context, guild_id: discord.Option(str, description="The guild ID of the server.", required=True), guild_name: discord.Option(str, description="The name of the guild.", required=True)):
        await ctx.defer()
        await self.bot.jfrservers.delete_by_custom({'guild_id': guild_id})
        channel = self.bot.get_channel(1147869001326792798)
        embed = discord.Embed(title="JFR Server removed!", description="A JFR Server has just been removed!", color=discord.Color.blue())
        embed.add_field(name="Guild Name:", value=f"{guild_name}", inline=False)
        await channel.send('<@&1161668411986804807>', embed=embed)
        await ctx.followup.send("JFR Server has been removed.")
def setup(bot):
    bot.add_cog(JFR(bot))