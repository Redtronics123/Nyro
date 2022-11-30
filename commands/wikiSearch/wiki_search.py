import nextcord
import nextcord.ext
from nextcord.ext import commands
import wikipedia
from template import embeds
from algorithm import string_split


class WikiSearch(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-wiki-search",
        description="Search in Wikipedia",
        force_global=True
    )
    async def wiki_search(self, ctx: nextcord.Interaction, search: str):
        await ctx.response.defer()
        try:
            result: str = wikipedia.summary(search)
        except wikipedia.WikipediaException:
            return await ctx.send("No content found", ephemeral=True)

        wiki_embed = embeds.TemplateEmbed(self.bot, ctx, nextcord.Color.dark_gold())
        wiki_embed.description = "All found results may not be correct!"

        if result and len(result) > 1024:
            list_strings = string_split.StringSplit(result).string_splitting()

            for element in list_strings:
                wiki_embed.add_field(name=search + "-->", value=str(element), inline=False)

        else:
            wiki_embed.add_field(name=search, value=result, inline=False)

        await ctx.send(embed=wiki_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(WikiSearch(bot))
