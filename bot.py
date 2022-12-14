import os
import sys

import discord
from discord.ext import commands
from discord import Embed

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

    bot = commands.Bot(commands.when_mentioned_or("%"), intents=intents)

    # Get the modules of all cogs whose directory structure is cogs/<module_name>/cog.py
    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            bot.load_extension(f"cogs.{folder}.cog")

    @bot.event
    async def on_ready():
        """When discord is connected"""
        end_time = perf_counter()
        logger.debug(
            f"{bot.user.name} has connected to Discord in {end_time - start_time} seconds!"
        )

    @bot.event
    async def on_message(message):
        """Uploads message from DMs to the bot and mentions to Napkin"""
        await bot.process_commands(message)
        # for DMs
        if not message.guild:
            url = "https://app.napkin.one/api/createThought"
            req = {
                "email": config.EMAIL,
                "token": config.NAPKIN_TOKEN,
                "thought": message.content,
            }

            requests.post(url, json=req)

            await message.author.send("```Thought uploaded.```")
        # for mentions in messages
        elif bot.user.mentioned_in(message):
            # removes mention of bot in the message before sending to Napkin
            message.content = message.content.replace(f"<@{bot.user.id}>", "")
            url = "https://app.napkin.one/api/createThought"
            req = {
                "email": config.EMAIL,
                "token": config.NAPKIN_TOKEN,
                "thought": message.content,
            }
            requests.post(url, json=req)

            # create embed and send new thought via DM to user
            embed = Embed(
                colour=discord.Colour.from_rgb(225, 198, 153),
                title=f"Napkin Thought Added:",
            )
            embed.add_field(name=chr(173), value=f"{message.content}")

            await message.author.send(embed=embed)

        else:
            pass

    # Run Discord bot
    bot.run(config.TOKEN)


if __name__ == "__main__":
    main()
