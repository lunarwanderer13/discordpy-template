import discord
from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(f"Logged on as {self.bot.user}!")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if "show message handling debug info" in message.content:
            await message.reply("This message is a reply.")
            await message.channel.send("This message is sent in the same channel.")
            await message.channel.send(f"The author of that message is {message.author} ({message.author.id})")
            await message.add_reaction("👋")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ready(bot))
