import discord
from discord.ext import commands
import os
from dotenv import dotenv_values

env: dict[str, str | None] = dotenv_values(".env")

class TemplateBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=commands.when_mentioned, intents=discord.Intents.all())

    async def setup_hook(self):
        # Loop over the two directories
        for directory in ("commands", "events"):
            # Loop over all files in the two directories
            for filename in os.listdir(directory):
                # Ignore non-python files starting with an underscore
                if not filename.startswith("_") and filename.endswith(".py"):
                    # Load cogs
                    await self.load_extension(f"{directory}.{filename[:-3]}")

        await self.tree.sync()

if __name__ == "__main__":
    bot: TemplateBot = TemplateBot()

    if env["TOKEN"]:
        bot.run(env["TOKEN"])
    else:
        raise KeyError("Environmental variable TOKEN does not exist.")