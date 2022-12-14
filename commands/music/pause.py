import nextcord.ext
from nextcord.ext import commands
import wavelink


class MusicPause(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-music-pause",
        description="Pause a song if bot is playing music.",
        guild_ids=[1032632067307085955, 1043477521473212547]
    )
    async def pause(self, ctx: nextcord.Interaction):
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)

        if not player.is_paused():
            await player.pause()
            return await ctx.send("Song is paused")

        return await ctx.send("Song is already paused")


def setup(bot):
    bot.add_cog(MusicPause(bot))
