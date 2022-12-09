import nextcord
import nextcord.ext
from nextcord.ext import commands, application_checks
from template import embeds


class Unban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-unban",
        description="Unban a user",
        force_global=True
    )
    @application_checks.has_permissions(administrator=True)
    async def unban(self, ctx: nextcord.Interaction, user: nextcord.Member, reason: str):
        unban_embed = embeds.TemplateEmbed(self.bot, ctx, user.color)
        unban_embed.set_thumbnail(user.avatar)
        unban_embed.add_field(name="User unban", value=str(user.name), inline=False)

        try:
            await ctx.guild.unban(user=user, reason=reason)
            await ctx.send(embed=unban_embed, ephemeral=True)

        except nextcord.NotFound:
            return await ctx.send("User not unbanned", ephemeral=True)


def setup(bot):
    bot.add_cog(Unban(bot))
