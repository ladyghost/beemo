# Developed by Redjumpman for Redbot
from discord.ext import commands
from random import choice as randchoice


class Fortune:
    """Fortune Cookie Commands."""

    def __init__(self, bot):
        self.bot = bot
        self.fortune = ["He who laughs at himself never runs out of things to laugh at.",
                        "Man who fart in church sit in his own pew",
                        "Man who go to bed with itchy butt wake up with stinky finger",
                        "There is no I in team but U in cunt",
                        "Gay man always order same, Sum Yung Guy",
                        "Today it's up to you to create the peacefulness you long for.",
                        "A friend asks only for your time not your money.",
                        "If you refuse to accept anything but the best, you very often get it.",
                        "A smile is your passport into the hearts of others.",
                        "A good way to keep healthy is to eat more Chinese food.",
                        "Your high-minded principles spell success.",
                        "Man piss in wind, wind piss back"]

    @commands.command(name="fortune", aliases=["cookie"])
    async def _cookie(self):
        """Ask for your fortune

        And look deeply into my scales
        """
        return await self.bot.say("`" + randchoice(self.fortune) + "`")


def setup(bot):
    bot.add_cog(Fortune(bot))
