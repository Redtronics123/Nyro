import nextcord
import nextcord.ext
from nextcord.ext import commands
from template import buttons, embeds


class AboutGithub(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-about-github",
        description="You can see Nyro's code.",
        force_global=True
    )
    async def github(self, ctx: nextcord.Interaction):
        github_embed = embeds.TemplateEmbed(self.bot, ctx, nextcord.Color.dark_blue())
        github_embed.add_field(name="Github", value="Click on the button to open the github project.")

        github_button = buttons.ButtonUrl(name="Github", url="https://github.com/Redtronics123/Nyro")

        await ctx.send(embed=github_embed, view=github_button, ephemeral=True)


def setup(bot):
    bot.add_cog(AboutGithub(bot))
