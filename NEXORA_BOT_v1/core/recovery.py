import time

from database.database import get_connection



async def check_new_members(bot):


    conn = get_connection()

    cursor = conn.cursor()



    for guild in bot.guilds:


        for member in guild.members:


            if member.bot:
                continue



            cursor.execute(
                """
                SELECT discord_id, welcomed
                FROM members
                WHERE discord_id = ?
                """,
                (str(member.id),)
            )


            data = cursor.fetchone()



            if not data:


                cursor.execute(
                    """
                    INSERT INTO members
                    (
                    discord_id,
                    joined_at,
                    welcomed
                    )
                    VALUES (?,?,?)
                    """,
                    (
                        str(member.id),
                        int(time.time()),
                        0
                    )
                )



                # Welcome Channel
                channel = guild.get_channel(
                    1537579943893016609
                )



                if channel:


                    await channel.send(
                        f"🎉 خوش آمدی {member.mention}\n\n"
                        f"🟣 به NEXORA Gaming Community خوش اومدی!"
                    )



                cursor.execute(
                    """
                    UPDATE members
                    SET welcomed = 1
                    WHERE discord_id = ?
                    """,
                    (str(member.id),)
                )



    conn.commit()

    conn.close()