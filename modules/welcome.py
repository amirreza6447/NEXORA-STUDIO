import discord
from discord.ext import commands

from settings import get_guild_settings
from config import SERVER_SETTINGS


print("WELCOME MODULE LOADED")


WELCOME_IMAGE_URL = (
    "https://cdn.discordapp.com/attachments/"
    "1149719751371788389/"
    "1539711913821343876/"
    "ChatGPT_Image_Aug_19_2026_10_32_43_PM.png"
)


class Welcome(commands.Cog):

    def __init__(self, bot):

        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):

        print("========== WELCOME DEBUG ==========")

        print(
            "NEW MEMBER JOINED:",
            member
        )

        print(
            "GUILD:",
            member.guild.name
        )

        print(
            "GUILD ID:",
            member.guild.id
        )


        # =====================================
        # CHECK SERVER CONFIG
        # =====================================

        server_config = SERVER_SETTINGS.get(
            member.guild.id
        )


        if server_config is None:

            print(
                "❌ THIS SERVER IS NOT "
                "CONFIGURED"
            )

            return


        # =====================================
        # LOAD SETTINGS FOR THIS SERVER ONLY
        # =====================================

        guild_settings = get_guild_settings(
            member.guild.id
        )


        welcome_settings = guild_settings.get(
            "welcome",
            {}
        )


        enabled = welcome_settings.get(
            "enabled",
            True
        )


        # =====================================
        # GET CHANNEL
        # =====================================

        # ابتدا تنظیمات پنل
        channel_id = welcome_settings.get(
            "channel_id"
        )


        # اگر از پنل تنظیم نشده باشد
        # از config.py استفاده می‌کنیم

        if not channel_id:

            channel_id = server_config.get(
                "welcome_channel"
            )


        print(
            "WELCOME ENABLED:",
            enabled
        )

        print(
            "WELCOME CHANNEL ID:",
            channel_id
        )


        # =====================================
        # CHECK ENABLED
        # =====================================

        if not enabled:

            print(
                "🔴 WELCOME SYSTEM IS DISABLED"
            )

            return


        # =====================================
        # CHECK CHANNEL
        # =====================================

        if not channel_id:

            print(
                "❌ WELCOME CHANNEL NOT SET"
            )

            return


        # =====================================
        # GET CHANNEL
        # =====================================

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
                    "❌ WELCOME CHANNEL ID IS WRONG"
                )

                return


            except discord.Forbidden:

                print(
                    "❌ BOT HAS NO ACCESS "
                    "TO WELCOME CHANNEL"
                )

                return


            except Exception as e:

                print(
                    "❌ WELCOME CHANNEL ERROR:",
                    e
                )

                return


        # =====================================
        # SECURITY CHECK
        # =====================================

        if channel.guild.id != member.guild.id:

            print(
                "❌ CHANNEL BELONGS "
                "TO ANOTHER SERVER"
            )

            return


        print(
            "✅ WELCOME CHANNEL FOUND:",
            channel.name
        )


        # =====================================
        # CREATE EMBED
        # =====================================

        embed = discord.Embed(

            title="🎮 Welcome To NEXORA",

            description=(

                f"سلام {member.mention} 👋\n\n"

                "به خانواده بزرگ NEXORA خوش اومدی 💜\n\n"

                "🎮 اخبار و معرفی بازی‌ها\n"
                "🛒 خدمات و محصولات گیمینگ\n"
                "💬 کامیونیتی گیمرها\n\n"

                "امیدواریم لحظات خوبی کنار ما داشته باشی ✨"

            ),

            color=discord.Color.purple()

        )


        # =====================================
        # MEMBER AVATAR
        # =====================================

        embed.set_thumbnail(

            url=member.display_avatar.url

        )


        # =====================================
        # WELCOME IMAGE
        # =====================================

        embed.set_image(

            url=WELCOME_IMAGE_URL

        )


        # =====================================
        # FOOTER
        # =====================================

        embed.set_footer(

            text=(
                f"NEXORA Community • "
                f"Members: "
                f"{member.guild.member_count}"
            )

        )


        # =====================================
        # SEND MESSAGE
        # =====================================

        try:

            await channel.send(
                embed=embed
            )


            print(
                "✅ WELCOME MESSAGE SENT"
            )


        except discord.Forbidden:

            print(
                "❌ BOT DOES NOT HAVE "
                "SEND MESSAGE PERMISSION"
            )


        except Exception as e:

            print(
                "❌ WELCOME SEND ERROR:",
                e
            )


async def setup(bot):

    await bot.add_cog(
        Welcome(bot)
    )