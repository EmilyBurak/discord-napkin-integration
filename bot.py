# import os
import sys

import discord
from discord.ext import commands

import config
from loguru import logger
from time import perf_counter
import requests


def main():

    start_time = perf_counter()
    logger.add(sys.stderr, level="INFO")
    # allows privledged intents for monitoring members joining, roles editing, and role assignments
    # these need to be enabled in the developer portal as well
    # not sure which of these are needed
    intents = discord.Intents.default()

    intents.guilds = True
    intents.members = True
    intents.message_content = True

    intents.presences = True

    # activity = discord.Activity(
    #     type=discord.ActivityType.listening, name=f"!napkinhelp"
    # )

    bot = commands.Bot(
        commands.when_mentioned_or(""),
        intents=intents,
        # activity=activity,
    )

    # Get the modules of all cogs whose directory structure is cogs/<module_name>/cog.py
    # Not currently using cogs
    # for folder in os.listdir("cogs"):
    #     if os.path.exists(os.path.join("cogs", folder, "cog.py")):
    #         bot.load_extension(f"cogs.{folder}.cog")

    @bot.event
    async def on_ready():
        """When discord is connected"""
        end_time = perf_counter()
        logger.debug(
            f"{bot.user.name} has connected to Discord in {end_time - start_time} seconds!"
        )

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)
        if not message.guild:
            url = "https://app.napkin.one/api/createThought"
            req = {
                "email": config.EMAIL,
                "token": config.NAPKIN_TOKEN,
                "thought": message.content,
            }

            requests.post(url, json=req)

        else:
            pass

    # Run Discord bot
    bot.run(config.TOKEN)


if __name__ == "__main__":
    main()
