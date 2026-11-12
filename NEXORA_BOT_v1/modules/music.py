import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os

print("MUSIC LOADED")


# =========================
# PATHS
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

COOKIES_FILE = os.path.join(
    BASE_DIR,
    "cookies.txt"
)

NODE_PATH = r"C:\Program Files\nodejs\node.exe"

FFMPEG_PATH = (
    r"C:\Users\Amir\Downloads"
    r"\ffmpeg-9.0.1-essentials_build"
    r"\bin\ffmpeg.exe"
)


# =========================
# YT-DLP OPTIONS
# =========================

YTDLP_OPTIONS = {

    # بهترین صدای موجود
    "format": "bestaudio/best",

    # فقط یک نتیجه
    "noplaylist": True,

    # نمایش اطلاعات در ترمینال
    "quiet": False,

    # سرچ یوتیوب
    "default_search": "ytsearch1",

    # Cookies
    "cookiefile": COOKIES_FILE,

    # Node.js
    "js_runtimes": {
        "node": {
            "path": NODE_PATH
        }
    },

    # EJS
    "remote_components": [
        "ejs:github"
    ]
}


# =========================
# FFMPEG OPTIONS
# =========================

FFMPEG_OPTIONS = {

    "before_options": (
        "-reconnect 1 "
        "-reconnect_streamed 1 "
        "-reconnect_delay_max 5"
    ),

    "options": "-vn"
}


# =========================
# MUSIC COG
# =========================

class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # =========================
    # JOIN
    # =========================

    @commands.command()
    async def join(self, ctx):

        if not ctx.author.voice:

            await ctx.send(
                "❌ اول وارد یک ویس شو."
            )

            return

        channel = ctx.author.voice.channel

        try:

            if ctx.voice_client:

                await ctx.voice_client.move_to(
                    channel
                )

            else:

                await channel.connect()

            await ctx.send(
                "🎵 وارد ویس شدم."
            )

        except Exception as e:

            print("================")
            print("JOIN ERROR")
            print(e)
            print("================")

            await ctx.send(
                "❌ نتونستم وارد ویس بشم."
            )


    # =========================
    # LEAVE
    # =========================

    @commands.command()
    async def leave(self, ctx):

        if ctx.voice_client:

            await ctx.voice_client.disconnect()

            await ctx.send(
                "👋 از ویس خارج شدم."
            )

        else:

            await ctx.send(
                "❌ داخل ویس نیستم."
            )


    # =========================
    # PLAY
    # =========================

    @commands.command()
    async def play(self, ctx, *, search):

        # -------------------------
        # CONNECT TO VOICE
        # -------------------------

        if not ctx.voice_client:

            if not ctx.author.voice:

                await ctx.send(
                    "❌ اول وارد یک ویس شو."
                )

                return

            try:

                await ctx.author.voice.channel.connect()

            except Exception as e:

                print("================")
                print("VOICE CONNECT ERROR")
                print(e)
                print("================")

                await ctx.send(
                    "❌ نتونستم وارد ویس بشم."
                )

                return


        await ctx.send(
            "⏳ دارم موزیک رو آماده می‌کنم..."
        )


        # -------------------------
        # YT-DLP
        # -------------------------

        try:

            loop = asyncio.get_running_loop()


            def extract_music():

                with yt_dlp.YoutubeDL(
                    YTDLP_OPTIONS
                ) as ydl:

                    return ydl.extract_info(
                        search,
                        download=False
                    )


            info = await loop.run_in_executor(
                None,
                extract_music
            )


            # -------------------------
            # SEARCH RESULT
            # -------------------------

            if "entries" in info:

                entries = info.get(
                    "entries"
                )

                if not entries:

                    raise Exception(
                        "هیچ موزیکی پیدا نشد."
                    )

                info = entries[0]


            # -------------------------
            # AUDIO URL
            # -------------------------

            url = info.get("url")

            if not url:

                raise Exception(
                    "Audio URL پیدا نشد."
                )


            # -------------------------
            # TITLE
            # -------------------------

            title = info.get(
                "title",
                "Unknown"
            )


            print("================")
            print("MUSIC FOUND")
            print("TITLE:", title)
            print("URL FOUND:", bool(url))
            print("FFMPEG:", FFMPEG_PATH)
            print("================")


            # -------------------------
            # CHECK FFMPEG
            # -------------------------

            if not os.path.isfile(
                FFMPEG_PATH
            ):

                raise Exception(
                    "FFmpeg پیدا نشد:\n"
                    + FFMPEG_PATH
                )


            # -------------------------
            # STOP OLD MUSIC
            # -------------------------

            if ctx.voice_client.is_playing():

                ctx.voice_client.stop()


            # -------------------------
            # CREATE AUDIO SOURCE
            # -------------------------

            source = discord.FFmpegPCMAudio(
                url,
                executable=FFMPEG_PATH,
                **FFMPEG_OPTIONS
            )


            # -------------------------
            # PLAY
            # -------------------------

            ctx.voice_client.play(
                source,
                after=lambda error:
                    print(
                        "PLAYER ERROR:",
                        error
                    )
                    if error
                    else None
            )


            await ctx.send(
                f"🎶 **در حال پخش:**\n"
                f"**{title}**"
            )


        except Exception as e:

            print("================")
            print("MUSIC ERROR")
            print(e)
            print("================")

            await ctx.send(
                "❌ خطا در پخش موزیک"
            )


# =========================
# SETUP
# =========================

async def setup(bot):

    await bot.add_cog(
        Music(bot)
    )