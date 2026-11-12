import discord
from discord.ext import commands

from database.database import get_connection
from utils.rank_card import create_rank_card


ROLE_NAMES = {

    1545583243565207633: "👤 Membership",

    1545583377095204955: "💠 Plus",

    1545583474767822939: "⚡ Pro",

    1545583660730683413: "💎 VIP",

    1545583889567715410: "👑 Legend"

}



def get_next_level_xp(level):

    return (level ** 2) * 100



class Rank(commands.Cog):


    def __init__(self, bot):

        self.bot = bot



    @commands.command(name="rank")

    async def rank(self, ctx):

        user_id = str(ctx.author.id)



        conn = get_connection()

        cursor = conn.cursor()



        cursor.execute(
            """
            SELECT xp, level, nex_balance
            FROM users
            WHERE discord_id = ?
            """,
            (user_id,)
        )


        data = cursor.fetchone()


        conn.close()



        if not data:

            await ctx.send(
                "❌ هنوز اطلاعاتی از شما ثبت نشده."
            )

            return



        xp, level, nex = data



        next_xp = get_next_level_xp(level + 1)



        current_rank = "👤 Member"



        for role in ctx.author.roles:

            if role.id in ROLE_NAMES:

                current_rank = ROLE_NAMES[role.id]



        card = await create_rank_card(

            ctx.author,

            level,

            xp,

            next_xp,

            nex,

            current_rank

        )



        file = discord.File(

            card,

            filename="NEXORA_RANK_CARD.png"

        )



        await ctx.send(

            file=file

        )





async def setup(bot):

    await bot.add_cog(Rank(bot))

    print("RANK MODULE LOADED")