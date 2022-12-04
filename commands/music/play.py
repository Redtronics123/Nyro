import nextcord
import nextcord.ext
from nextcord.ext import commands
import wavelink
from template import embeds


class MusicPlay(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.testing = 1043477521473212547

    @nextcord.slash_command(
        name="nyro-music-play",
        description="Play your favourite song in a voice channel",
        guild_ids=[1032632067307085955, 1043477521473212547]
    )
    async def music_play(self, ctx: nextcord.Interaction, track: str):
        await ctx.response.defer()
        node = wavelink.NodePool.get_node()

        try:
            search = await wavelink.YouTubeTrack.search(query=track, return_first=True)
        except wavelink.LavalinkException:
            return await ctx.send("Track not found.")

        player = node.get_player(ctx.guild)

        if player is None:
            player = await ctx.user.voice.channel.connect(cls=wavelink.Player)

        if not player.is_playing():
            await player.play(search)

            embed_play = embeds.TemplateEmbed(self.bot, ctx, nextcord.Color.fuchsia())
            embed_play.add_field(name="Now playing", value=str(search), inline=False)
            embed_play.add_field(name="Volume", value=str(player.volume))

            await ctx.send(embed=embed_play)


def setup(bot):
    bot.add_cog(MusicPlay(bot))
