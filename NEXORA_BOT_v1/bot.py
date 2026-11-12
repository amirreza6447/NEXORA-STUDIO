print("NEXORA NEW BOT FILE LOADED")

import discord
from discord.ext import commands

from config import TOKEN, PREFIX
from database.database import create_tables

from core.recovery import check_new_members



intents = discord.Intents.default()

intents.members = True
intents.message_content = True





class NexoraBot(commands.Bot):

    async def setup_hook(self):

        print("SETUP HOOK STARTED")



        # =========================
        # DATABASE
        # =========================

        create_tables()

        print("DATABASE READY")





        # =========================
        # TICKET
        # =========================

        await self.load_extension("modules.ticket")

        from modules.ticket import TicketView, TicketCloseView

        self.add_view(TicketView())
        self.add_view(TicketCloseView())

        print("TICKET LOADED")





        # =========================
        # WELCOME
        # =========================

        await self.load_extension("modules.welcome")

        print("WELCOME LOADED")





        # =========================
        # LEAVE
        # =========================

        await self.load_extension("modules.leave")

        print("LEAVE LOADED")





        # =========================
        # AUTOROLE
        # =========================

        await self.load_extension("modules.autorole")

        print("AUTOROLE LOADED")





        # =========================
        # MODERATION
        # =========================

        await self.load_extension("modules.moderation")

        print("MODERATION LOADED")





        # =========================
        # LOGS
        # =========================

        await self.load_extension("modules.logs")

        print("LOGS LOADED")





        # =========================
        # GIVEAWAY
        # =========================

        await self.load_extension("modules.giveaway")

        print("GIVEAWAY LOADED")





        # =========================
        # MUSIC
        # =========================

        await self.load_extension("modules.music")

        print("MUSIC LOADED")





        # =========================
        # HELP
        # =========================

        await self.load_extension("modules.help")

        print("HELP LOADED")





        # =========================
        # SETTINGS
        # =========================

        await self.load_extension("modules.settings")

        print("SETTINGS LOADED")





        # =========================
        # LEVELING
        # =========================

        await self.load_extension("modules.leveling")

        print("LEVELING LOADED")





        # =========================
        # RANK
        # =========================

        await self.load_extension("modules.rank")

        print("RANK LOADED")





        # =========================
        # WALLET
        # =========================

        await self.load_extension("modules.wallet")

        print("WALLET LOADED")





        # =========================
        # ECONOMY
        # =========================

        await self.load_extension("modules.economy")

        print("ECONOMY LOADED")





        # =========================
        # PAY
        # =========================

        await self.load_extension("modules.economy_pay")

        print("PAY LOADED")





        # =========================
        # RICH
        # =========================

        await self.load_extension("modules.rich")

        print("RICH LOADED")





        # =========================
        # LEADERBOARD
        # =========================

        await self.load_extension("modules.leaderboard")

        print("LEADERBOARD LOADED")





        # =========================
        # SHOP
        # =========================

        await self.load_extension("modules.shop")

        print("SHOP LOADED")





        # =========================
        # AI
        # =========================

        await self.load_extension("modules.ai")

        print("AI LOADED")





        print(
            "TICKET, WELCOME, LEAVE, AUTOROLE, MODERATION, "
            "LOGS, GIVEAWAY, MUSIC, HELP, SETTINGS, "
            "LEVELING, RANK, WALLET, ECONOMY, PAY, "
            "RICH, LEADERBOARD, SHOP AND AI LOADED"
        )







bot = NexoraBot(

    command_prefix=PREFIX,

    intents=intents,

    help_command=None

)







@bot.event
async def on_ready():

    print(f"NEXORA BOT ONLINE: {bot.user}")



    # =========================
    # RECOVERY SYSTEM
    # =========================

    await check_new_members(bot)

    print("RECOVERY SYSTEM CHECKED")







@bot.command()
async def ping(ctx):

    await ctx.send("🏓 Pong!")







bot.run(TOKEN)