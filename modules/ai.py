
import discord
from discord.ext import commands
import aiohttp


print("AI MODULE LOADED")


# =========================================
# AI SETTINGS
# =========================================

AI_CHANNEL_NAME = "💜・𝗡𝗲𝘅𝗼𝗿𝗮-𝗔𝗜"

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

AI_MODEL = "qwen2.5:1.5b"


SYSTEM_PROMPT = """
تو NEXORA AI هستی، دستیار هوشمند فارسی‌زبان سرور NEXORA.

مهم‌ترین قانون:
همیشه فارسی معیار، طبیعی، روان و محاوره‌ایِ رایج در ایران بنویس.

قوانین زبان:
- از فارسی رایج در ایران استفاده کن.
- جمله‌ها را طبیعی و مثل یک فارسی‌زبان ایرانی بنویس.
- از ساختارهای غیرطبیعی یا ترجمه مستقیم از انگلیسی استفاده نکن.
- از واژه‌های نامأنوس و جمله‌بندی غیرعادی استفاده نکن.
- اگر کاربر محاوره‌ای صحبت کرد، می‌توانی محاوره‌ای و دوستانه جواب بدهی.
- اگر کاربر رسمی صحبت کرد، رسمی و محترمانه جواب بده.
- از ترکیب کردن فارسی و انگلیسی بدون دلیل خودداری کن.

شخصیت:
- دوستانه، باهوش و حرفه‌ای باش.
- کمی شوخ‌طبع باش، اما زیاده‌روی نکن.
- پاسخ‌ها را واضح و مفید بده.
- پاسخ‌های بی‌دلیل طولانی نده.

موضوعات تخصصی:
- گیمینگ
- بازی‌های ویدیویی
- تکنولوژی
- Discord
- کامپیوتر

اگر چیزی را نمی‌دانی، صادقانه بگو که مطمئن نیستی.

هرگز خودت را یک مدل زبانی معرفی نکن.
تو برای کاربران سرور، NEXORA AI هستی.
"""

class AI(commands.Cog):

    def __init__(self, bot):

        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):

        # =========================================
        # IGNORE BOTS
        # =========================================

        if message.author.bot:

            return


        # =========================================
        # CHECK AI CHANNEL
        # =========================================

        if message.channel.name != AI_CHANNEL_NAME:

            return


        # =========================================
        # CHECK EMPTY MESSAGE
        # =========================================

        if not message.content.strip():

            return


        print(
            "AI USER:",
            message.content
        )


        thinking_message = None


        try:

            # =========================================
            # THINKING MESSAGE
            # =========================================

            thinking_message = await message.channel.send(
                "🧠 دارم فکر می‌کنم..."
            )


            # =========================================
            # SEND REQUEST TO OLLAMA
            # =========================================

            payload = {

                "model": AI_MODEL,

                "messages": [

                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },

                    {
                        "role": "user",
                        "content": message.content
                    }

                ],

                "stream": False

            }


            timeout = aiohttp.ClientTimeout(
                total=120
            )


            async with aiohttp.ClientSession(
                timeout=timeout
            ) as session:


                async with session.post(
                    OLLAMA_URL,
                    json=payload
                ) as response:


                    # =========================================
                    # CHECK ERROR
                    # =========================================

                    if response.status != 200:

                        error_text = await response.text()

                        print(
                            "OLLAMA HTTP ERROR:",
                            response.status
                        )

                        print(
                            "OLLAMA ERROR:",
                            error_text
                        )

                        raise Exception(
                            f"Ollama HTTP {response.status}"
                        )


                    data = await response.json()


            # =========================================
            # GET ANSWER
            # =========================================

            answer = (
                data.get(
                    "message",
                    {}
                ).get(
                    "content",
                    ""
                )
            )


            # =========================================
            # CHECK EMPTY ANSWER
            # =========================================

            if not answer:

                answer = (
                    "متأسفم، نتونستم پاسخی تولید کنم. "
                    "یه بار دیگه امتحان کن."
                )


            # =========================================
            # DELETE THINKING MESSAGE
            # =========================================

            if thinking_message:

                await thinking_message.delete()


            # =========================================
            # DISCORD MESSAGE LIMIT
            # =========================================

            if len(answer) <= 2000:

                await message.channel.send(
                    f"🤖 {answer}"
                )


            else:

                for i in range(
                    0,
                    len(answer),
                    1900
                ):

                    part = answer[
                        i:i + 1900
                    ]


                    await message.channel.send(
                        f"🤖 {part}"
                    )


            print(
                "AI RESPONSE SENT"
            )


        except aiohttp.ClientConnectorError:

            print(
                "AI ERROR: OLLAMA NOT RUNNING"
            )


            if thinking_message:

                try:

                    await thinking_message.delete()

                except Exception:

                    pass


            await message.channel.send(

                "❌ موتور هوش مصنوعی در حال اجرا نیست.\n"
                "لطفاً Ollama را روی سیستم بررسی کن."

            )


        except Exception as e:

            print(
                "AI ERROR:",
                e
            )


            if thinking_message:

                try:

                    await thinking_message.delete()

                except Exception:

                    pass


            await message.channel.send(

                "❌ یه مشکلی در سیستم AI پیش اومد."

            )


async def setup(bot):

    await bot.add_cog(
        AI(bot)
    )

