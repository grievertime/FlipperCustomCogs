from redbot.core import commands, modlog
import discord


# Classname should be CamelCase and the same spelling as the folder
class ModLogAuxCog(commands.Cog):
    """Aux modlog cog for handling various custom commands"""
 
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def killcount(self, ctx):
        """Gets the killcount on the server"""
        moderators_killcount = {}
        for log in await modlog.get_all_cases(ctx.guild, self.bot):
            if not log.moderator.name in moderators_killcount:
                moderators_killcount[log.moderator.name] = 0
            moderators_killcount[log.moderator.name] += 1

        output_text = '\n'.join((kc +" killcount:"+str(moderators_killcount[kc])) for kc in moderators_killcount)

        await ctx.send(output_text)
