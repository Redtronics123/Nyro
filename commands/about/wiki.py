import nextcord
import nextcord.ext
from nextcord.ext import commands
from template import buttons, embeds


class AboutWiki(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-about-wiki",
        description="You can see Nyro's wiki.",
        force_global=True
    )
    async def github(self, ctx: nextcord.Interaction):
        wiki_embed = embeds.TemplateEmbed(self.bot, ctx, nextcord.Color.dark_blue())
        wiki_embed.add_field(name="Github", value="Click on the button to open the wiki.")

        wiki_button = buttons.ButtonUrl(name="Wiki", url="https://github.com/Redtronics123/Nyro/wiki")

        await ctx.send(embed=wiki_embed, view=wiki_button, ephemeral=True)


def setup(bot):
    bot.add_cog(AboutWiki(bot))
