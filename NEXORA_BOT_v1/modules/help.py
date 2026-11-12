import discord
from discord.ext import commands

from config import PREFIX


print("HELP MODULE LOADED")


# =========================================================
# HELP MAIN VIEW
# =========================================================

class HelpView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=180)

    @discord.ui.button(
        label="Music",
        emoji="🎵",
        style=discord.ButtonStyle.primary
    )
    async def music_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="🎵 NEXORA MUSIC",
            description=(
                f"**{PREFIX}play <song>**\n"
                "پخش آهنگ از YouTube\n\n"

                f"**{PREFIX}stop**\n"
                "توقف موزیک در حال پخش\n\n"

                f"**{PREFIX}join**\n"
                "ورود NEXORA به Voice Channel\n\n"

                f"**{PREFIX}leave**\n"
                "خروج NEXORA از Voice Channel"
            ),
            color=discord.Color.purple()
        )

        embed.set_footer(
            text="NEXORA MUSIC • Your Music. Your Vibe."
        )

        await interaction.response.edit_message(
            embed=embed,
            view=HelpView()
        )


    @discord.ui.button(
        label="Ticket",
        emoji="🎫",
        style=discord.ButtonStyle.primary
    )
    async def ticket_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="🎫 NEXORA TICKET",
            description=(
                "سیستم Ticket برای ارتباط با تیم پشتیبانی سرور.\n\n"

                f"**{PREFIX}ticketpanel**\n"
                "ارسال پنل Ticket\n\n"

                "از طریق پنل می‌توانید برای موارد مختلف "
                "تیکت ایجاد کنید."
            ),
            color=discord.Color.blue()
        )

        embed.set_footer(
            text="NEXORA TICKET SYSTEM"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=HelpView()
        )


    @discord.ui.button(
        label="Giveaway",
        emoji="🎁",
        style=discord.ButtonStyle.primary
    )
    async def giveaway_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="🎁 NEXORA GIVEAWAY",
            description=(
                f"**{PREFIX}gstart**\n"
                "شروع Giveaway جدید\n\n"

                "سیستم Giveaway برای برگزاری مسابقه "
                "و انتخاب برنده در سرور استفاده می‌شود."
            ),
            color=discord.Color.gold()
        )

        embed.set_footer(
            text="NEXORA GIVEAWAY SYSTEM"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=HelpView()
        )


    @discord.ui.button(
        label="Moderation",
        emoji="🛡️",
        style=discord.ButtonStyle.danger
    )
    async def moderation_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="🛡️ NEXORA MODERATION",
            description=(
                "ابزارهای مدیریت و کنترل کاربران سرور.\n\n"

                "دستورات Moderation شامل ابزارهایی "
                "برای مدیریت اعضا و حفظ نظم سرور هستند.\n\n"

                "🔒 دستورات مدیریتی فقط برای کاربران "
                "دارای Permission مناسب قابل استفاده هستند."
            ),
            color=discord.Color.red()
        )

        embed.set_footer(
            text="NEXORA MODERATION SYSTEM"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=HelpView()
        )


    @discord.ui.button(
        label="User",
        emoji="👤",
        style=discord.ButtonStyle.success
    )
    async def user_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="👤 NEXORA USER COMMANDS",
            description=(
                f"**{PREFIX}ping**\n"
                "بررسی وضعیت و پاسخ‌دهی بات.\n\n"

                f"**{PREFIX}help**\n"
                "نمایش راهنمای NEXORA.\n\n"

                "برای مشاهده قابلیت‌های مختلف "
                "از دکمه‌های این پنل استفاده کنید."
            ),
            color=discord.Color.green()
        )

        embed.set_footer(
            text="NEXORA USER SYSTEM"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=HelpView()
        )


    @discord.ui.button(
        label="General",
        emoji="📋",
        style=discord.ButtonStyle.secondary
    )
    async def general_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        embed = discord.Embed(
            title="📋 NEXORA GENERAL",
            description=(
                f"**{PREFIX}ping**\n"
                "بررسی آنلاین بودن بات.\n\n"

                f"**{PREFIX}help**\n"
                "نمایش راهنمای کاربران.\n\n"

                f"**{PREFIX}adminhelp**\n"
                "نمایش راهنمای مخصوص مدیران.\n\n"

                "🤖 NEXORA یک بات چندمنظوره برای "
                "مدیریت، سرگرمی و امکانات سرور است."
            ),
            color=discord.Color.blurple()
        )

        embed.set_footer(
            text="NEXORA BOT"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=HelpView()
        )


# =========================================================
# ADMIN HELP VIEW
# =========================================================

class AdminHelpView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=180)


    @discord.ui.button(
        label="Moderation",
        emoji="🛡️",
        style=discord.ButtonStyle.danger
    )
    async def moderation_admin(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ این بخش فقط برای Administratorهاست.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="🛡️ NEXORA ADMIN • MODERATION",
            description=(
                "دستورات مدیریتی NEXORA در این بخش قرار می‌گیرند.\n\n"

                "🔨 مدیریت کاربران\n"
                "⚠️ مدیریت تخلفات\n"
                "🧹 مدیریت پیام‌ها\n"
                "🔒 کنترل کانال‌ها\n\n"

                "دستورات دقیق Moderation با تکمیل "
                "سیستم مدیریتی به این بخش اضافه خواهند شد."
            ),
            color=discord.Color.red()
        )

        embed.set_footer(
            text="NEXORA ADMIN SYSTEM"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=AdminHelpView()
        )


    @discord.ui.button(
        label="Ticket",
        emoji="🎫",
        style=discord.ButtonStyle.primary
    )
    async def ticket_admin(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ این بخش فقط برای Administratorهاست.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="🎫 NEXORA ADMIN • TICKET",
            description=(
                f"**{PREFIX}ticketpanel**\n"
                "ارسال پنل Ticket در کانال موردنظر.\n\n"

                "پنل شامل سیستم‌های:\n"
                "🛒 خرید\n"
                "❓ سوال\n"
                "⚠️ مشکلات سرور"
            ),
            color=discord.Color.blue()
        )

        embed.set_footer(
            text="NEXORA TICKET ADMIN"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=AdminHelpView()
        )


    @discord.ui.button(
        label="Giveaway",
        emoji="🎁",
        style=discord.ButtonStyle.primary
    )
    async def giveaway_admin(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ این بخش فقط برای Administratorهاست.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="🎁 NEXORA ADMIN • GIVEAWAY",
            description=(
                f"**{PREFIX}gstart**\n"
                "شروع Giveaway جدید.\n\n"

                "سیستم Giveaway برای برگزاری مسابقه، "
                "جمع‌آوری شرکت‌کنندگان و انتخاب برنده "
                "استفاده می‌شود."
            ),
            color=discord.Color.gold()
        )

        embed.set_footer(
            text="NEXORA GIVEAWAY ADMIN"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=AdminHelpView()
        )


    @discord.ui.button(
        label="Logs",
        emoji="📋",
        style=discord.ButtonStyle.secondary
    )
    async def logs_admin(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ این بخش فقط برای Administratorهاست.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="📋 NEXORA ADMIN • LOGS",
            description=(
                "سیستم Logs فعالیت‌های مهم سرور را "
                "ثبت می‌کند.\n\n"

                "👤 ورود و خروج کاربران\n"
                "🛡️ اقدامات مدیریتی\n"
                "🎫 فعالیت‌های Ticket\n"
                "⚙️ رویدادهای مهم بات"
            ),
            color=discord.Color.orange()
        )

        embed.set_footer(
            text="NEXORA LOG SYSTEM"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=AdminHelpView()
        )


    @discord.ui.button(
        label="Welcome",
        emoji="👋",
        style=discord.ButtonStyle.success
    )
    async def welcome_admin(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ این بخش فقط برای Administratorهاست.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="👋 NEXORA ADMIN • WELCOME",
            description=(
                "سیستم Welcome و Leave برای مدیریت "
                "پیام‌های ورود و خروج اعضای سرور استفاده می‌شود.\n\n"

                "🎉 Welcome Message\n"
                "👋 Leave Message"
            ),
            color=discord.Color.green()
        )

        embed.set_footer(
            text="NEXORA WELCOME SYSTEM"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=AdminHelpView()
        )


    @discord.ui.button(
        label="Auto Role",
        emoji="🎭",
        style=discord.ButtonStyle.secondary
    )
    async def autorole_admin(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message(
                "❌ این بخش فقط برای Administratorهاست.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="🎭 NEXORA ADMIN • AUTO ROLE",
            description=(
                "سیستم Auto Role به اعضای جدید "
                "به‌صورت خودکار Role اختصاص می‌دهد."
            ),
            color=discord.Color.purple()
        )

        embed.set_footer(
            text="NEXORA AUTOROLE SYSTEM"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=AdminHelpView()
        )


# =========================================================
# HELP COG
# =========================================================

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # =====================================================
    # USER HELP
    # =====================================================

    @commands.command(name="help")
    async def help_command(self, ctx):

        embed = discord.Embed(
            title="🤖 NEXORA BOT",
            description=(
                "به **NEXORA BOT** خوش آمدید.\n\n"
                "برای مشاهده راهنمای هر بخش، "
                "از دکمه‌های زیر استفاده کنید.\n\n"

                "🎵 **Music**\n"
                "پخش موزیک در Voice Channel\n\n"

                "🎫 **Ticket**\n"
                "سیستم پشتیبانی و تیکت\n\n"

                "🎁 **Giveaway**\n"
                "برگزاری Giveaway\n\n"

                "🛡️ **Moderation**\n"
                "ابزارهای مدیریت سرور"
            ),
            color=discord.Color.blurple()
        )

        embed.set_footer(
            text="NEXORA • Smart. Powerful. Ready."
        )

        await ctx.send(
            embed=embed,
            view=HelpView()
        )


    # =====================================================
    # ADMIN HELP
    # =====================================================

    @commands.command(name="adminhelp")
    @commands.has_permissions(administrator=True)
    async def admin_help_command(self, ctx):

        embed = discord.Embed(
            title="👑 NEXORA ADMIN HELP",
            description=(
                "راهنمای مخصوص مدیران سرور.\n\n"

                "در این پنل می‌توانید راهنمای سیستم‌های "
                "مدیریتی NEXORA را مشاهده کنید.\n\n"

                "🛡️ Moderation\n"
                "🎫 Ticket Management\n"
                "🎁 Giveaway\n"
                "📋 Logs\n"
                "👋 Welcome / Leave\n"
                "🎭 Auto Role"
            ),
            color=discord.Color.gold()
        )

        embed.set_footer(
            text="NEXORA ADMIN SYSTEM"
        )

        await ctx.send(
            embed=embed,
            view=AdminHelpView()
        )


    # =====================================================
    # ADMIN PERMISSION ERROR
    # =====================================================

    @admin_help_command.error
    async def admin_help_error(self, ctx, error):

        if isinstance(
            error,
            commands.MissingPermissions
        ):

            await ctx.send(
                "❌ این دستور فقط برای Administratorها قابل استفاده است."
            )


# =========================================================
# SETUP
# =========================================================

async def setup(bot):

    await bot.add_cog(
        Help(bot)
    )