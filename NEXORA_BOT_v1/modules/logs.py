import discord
from discord.ext import commands

from settings import get_all_settings


print("LOGS MODULE LOADED")


class Logs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    async def send_log(
        self,
        guild,
        title,
        description,
        color=discord.Color.blue()
    ):

        # =========================
        # LOAD SETTINGS
        # =========================

        settings = get_all_settings()

        logs_settings = settings.get(
            "logs",
            {}
        )


        enabled = logs_settings.get(
            "enabled",
            True
        )


        channel_id = logs_settings.get(
            "channel_id"
        )


        print(
            "LOGS ENABLED:",
            enabled
        )

        print(
            "LOG CHANNEL ID:",
            channel_id
        )


        # =========================
        # CHECK ENABLED
        # =========================

        if not enabled:

            print(
                "🔴 LOG SYSTEM IS DISABLED"
            )

            return


        # =========================
        # CHECK CHANNEL
        # =========================

        if not channel_id:

            print(
                "❌ LOG CHANNEL NOT SET"
            )

            return


        # =========================
        # GET CHANNEL
        # =========================

        channel = guild.get_channel(
            channel_id
        )


        if channel is None:

            print(
                "LOG CHANNEL NOT IN CACHE, "
                "TRYING FETCH..."
            )


            try:

                channel = await self.bot.fetch_channel(
                    channel_id
                )


            except discord.NotFound:

                print(
                    "❌ LOG CHANNEL ID IS WRONG"
                )

                return


            except discord.Forbidden:

                print(
                    "❌ BOT HAS NO ACCESS "
                    "TO LOG CHANNEL"
                )

                return


            except Exception as e:

                print(
                    "❌ LOG CHANNEL ERROR:",
                    e
                )

                return


        # =========================
        # CREATE EMBED
        # =========================

        embed = discord.Embed(
            title=title,
            description=description,
            color=color,
            timestamp=discord.utils.utcnow()
        )


        embed.set_footer(
            text="NEXORA LOG SYSTEM"
        )


        # =========================
        # SEND LOG
        # =========================

        try:

            await channel.send(
                embed=embed
            )


            print(
                "✅ LOG SENT"
            )


        except discord.Forbidden:

            print(
                "❌ BOT DOES NOT HAVE "
                "SEND MESSAGE PERMISSION "
                "IN LOG CHANNEL"
            )


        except Exception as e:

            print(
                "❌ LOG SEND ERROR:",
                e
            )



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def testlog(self, ctx):

        await self.send_log(
            ctx.guild,
            "📋 NEXORA LOG TEST",
            f"Test log by {ctx.author.mention}",
            discord.Color.green()
        )


        await ctx.send(
            "✅ Log test sent!"
        )


async def create_log(
    bot,
    guild,
    title,
    description,
    color=discord.Color.blue()
):

    logs = bot.get_cog(
        "Logs"
    )


    if logs:

        await logs.send_log(
            guild,
            title,
            description,
            color
        )


async def setup(bot):

    await bot.add_cog(
        Logs(bot)
    )