import discord
from discord.ext import commands

import random
import time

from database.database import create_user, get_connection


# =========================
# NEXORA RANK SYSTEM
# =========================

ROLE_LEVELS = {

    15: 1545583243565207633,     # 👤 Membership

    35: 1545583377095204955,     # 💠 Plus

    60: 1545583474767822939,     # ⚡ Pro

    90: 1545583660730683413,     # 💎 VIP

    130: 1545583889567715410     # 👑 Legend

}


ALL_RANK_ROLES = list(ROLE_LEVELS.values())


# ضد اسپم XP

message_cooldown = {}



# =========================
# XP FORMULA
# =========================

def get_level(xp):

    level = 1

    while xp >= (level ** 2) * 100:

        level += 1

    return level



# =========================
# GET BEST RANK
# =========================

def get_rank_role(level):

    current_role = None

    for lvl, role_id in ROLE_LEVELS.items():

        if level >= lvl:

            current_role = role_id

    return current_role



class Leveling(commands.Cog):


    def __init__(self, bot):

        self.bot = bot



    # =========================
    # MESSAGE XP
    # =========================

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return


        if not message.guild:
            return



        user_id = str(message.author.id)


        current_time = time.time()



        # هر 60 ثانیه XP

        if user_id in message_cooldown:

            if current_time - message_cooldown[user_id] < 60:

                return



        message_cooldown[user_id] = current_time



        # ساخت کاربر

        create_user(user_id)



        xp_gain = random.randint(5, 15)



        conn = get_connection()

        cursor = conn.cursor()



        cursor.execute(
            """
            SELECT xp, level
            FROM users
            WHERE discord_id = ?
            """,
            (user_id,)
        )


        user = cursor.fetchone()



        old_xp = user[0]

        old_level = user[1]



        new_xp = old_xp + xp_gain


        new_level = get_level(new_xp)



        cursor.execute(
            """
            UPDATE users
            SET xp = ?, level = ?
            WHERE discord_id = ?
            """,
            (
                new_xp,
                new_level,
                user_id
            )
        )



        conn.commit()

        conn.close()



        # =========================
        # LEVEL UP
        # =========================

        if new_level > old_level:


            embed = discord.Embed(

                title="🟣 NEXORA LEVEL UP",

                description=(

                    f"🎮 {message.author.mention}\n\n"

                    f"⭐ Level جدید:\n"
                    f"**{new_level}**\n\n"

                    f"🔥 ادامه بده، داری به Rank های بالاتر نزدیک میشی!"

                ),

                color=0x8A2BE2

            )


            embed.set_thumbnail(

                url=message.author.display_avatar.url

            )


            await message.channel.send(embed=embed)



            # =========================
            # AUTO RANK
            # =========================


            new_role_id = get_rank_role(new_level)



            if new_role_id:


                new_role = message.guild.get_role(
                    new_role_id
                )


                if new_role:


                    # حذف Rank های قبلی

                    remove_roles = []


                    for role in message.author.roles:

                        if role.id in ALL_RANK_ROLES:

                            if role.id != new_role_id:

                                remove_roles.append(role)



                    if remove_roles:

                        await message.author.remove_roles(
                            *remove_roles
                        )



                    # دادن Rank جدید

                    if new_role not in message.author.roles:


                        await message.author.add_roles(
                            new_role
                        )


                        rank_embed = discord.Embed(

                            title="🏆 NEXORA RANK UNLOCKED",

                            description=(

                                f"تبریک {message.author.mention} 🎉\n\n"

                                f"شما به Rank جدید رسیدید:\n"

                                f"**{new_role.name}**"

                            ),

                            color=0xFFD700

                        )


                        await message.channel.send(
                            embed=rank_embed
                        )



async def setup(bot):

    await bot.add_cog(Leveling(bot))

    print("LEVELING MODULE LOADED")