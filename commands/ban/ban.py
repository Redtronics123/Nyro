import nextcord.ext
from nextcord.ext import commands, application_checks
from template import embeds


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
        ban_embed = embeds.TemplateEmbed(self.bot, ctx, user.color)
        ban_embed.set_thumbnail(user.avatar)
        ban_embed.add_field(name="User banned", value=str(user.name), inline=False)

        await ctx.guild.ban(user=user, reason=reason)
        await ctx.send(embed=ban_embed)

def setup(bot):
    bot.add_cog(Ban(bot))
