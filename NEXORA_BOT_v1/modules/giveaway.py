import discord
from discord.ext import commands, tasks
import asyncio
import random
import datetime

from config import GIVEAWAY_CHANNEL_ID


print("GIVEAWAY MODULE LOADED")


active_giveaways = {}


class Giveaway(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    def parse_time(self, time):

        unit = time[-1]
        amount = int(time[:-1])

        if unit == "s":
            return amount

        if unit == "m":
            return amount * 60

        if unit == "h":
            return amount * 3600

        if unit == "d":
            return amount * 86400

        return None



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def gstart(self, ctx, duration=None, *, prize=None):

        if duration is None or prize is None:
            await ctx.send(
                "❌ Example:\n"
                "`!gstart 24h Steam Gift Card`"
            )
            return


        seconds = self.parse_time(duration)


        if seconds is None:
            await ctx.send(
                "❌ Invalid time format.\n"
                "Use: 10s / 5m / 2h / 1d"
            )
            return



        channel = self.bot.get_channel(
            GIVEAWAY_CHANNEL_ID
        )


        if channel is None:
            await ctx.send(
                "❌ Giveaway channel not found."
            )
            return



        embed = discord.Embed(
            title="🎉 NEXORA GIVEAWAY",
            description=(
                f"🎁 **Prize:**\n"
                f"{prize}\n\n"
                "React with 🎉 to enter!\n\n"
                f"⏳ Ends: <t:{int(datetime.datetime.now().timestamp()) + seconds}:R>"
            ),
            color=discord.Color.purple()
        )


        embed.set_footer(
            text="NEXORA Community Giveaway"
        )


        message = await channel.send(
            embed=embed
        )


        await message.add_reaction("🎉")


        active_giveaways[message.id] = {
            "message": message,
            "channel": channel,
            "prize": prize
        }


        await ctx.send(
            "✅ Giveaway started!"
        )


        await asyncio.sleep(seconds)


        await self.end_giveaway(
            message.id
        )



    async def end_giveaway(self, message_id):

        giveaway = active_giveaways.get(
            message_id
        )


        if giveaway is None:
            return


        message = giveaway["message"]
        channel = giveaway["channel"]


        try:
            message = await channel.fetch_message(
                message.id
            )

        except Exception as e:
            print("GIVEAWAY FETCH ERROR:", e)
            return



        users = set()


        for reaction in message.reactions:

            if str(reaction.emoji) == "🎉":

                async for user in reaction.users():

                    if not user.bot:
                        users.add(user)



        print(
            f"GIVEAWAY USERS FOUND: {len(users)}"
        )



        if users:

            winner = random.choice(
                list(users)
            )


            await channel.send(
                f"🎉 **Giveaway Ended!**\n\n"
                f"🎁 Prize: **{giveaway['prize']}**\n"
                f"🏆 Winner: {winner.mention}\n\n"
                f"تبریک به برنده 🎊"
            )


            print(
                f"GIVEAWAY WINNER: {winner}"
            )


        else:

            await channel.send(
                "❌ Giveaway ended but nobody joined."
            )


            print(
                "NO GIVEAWAY USERS"
            )


        del active_giveaways[message_id]



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def gend(self, ctx):

        if not active_giveaways:

            await ctx.send(
                "❌ No active giveaways."
            )
            return


        giveaway_id = list(active_giveaways.keys())[0]

        await self.end_giveaway(
            giveaway_id
        )

        await ctx.send(
            "✅ Giveaway ended manually."
        )



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def greroll(self, ctx):

        await ctx.send(
            "🔄 Reroll system will be added with saved giveaways."
        )



async def setup(bot):

    await bot.add_cog(
        Giveaway(bot)
    )