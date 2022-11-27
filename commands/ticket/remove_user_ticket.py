import nextcord
import nextcord.ext
from nextcord.ext import commands, application_checks
from database import database_check


class RemoveUserTicket(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="nyro-ticket-remove-user",
        description="Remove user from ticket.",
        force_global=True
    )
    @application_checks.has_permissions(administrator=True)
    async def ticket_remove_user(self, ctx: nextcord.Interaction, user: nextcord.Member, ticket: nextcord.TextChannel):
        if await database_check.DatabaseCheck().check_command_status(ctx, "ticket"):
            return

        category = nextcord.utils.get(ctx.guild.categories, name="ticket")
        if len(category.channels) == 0:
            return await ctx.send("There are no tickets.", ephemeral=True)

        if user.name == ctx.user.name:
            return await ctx.send("You can't remove yourself.", ephemeral=True)

        for channel in category.channels:
            if channel.name == ticket.name:
                await ticket.set_permissions(user, view_channel=False)
                return await ctx.send(f"The user **{user}** was removed from the ticket.")

        await ctx.send("This channel is not in the category **ticket**.", ephemeral=True)


def setup(bot):
    bot.add_cog(RemoveUserTicket(bot))
