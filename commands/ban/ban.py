import nextcord
import nextcord.ext
from nextcord.ext import commands, application_checks


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-ban",
        description="Ban a player from the server",
        force_global=True
    )
    @application_checks.has_permissions(administrator=True)
    async def ban(self, ctx: nextcord.Interaction, user: nextcord.Member, reason: str):
        await ctx.guild.ban(user=user, reason=reason)
        await ctx.send(f"The user {user} was banned from the server.")

def setup(bot):
    bot.add_cog(Ban(bot))
