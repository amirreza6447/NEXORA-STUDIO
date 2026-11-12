import discord
from discord.ext import commands

from database.database import get_connection


ROLE_NAMES = {

    1545583243565207633: "👤 Membership",

    1545583377095204955: "💠 Plus",

    1545583474767822939: "⚡ Pro",

    1545583660730683413: "💎 VIP",

    1545583889567715410: "👑 Legend"

}



class Wallet(commands.Cog):


    def __init__(self, bot):

        self.bot = bot



    @commands.command(name="wallet")
    async def wallet(self, ctx):

        user_id = str(ctx.author.id)


        conn = get_connection()

        cursor = conn.cursor()



        cursor.execute(
            """
            SELECT xp, level, nex_balance, purchased_nex, reward_nex, rank
            FROM users
            WHERE discord_id = ?
            """,
            (user_id,)
        )


        data = cursor.fetchone()


        conn.close()



        if not data:

            await ctx.send(
                "❌ اطلاعات کیف پول شما ثبت نشده."
            )

            return



        xp, level, nex, purchased, reward, rank = data



        current_rank = "👤 Member"



        for role in ctx.author.roles:

            if role.id in ROLE_NAMES:

                current_rank = ROLE_NAMES[role.id]



        embed = discord.Embed(

            title="🟣 NEXORA WALLET",

            description=(

                f"👤 **User**\n"
                f"{ctx.author.mention}\n\n"

                f"🪙 **NEX COIN**\n"
                f"**{nex} NEX**\n\n"

                f"⭐ **Level**\n"
                f"**{level}**\n\n"

                f"🏆 **Rank**\n"
                f"**{current_rank}**\n\n"

                f"💳 **Purchased NEX**\n"
                f"**{purchased}**\n\n"

                f"🎁 **Reward NEX**\n"
                f"**{reward}**"

            ),

            color=0x8A2BE2

        )


        embed.set_thumbnail(

            url=ctx.author.display_avatar.url

        )


        embed.set_footer(

            text="NEXORA GAMING ECONOMY 🟣"

        )


        await ctx.send(embed=embed)





async def setup(bot):

    await bot.add_cog(Wallet(bot))

    print("WALLET MODULE LOADED")