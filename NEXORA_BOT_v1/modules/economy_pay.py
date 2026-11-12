import discord
from discord.ext import commands

from database.database import create_user, get_connection


class Pay(commands.Cog):

    def __init__(self, bot):

        self.bot = bot



    @commands.command(name="pay")
    async def pay(self, ctx, member: discord.Member, amount: int):


        sender_id = str(ctx.author.id)

        receiver_id = str(member.id)



        # جلوگیری از پرداخت به خود

        if sender_id == receiver_id:

            await ctx.send(
                "❌ نمی‌تونی به خودت NEX ارسال کنی."
            )

            return



        # مقدار منفی

        if amount <= 0:

            await ctx.send(
                "❌ مقدار باید بیشتر از صفر باشد."
            )

            return



        create_user(sender_id)

        create_user(receiver_id)



        conn = get_connection()

        cursor = conn.cursor()



        # موجودی فرستنده

        cursor.execute(
            """
            SELECT nex_balance
            FROM users
            WHERE discord_id = ?
            """,
            (sender_id,)
        )


        sender_balance = cursor.fetchone()[0]



        if sender_balance < amount:

            conn.close()

            await ctx.send(
                "❌ موجودی NEX کافی نیست."
            )

            return



        # کم کردن از فرستنده

        cursor.execute(
            """
            UPDATE users
            SET nex_balance = nex_balance - ?
            WHERE discord_id = ?
            """,
            (
                amount,
                sender_id
            )
        )



        # اضافه کردن به گیرنده

        cursor.execute(
            """
            UPDATE users
            SET nex_balance = nex_balance + ?
            WHERE discord_id = ?
            """,
            (
                amount,
                receiver_id
            )
        )



        conn.commit()

        conn.close()



        embed = discord.Embed(

            title="🟣 NEXORA TRANSFER",

            description=(

                f"💸 انتقال موفق!\n\n"

                f"👤 فرستنده:\n"
                f"{ctx.author.mention}\n\n"

                f"🎁 گیرنده:\n"
                f"{member.mention}\n\n"

                f"🪙 مقدار:\n"
                f"**{amount} NEX**"

            ),

            color=0x8A2BE2

        )


        embed.set_footer(
            text="NEXORA ECONOMY SYSTEM 🟣"
        )


        await ctx.send(embed=embed)




async def setup(bot):

    await bot.add_cog(Pay(bot))

    print("PAY MODULE LOADED")