from discord.ext import commands

class CommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context[commands.Bot]) -> None:
        await ctx.send("Pong!")

    @commands.command()
    async def foo(self, ctx: commands.Context[commands.Bot]) -> None:
        await ctx.send("bar")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CommandCog(bot))
