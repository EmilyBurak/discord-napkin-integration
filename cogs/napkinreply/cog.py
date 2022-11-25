from discord.ext import commands
import config
import requests
from discord import Embed
import discord


class ReplyUpload(commands.Cog, name="napkinreply"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="napkinreply")
    async def upload_replied_message(self, ctx: commands.Context):
        """A command which uploads the message being replied to to Napkin
        Usage:
        ```
        %napkinreply (when replying to a message)
        ```
        """
        # check if reply
        if ctx.message.reference:

            # get message being replied to
            replied_message = await ctx.channel.fetch_message(
                ctx.message.reference.message_id
            )

            # post message to Napkin
            url = "https://app.napkin.one/api/createThought"
            req = {
                "email": config.EMAIL,
                "token": config.NAPKIN_TOKEN,
                "thought": replied_message.content,
            }

            requests.post(url, json=req)

            # create embed and send new thought via DM to user
            embed = Embed(
                colour=discord.Colour.from_rgb(225, 198, 153),
                title=f"Napkin Thought Added:",
            )
            embed.add_field(name=chr(173), value=f"{replied_message.content}")

            await ctx.author.send(embed=embed)
        else:
            pass


# # This function will be called when this extension is loaded.
# # It is necessary to add these functions to the bot.
def setup(bot: commands.Bot):
    bot.add_cog(ReplyUpload(bot))
