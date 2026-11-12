import discord
from discord.ext import commands

from database.database import get_connection



# لوگوی NEXORA برای Thumbnail
NEXORA_LOGO = "https://media.discordapp.net/attachments/1380593437635514470/1545894339379732490/NEXORA_BOT_big_stars_animated_4s.gif?ex=6a9e768b&is=6a9d250b&hm=105dc83e9294999cfdb8a47950ab89abd2aedf2457af99f9105f6206089592ef&=&width=640&height=256"




class Rich(commands.Cog):


    def __init__(self, bot):

        self.bot = bot




    @commands.command(name="rich")
    async def rich(self, ctx):


        conn = get_connection()

        cursor = conn.cursor()



        # Top 10 Rich Users

        cursor.execute(
            """
            SELECT discord_id, nex_balance
            FROM users
            ORDER BY nex_balance DESC
            LIMIT 10
            """
        )


        users = cursor.fetchall()



        # Economy Stats

        cursor.execute(
            """
            SELECT COUNT(*), SUM(nex_balance)
            FROM users
            """
        )


        stats = cursor.fetchone()


        conn.close()



        if not users:


            await ctx.send(
                "❌ هنوز کسی NEX ندارد."
            )

            return




        total_users = stats[0] or 0

        total_nex = stats[1] or 0



        description = ""



        medals = [

            "🥇",

            "🥈",

            "🥉"

        ]



        position = 1



        for user_id, balance in users:


            user = self.bot.get_user(
                int(user_id)
            )


            if user:

                name = user.name

            else:

                name = "Unknown"




            if position <= 3:

                icon = medals[position-1]

            else:

                icon = f"#{position}"




            if position == 1:

                extra = "\n👑 **TOP HOLDER**"

            else:

                extra = ""



            description += (

                f"{icon} **{name}**\n"
                f"┗ 🪙 **{balance:,} NEX**"
                f"{extra}\n\n"

            )



            position += 1





        embed = discord.Embed(

            title="🟣 NEXORA WEALTH HALL",

            description=description,

            color=0x8A2BE2

        )



        embed.add_field(

            name="🌐 Economy Statistics",

            value=(

                f"👥 Users: **{total_users}**\n"
                f"🪙 Total NEX: **{total_nex:,}**"

            ),

            inline=False

        )





        if NEXORA_LOGO != "LINK_YOUR_LOGO_HERE":

            embed.set_thumbnail(

                url=NEXORA_LOGO

            )





        embed.set_footer(

            text="NEXORA ECONOMY SYSTEM • Season 1 🟣"

        )


        embed.timestamp = discord.utils.utcnow()



        await ctx.send(

            embed=embed

        )






async def setup(bot):

    await bot.add_cog(Rich(bot))

    print("RICH MODULE LOADED")