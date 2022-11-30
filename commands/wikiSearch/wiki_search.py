import nextcord
import nextcord.ext
from nextcord.ext import commands
import wikipedia
from template import embeds
from algorythmen import string_split


class Search(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-wiki-search",
        description="Search in Wikipedia",
        force_global=True
    )
    async def search(self, ctx: nextcord.Interaction, search: str):
        await ctx.response.defer()
        try:
            wikipedia.set_lang("de")
            result: str = wikipedia.summary(search)
        except wikipedia.WikipediaException:
            return await ctx.send("No content found", ephemeral=True)

        wiki_embed = embeds.TemplateEmbed(self.bot, ctx, nextcord.Color.dark_gold())

        if result and len(result) > 1024:
            list_strings = string_split.StringSplit(result).string_splitting()

            for element in list_strings:
                wiki_embed.add_field(name=search + "-->", value=str(element), inline=False)

        else:
            wiki_embed.add_field(name=search, value=result, inline=False)

        await ctx.send(embed=wiki_embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Search(bot))
