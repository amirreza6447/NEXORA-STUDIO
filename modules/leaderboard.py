import discord
from discord.ext import commands

from database.database import get_connection



NEXORA_LOGO = "https://media.discordapp.net/attachments/1380593437635514470/1545894339379732490/NEXORA_BOT_big_stars_animated_4s.gif?width=640&height=256"



class Leaderboard(commands.Cog):


    def __init__(self, bot):

        self.bot = bot



    @commands.command(name="leaderboard")
    async def leaderboard(self, ctx):


        conn = get_connection()

        cursor = conn.cursor()



        cursor.execute(
            """
            SELECT discord_id, xp, level
            FROM users
            ORDER BY level DESC, xp DESC
            LIMIT 10
            """
        )


        users = cursor.fetchall()


        conn.close()



        if not users:


            await ctx.send(
                "❌ هنوز کسی XP ندارد."
            )

            return




        description = ""



        medals = [

            "🥇",

            "🥈",

            "🥉"

        ]



        position = 1



        for user_id, xp, level in users:



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




            description += (

                f"{icon} **{name}**\n"
                f"┗ ⭐ Level: **{level}**\n"
                f"┗ ✨ XP: **{xp:,}**\n\n"

            )



            position += 1





        embed = discord.Embed(

            title="🟣 NEXORA LEVEL HALL",

            description=description,

            color=0x8A2BE2

        )



        embed.set_thumbnail(

            url=NEXORA_LOGO

        )



        embed.set_footer(

            text="NEXORA RANK SYSTEM • Season 1 🟣"

        )



        embed.timestamp = discord.utils.utcnow()



        await ctx.send(

            embed=embed

        )





async def setup(bot):

    await bot.add_cog(Leaderboard(bot))

    print("LEADERBOARD MODULE LOADED")