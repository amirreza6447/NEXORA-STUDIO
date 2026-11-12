import discord
from discord.ext import commands

from settings import get_all_settings


print("LEAVE MODULE LOADED")


class Leave(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_remove(self, member):

        print("========== LEAVE DEBUG ==========")

        print("MEMBER LEFT:", member)

        print("GUILD:", member.guild.name)

        print("GUILD ID:", member.guild.id)


        # =========================
        # LOAD SETTINGS
        # =========================

        settings = get_all_settings()

        leave_settings = settings.get(
            "leave",
            {}
        )


        enabled = leave_settings.get(
            "enabled",
            True
        )


        channel_id = leave_settings.get(
            "channel_id"
        )


        print(
            "LEAVE ENABLED:",
            enabled
        )

        print(
            "LEAVE CHANNEL ID:",
            channel_id
        )


        # =========================
        # CHECK ENABLED
        # =========================

        if not enabled:

            print(
                "🔴 LEAVE SYSTEM IS DISABLED"
            )

            return


        # =========================
        # CHECK CHANNEL
        # =========================

        if not channel_id:

            print(
                "❌ LEAVE CHANNEL NOT SET"
            )

            return


        # =========================
        # GET CHANNEL
        # =========================

        channel = member.guild.get_channel(
            channel_id
        )


        if channel is None:

            print(
                "CHANNEL NOT IN CACHE, "
                "TRYING FETCH..."
            )


            try:

                channel = await self.bot.fetch_channel(
                    channel_id
                )


            except discord.NotFound:

                print(
                    "❌ LEAVE CHANNEL ID IS WRONG"
                )

                return


            except discord.Forbidden:

                print(
                    "❌ BOT HAS NO ACCESS "
                    "TO LEAVE CHANNEL"
                )

                return


            except Exception as e:

                print(
                    "❌ LEAVE CHANNEL ERROR:",
                    e
                )

                return


        print(
            "✅ LEAVE CHANNEL FOUND:",
            channel.name
        )


        # =========================
        # CREATE MESSAGE
        # =========================

        message = (

            f"🎮 **{member.name}** "
            "left the NEXORA community.\n\n"

            "Thanks for playing with us.\n"

            "Good luck on your next adventure! 💜"

        )


        # =========================
        # SEND MESSAGE
        # =========================

        try:

            await channel.send(
                message
            )


            print(
                "✅ LEAVE MESSAGE SENT"
            )


        except discord.Forbidden:

            print(
                "❌ BOT DOES NOT HAVE "
                "SEND MESSAGE PERMISSION"
            )


        except Exception as e:

            print(
                "❌ LEAVE SEND ERROR:",
                e
            )


async def setup(bot):

    await bot.add_cog(
        Leave(bot)
    )