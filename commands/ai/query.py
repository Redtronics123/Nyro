import nextcord.ext
from nextcord.ext import commands
from nlp.ai import processing, search


class Query(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-analysis",
        description="Text",
        force_global=True
    )
    async def analysis(self, ctx: nextcord.Interaction, text: str):
        await ctx.response.defer()
        res = await processing.Processing(text=text).processing()
        await search.Search(ctx, self.bot, res).search()


def setup(bot):
    bot.add_cog(Query(bot))
