import nextcord.ext
from nextcord.ext import commands
import wavelink


class MusicResume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-music-resume",
        description="Resume song in voice channel.",
        guild_ids=[1032632067307085955, 1043477521473212547]
    )
    async def resume(self, ctx: nextcord.Interaction):
        node = wavelink.NodePool.get_node()
        player = node.get_player(ctx.guild)
        if not player.is_paused():
            return await ctx.send("The song is playing")
        await player.resume()
        await ctx.send("The song is playing again")


def setup(bot):
    bot.add_cog(MusicResume(bot))
