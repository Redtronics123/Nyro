import nextcord.ext
from nextcord.ext import commands
from deep_translator import GoogleTranslator


class Translate(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-translate",
        description="Translate any text to any language",
        force_global=True
    )
    async def translate(self, ctx: nextcord.Interaction, language: str, text: str):
        if language not in GoogleTranslator().get_supported_languages():
            return await ctx.send("Language not supported.")

        translator = GoogleTranslator(target=language)
        translated_text = translator.translate(text=text)

        await ctx.send(translated_text, ephemeral=True)


def setup(bot):
    bot.add_cog(Translate(bot))
