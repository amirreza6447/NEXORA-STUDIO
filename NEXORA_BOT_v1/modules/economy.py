import discord
from discord.ext import commands

import random
import time

from database.database import create_user, get_connection


DAILY_COOLDOWN = 86400



class DailyWheel(discord.ui.View):

    def __init__(self, user_id):

        super().__init__(timeout=60)

        self.user_id = user_id



    @discord.ui.button(
        label="🎡 چرخش گردونه",
        style=discord.ButtonStyle.primary
    )
    async def spin(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):


        if str(interaction.user.id) != self.user_id:

            await interaction.response.send_message(
                "❌ این گردونه برای شما نیست!",
                ephemeral=True
            )

            return



        result = await spin_reward(
            interaction.user.id
        )


        await interaction.response.edit_message(
            embed=result[0],
            view=result[1]
        )





class RetryWheel(discord.ui.View):

    def __init__(self, user_id):

        super().__init__(timeout=60)

        self.user_id = user_id



    @discord.ui.button(
        label="🔄 چرخش دوباره",
        style=discord.ButtonStyle.success
    )
    async def retry(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):


        if str(interaction.user.id) != self.user_id:

            await interaction.response.send_message(
                "❌ این گردونه برای شما نیست!",
                ephemeral=True
            )

            return



        conn = get_connection()

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT daily_retry
            FROM users
            WHERE discord_id = ?
            """,
            (self.user_id,)
        )


        data = cursor.fetchone()



        if data[0] == 1:

            conn.close()

            await interaction.response.send_message(
                "❌ شما قبلاً از چرخش دوباره استفاده کردی!",
                ephemeral=True
            )

            return



        cursor.execute(
            """
            UPDATE users
            SET daily_retry = 1
            WHERE discord_id = ?
            """,
            (self.user_id,)
        )


        conn.commit()

        conn.close()



        result = await spin_reward(
            self.user_id
        )


        await interaction.response.edit_message(
            embed=result[0],
            view=None
        )





async def spin_reward(user_id):


    chance = random.randint(1,100)


    reward = 0


    if chance <= 50:

        reward = random.randint(5,15)


        conn = get_connection()

        cursor = conn.cursor()


        cursor.execute(
            """
            UPDATE users
            SET nex_balance = nex_balance + ?
            WHERE discord_id = ?
            """,
            (
                reward,
                str(user_id)
            )
        )


        conn.commit()

        conn.close()



        text = (
            f"🎉 تبریک!\n\n"
            f"🪙 جایزه شما:\n"
            f"**+{reward} NEX**"
        )


    else:

        text = (
            "❌ گردونه پوچ بود!\n\n"
            "امروز جایزه‌ای نگرفتی."
        )



    embed = discord.Embed(

        title="🟣 NEXORA DAILY WHEEL",

        description=text,

        color=0x8A2BE2

    )


    embed.set_footer(
        text="NEXORA GAMING ECONOMY"
    )


    return (
        embed,
        RetryWheel(str(user_id))
    )







class Economy(commands.Cog):


    def __init__(self, bot):

        self.bot = bot





    @commands.command(name="daily")
    async def daily(self, ctx):


        user_id = str(ctx.author.id)


        create_user(user_id)



        conn = get_connection()

        cursor = conn.cursor()



        cursor.execute(
            """
            SELECT last_daily
            FROM users
            WHERE discord_id = ?
            """,
            (user_id,)
        )


        data = cursor.fetchone()



        current_time = int(time.time())


        if current_time - data[0] < DAILY_COOLDOWN:


            remaining = DAILY_COOLDOWN - (
                current_time - data[0]
            )


            hours = remaining // 3600

            minutes = (remaining % 3600) // 60



            embed = discord.Embed(

                title="⏳ NEXORA DAILY",

                description=
                f"❌ هنوز آماده نیست!\n\n"
                f"🕒 {hours} ساعت و {minutes} دقیقه باقی مانده",

                color=0xff0000

            )


            await ctx.send(embed=embed)

            conn.close()

            return




        cursor.execute(
            """
            UPDATE users
            SET 
            last_daily = ?,
            daily_retry = 0
            WHERE discord_id = ?
            """,
            (
                current_time,
                user_id
            )
        )


        conn.commit()

        conn.close()



        embed = discord.Embed(

            title="🎡 NEXORA DAILY WHEEL",

            description=
            "گردونه آماده است!\n\n"
            "روی دکمه بزن و شانس خودتو امتحان کن 🟣",

            color=0x8A2BE2

        )



        await ctx.send(
            embed=embed,
            view=DailyWheel(user_id)
        )







async def setup(bot):

    await bot.add_cog(Economy(bot))

    print("ECONOMY MODULE LOADED")