import discord
from discord.ext import commands

from settings import get_all_settings


print("AUTOROLE MODULE LOADED")


class AutoRole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):

        print("========== AUTOROLE DEBUG ==========")

        print("MEMBER:", member)

        print("GUILD:", member.guild.name)

        print("GUILD ID:", member.guild.id)

        print("IS BOT:", member.bot)


        # =========================
        # LOAD SETTINGS
        # =========================

        settings = get_all_settings()

        autorole_settings = settings.get(
            "autorole",
            {}
        )


        enabled = autorole_settings.get(
            "enabled",
            True
        )


        print(
            "AUTOROLE ENABLED:",
            enabled
        )


        # =========================
        # CHECK ENABLED
        # =========================

        if not enabled:

            print(
                "🔴 AUTOROLE SYSTEM IS DISABLED"
            )

            return


        # =========================
        # SELECT ROLE
        # =========================

        if member.bot:

            role_id = autorole_settings.get(
                "bot_role_id"
            )

            role_type = "BOT"

        else:

            role_id = autorole_settings.get(
                "member_role_id"
            )

            role_type = "MEMBER"


        print(
            f"{role_type} ROLE ID:",
            role_id
        )


        # =========================
        # CHECK ROLE
        # =========================

        if not role_id:

            print(
                f"❌ {role_type} ROLE NOT SET"
            )

            return


        # =========================
        # GET ROLE
        # =========================

        role = member.guild.get_role(
            role_id
        )


        if role is None:

            print(
                f"❌ {role_type} ROLE NOT FOUND: "
                f"{role_id}"
            )

            return


        # =========================
        # ADD ROLE
        # =========================

        try:

            await member.add_roles(
                role,
                reason="NEXORA Auto Role"
            )


            print(
                f"✅ {role_type} ROLE ADDED: "
                f"{role.name} → {member}"
            )


        except discord.Forbidden:

            print(
                f"❌ NEXORA BOT CANNOT ADD ROLE: "
                f"{role.name}"
            )

            print(
                "Make sure NEXORA BOT role is ABOVE "
                "the Member and Bot roles."
            )


        except Exception as e:

            print(
                "❌ AUTOROLE ERROR:",
                e
            )


async def setup(bot):

    await bot.add_cog(
        AutoRole(bot)
    )