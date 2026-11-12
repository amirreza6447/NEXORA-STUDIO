import discord
from discord.ext import commands

from settings import (
    get_guild_settings,
    set_setting
)


print("SETTINGS MODULE LOADED")


# =========================================================
# WELCOME SETTINGS
# =========================================================

class WelcomeSettingsView(discord.ui.View):

    def __init__(self):

        super().__init__(
            timeout=300
        )


    @discord.ui.select(
        cls=discord.ui.ChannelSelect,
        channel_types=[discord.ChannelType.text],
        placeholder="📢 انتخاب کانال Welcome",
        min_values=1,
        max_values=1
    )
    async def welcome_channel(
        self,
        interaction,
        select
    ):

        channel = select.values[0]


        set_setting(
            interaction.guild.id,
            "welcome",
            "channel_id",
            channel.id
        )


        await interaction.response.send_message(
            f"✅ کانال Welcome تنظیم شد:\n"
            f"{channel.mention}",
            ephemeral=True
        )


    @discord.ui.button(
        label="🟢 فعال",
        style=discord.ButtonStyle.green
    )
    async def enable_welcome(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "welcome",
            "enabled",
            True
        )


        await interaction.response.send_message(
            "✅ سیستم Welcome فعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔴 غیرفعال",
        style=discord.ButtonStyle.red
    )
    async def disable_welcome(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "welcome",
            "enabled",
            False
        )


        await interaction.response.send_message(
            "🔴 سیستم Welcome غیرفعال شد.",
            ephemeral=True
        )


# =========================================================
# LEAVE SETTINGS
# =========================================================

class LeaveSettingsView(discord.ui.View):

    def __init__(self):

        super().__init__(
            timeout=300
        )


    @discord.ui.select(
        cls=discord.ui.ChannelSelect,
        channel_types=[discord.ChannelType.text],
        placeholder="📢 انتخاب کانال Leave",
        min_values=1,
        max_values=1
    )
    async def leave_channel(
        self,
        interaction,
        select
    ):

        channel = select.values[0]


        set_setting(
            interaction.guild.id,
            "leave",
            "channel_id",
            channel.id
        )


        await interaction.response.send_message(
            f"✅ کانال Leave تنظیم شد:\n"
            f"{channel.mention}",
            ephemeral=True
        )


    @discord.ui.button(
        label="🟢 فعال",
        style=discord.ButtonStyle.green
    )
    async def enable_leave(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "leave",
            "enabled",
            True
        )


        await interaction.response.send_message(
            "✅ سیستم Leave فعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔴 غیرفعال",
        style=discord.ButtonStyle.red
    )
    async def disable_leave(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "leave",
            "enabled",
            False
        )


        await interaction.response.send_message(
            "🔴 سیستم Leave غیرفعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔄 وضعیت",
        style=discord.ButtonStyle.blurple
    )
    async def leave_status(
        self,
        interaction,
        button
    ):

        settings = get_guild_settings(
            interaction.guild.id
        )


        data = settings.get(
            "leave",
            {}
        )


        channel_id = data.get(
            "channel_id"
        )


        if channel_id:

            channel = interaction.guild.get_channel(
                channel_id
            )


            channel_text = (
                channel.mention
                if channel
                else f"`{channel_id}`"
            )

        else:

            channel_text = (
                "❌ تنظیم نشده"
            )


        status = (
            "🟢 فعال"
            if data.get(
                "enabled",
                True
            )
            else "🔴 غیرفعال"
        )


        await interaction.response.send_message(
            "🚪 **LEAVE STATUS**\n\n"
            f"وضعیت: {status}\n"
            f"کانال: {channel_text}",
            ephemeral=True
        )


# =========================================================
# AUTOROLE SETTINGS
# =========================================================

class AutoRoleSettingsView(discord.ui.View):

    def __init__(self):

        super().__init__(
            timeout=300
        )


    @discord.ui.select(
        cls=discord.ui.RoleSelect,
        placeholder="👤 انتخاب Member Role",
        min_values=1,
        max_values=1
    )
    async def member_role(
        self,
        interaction,
        select
    ):

        role = select.values[0]


        set_setting(
            interaction.guild.id,
            "autorole",
            "member_role_id",
            role.id
        )


        await interaction.response.send_message(
            f"✅ Member Role تنظیم شد:\n"
            f"{role.mention}",
            ephemeral=True
        )


    @discord.ui.select(
        cls=discord.ui.RoleSelect,
        placeholder="🤖 انتخاب Bot Role",
        min_values=1,
        max_values=1
    )
    async def bot_role(
        self,
        interaction,
        select
    ):

        role = select.values[0]


        set_setting(
            interaction.guild.id,
            "autorole",
            "bot_role_id",
            role.id
        )


        await interaction.response.send_message(
            f"✅ Bot Role تنظیم شد:\n"
            f"{role.mention}",
            ephemeral=True
        )


    @discord.ui.button(
        label="🟢 فعال",
        style=discord.ButtonStyle.green,
        row=2
    )
    async def enable_autorole(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "autorole",
            "enabled",
            True
        )


        await interaction.response.send_message(
            "✅ سیستم Auto Role فعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔴 غیرفعال",
        style=discord.ButtonStyle.red,
        row=2
    )
    async def disable_autorole(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "autorole",
            "enabled",
            False
        )


        await interaction.response.send_message(
            "🔴 سیستم Auto Role غیرفعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔄 وضعیت",
        style=discord.ButtonStyle.blurple,
        row=2
    )
    async def autorole_status(
        self,
        interaction,
        button
    ):

        settings = get_guild_settings(
            interaction.guild.id
        )


        data = settings.get(
            "autorole",
            {}
        )


        member_role_id = data.get(
            "member_role_id"
        )


        bot_role_id = data.get(
            "bot_role_id"
        )


        if member_role_id:

            role = interaction.guild.get_role(
                member_role_id
            )


            member_text = (
                role.mention
                if role
                else f"`{member_role_id}`"
            )

        else:

            member_text = (
                "❌ تنظیم نشده"
            )


        if bot_role_id:

            role = interaction.guild.get_role(
                bot_role_id
            )


            bot_text = (
                role.mention
                if role
                else f"`{bot_role_id}`"
            )

        else:

            bot_text = (
                "❌ تنظیم نشده"
            )


        status = (
            "🟢 فعال"
            if data.get(
                "enabled",
                True
            )
            else "🔴 غیرفعال"
        )


        await interaction.response.send_message(
            "🎭 **AUTOROLE STATUS**\n\n"
            f"وضعیت: {status}\n\n"
            f"👤 Member Role: {member_text}\n"
            f"🤖 Bot Role: {bot_text}",
            ephemeral=True
        )


# =========================================================
# LOGS SETTINGS
# =========================================================

class LogsSettingsView(discord.ui.View):

    def __init__(self):

        super().__init__(
            timeout=300
        )


    @discord.ui.select(
        cls=discord.ui.ChannelSelect,
        channel_types=[discord.ChannelType.text],
        placeholder="📋 انتخاب کانال Logs",
        min_values=1,
        max_values=1
    )
    async def logs_channel(
        self,
        interaction,
        select
    ):

        channel = select.values[0]


        set_setting(
            interaction.guild.id,
            "logs",
            "channel_id",
            channel.id
        )


        await interaction.response.send_message(
            f"✅ کانال Logs تنظیم شد:\n"
            f"{channel.mention}",
            ephemeral=True
        )


    @discord.ui.button(
        label="🟢 فعال",
        style=discord.ButtonStyle.green,
        row=1
    )
    async def enable_logs(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "logs",
            "enabled",
            True
        )


        await interaction.response.send_message(
            "✅ سیستم Logs فعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔴 غیرفعال",
        style=discord.ButtonStyle.red,
        row=1
    )
    async def disable_logs(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "logs",
            "enabled",
            False
        )


        await interaction.response.send_message(
            "🔴 سیستم Logs غیرفعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔄 وضعیت",
        style=discord.ButtonStyle.blurple,
        row=1
    )
    async def logs_status(
        self,
        interaction,
        button
    ):

        settings = get_guild_settings(
            interaction.guild.id
        )


        data = settings.get(
            "logs",
            {}
        )


        channel_id = data.get(
            "channel_id"
        )


        if channel_id:

            channel = interaction.guild.get_channel(
                channel_id
            )


            channel_text = (
                channel.mention
                if channel
                else f"`{channel_id}`"
            )

        else:

            channel_text = (
                "❌ تنظیم نشده"
            )


        status = (
            "🟢 فعال"
            if data.get(
                "enabled",
                True
            )
            else "🔴 غیرفعال"
        )


        await interaction.response.send_message(
            "📋 **LOGS STATUS**\n\n"
            f"وضعیت: {status}\n"
            f"کانال: {channel_text}",
            ephemeral=True
        )


# =========================================================
# TICKET SUPPORT ROLE SELECT
# =========================================================

class SupportRoleSelect(discord.ui.RoleSelect):

    def __init__(self):

        super().__init__(
            placeholder="🎭 انتخاب Support Role",
            min_values=1,
            max_values=1,
            row=0
        )


    async def callback(
        self,
        interaction
    ):

        try:

            role = self.values[0]


            set_setting(
                interaction.guild.id,
                "ticket",
                "support_role_id",
                role.id
            )


            await interaction.response.send_message(
                f"✅ Support Role تنظیم شد:\n"
                f"{role.mention}",
                ephemeral=True
            )


        except Exception as e:

            print(
                "❌ SUPPORT ROLE CALLBACK ERROR:",
                e
            )


            if not interaction.response.is_done():

                await interaction.response.send_message(
                    "❌ هنگام تنظیم Support Role خطایی رخ داد.",
                    ephemeral=True
                )


# =========================================================
# TICKET CATEGORY SELECT
# =========================================================

class TicketCategorySelect(discord.ui.Select):

    def __init__(
        self,
        guild
    ):

        options = []


        for category in guild.categories[:25]:

            options.append(
                discord.SelectOption(
                    label=category.name[:100],
                    value=str(category.id),
                    emoji="📂"
                )
            )


        if not options:

            options.append(
                discord.SelectOption(
                    label="هیچ Category وجود ندارد",
                    value="none",
                    emoji="❌"
                )
            )


        super().__init__(
            placeholder="📂 انتخاب Ticket Category",
            min_values=1,
            max_values=1,
            options=options,
            row=1
        )


    async def callback(
        self,
        interaction
    ):

        value = self.values[0]


        if value == "none":

            await interaction.response.send_message(
                "❌ هیچ Categoryای در سرور وجود ندارد.",
                ephemeral=True
            )

            return


        try:

            category_id = int(
                value
            )


            category = interaction.guild.get_channel(
                category_id
            )


            if category is None:

                await interaction.response.send_message(
                    "❌ Category پیدا نشد.",
                    ephemeral=True
                )

                return


            set_setting(
                interaction.guild.id,
                "ticket",
                "category_id",
                category.id
            )


            await interaction.response.send_message(
                f"✅ Ticket Category تنظیم شد:\n"
                f"📂 **{category.name}**",
                ephemeral=True
            )


        except Exception as e:

            print(
                "❌ CATEGORY CALLBACK ERROR:",
                e
            )


            if not interaction.response.is_done():

                await interaction.response.send_message(
                    "❌ هنگام تنظیم Category خطایی رخ داد.",
                    ephemeral=True
                )


# =========================================================
# TICKET SETTINGS
# =========================================================

class TicketSettingsView(discord.ui.View):

    def __init__(
        self,
        guild
    ):

        super().__init__(
            timeout=300
        )


        self.add_item(
            SupportRoleSelect()
        )


        self.add_item(
            TicketCategorySelect(
                guild
            )
        )


    @discord.ui.button(
        label="🟢 فعال",
        style=discord.ButtonStyle.green,
        row=2
    )
    async def enable_ticket(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "ticket",
            "enabled",
            True
        )


        await interaction.response.send_message(
            "✅ سیستم Ticket فعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔴 غیرفعال",
        style=discord.ButtonStyle.red,
        row=2
    )
    async def disable_ticket(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "ticket",
            "enabled",
            False
        )


        await interaction.response.send_message(
            "🔴 سیستم Ticket غیرفعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔄 وضعیت",
        style=discord.ButtonStyle.blurple,
        row=2
    )
    async def ticket_status(
        self,
        interaction,
        button
    ):

        settings = get_guild_settings(
            interaction.guild.id
        )


        data = settings.get(
            "ticket",
            {}
        )


        support_role_id = data.get(
            "support_role_id"
        )


        category_id = data.get(
            "category_id"
        )


        if support_role_id:

            role = interaction.guild.get_role(
                support_role_id
            )


            role_text = (
                role.mention
                if role
                else f"`{support_role_id}`"
            )

        else:

            role_text = (
                "❌ تنظیم نشده"
            )


        if category_id:

            category = interaction.guild.get_channel(
                category_id
            )


            category_text = (
                f"📂 **{category.name}**"
                if category
                else f"`{category_id}`"
            )

        else:

            category_text = (
                "❌ تنظیم نشده"
            )


        status = (
            "🟢 فعال"
            if data.get(
                "enabled",
                True
            )
            else "🔴 غیرفعال"
        )


        await interaction.response.send_message(
            "🎫 **TICKET STATUS**\n\n"
            f"وضعیت: {status}\n"
            f"🎭 Support Role: {role_text}\n"
            f"📂 Category: {category_text}",
            ephemeral=True
        )


# =========================================================
# GIVEAWAY SETTINGS
# =========================================================

class GiveawaySettingsView(discord.ui.View):

    def __init__(self):

        super().__init__(
            timeout=300
        )


    @discord.ui.select(
        cls=discord.ui.ChannelSelect,
        channel_types=[discord.ChannelType.text],
        placeholder="🎁 انتخاب کانال Giveaway",
        min_values=1,
        max_values=1
    )
    async def giveaway_channel(
        self,
        interaction,
        select
    ):

        channel = select.values[0]


        set_setting(
            interaction.guild.id,
            "giveaway",
            "channel_id",
            channel.id
        )


        await interaction.response.send_message(
            f"✅ کانال Giveaway تنظیم شد:\n"
            f"{channel.mention}",
            ephemeral=True
        )


    @discord.ui.button(
        label="🟢 فعال",
        style=discord.ButtonStyle.green,
        row=1
    )
    async def enable_giveaway(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "giveaway",
            "enabled",
            True
        )


        await interaction.response.send_message(
            "✅ سیستم Giveaway فعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔴 غیرفعال",
        style=discord.ButtonStyle.red,
        row=1
    )
    async def disable_giveaway(
        self,
        interaction,
        button
    ):

        set_setting(
            interaction.guild.id,
            "giveaway",
            "enabled",
            False
        )


        await interaction.response.send_message(
            "🔴 سیستم Giveaway غیرفعال شد.",
            ephemeral=True
        )


    @discord.ui.button(
        label="🔄 وضعیت",
        style=discord.ButtonStyle.blurple,
        row=1
    )
    async def giveaway_status(
        self,
        interaction,
        button
    ):

        settings = get_guild_settings(
            interaction.guild.id
        )


        data = settings.get(
            "giveaway",
            {}
        )


        channel_id = data.get(
            "channel_id"
        )


        if channel_id:

            channel = interaction.guild.get_channel(
                channel_id
            )


            channel_text = (
                channel.mention
                if channel
                else f"`{channel_id}`"
            )

        else:

            channel_text = (
                "❌ تنظیم نشده"
            )


        status = (
            "🟢 فعال"
            if data.get(
                "enabled",
                True
            )
            else "🔴 غیرفعال"
        )


        await interaction.response.send_message(
            "🎁 **GIVEAWAY STATUS**\n\n"
            f"وضعیت: {status}\n"
            f"کانال: {channel_text}",
            ephemeral=True
        )


# =========================================================
# MAIN SETTINGS PANEL
# =========================================================

class SettingsView(discord.ui.View):

    def __init__(self):

        super().__init__(
            timeout=300
        )


    # =====================================================
    # WELCOME
    # =====================================================

    @discord.ui.button(
        label="👋 Welcome",
        style=discord.ButtonStyle.blurple,
        row=0
    )
    async def welcome(
        self,
        interaction,
        button
    ):

        embed = discord.Embed(
            title="👋 NEXORA | Welcome Settings",
            description=(
                "📢 انتخاب کانال Welcome\n"
                "🟢 فعال کردن\n"
                "🔴 غیرفعال کردن"
            ),
            color=discord.Color.purple()
        )


        await interaction.response.send_message(
            embed=embed,
            view=WelcomeSettingsView(),
            ephemeral=True
        )


    # =====================================================
    # LEAVE
    # =====================================================

    @discord.ui.button(
        label="🚪 Leave",
        style=discord.ButtonStyle.blurple,
        row=0
    )
    async def leave(
        self,
        interaction,
        button
    ):

        embed = discord.Embed(
            title="🚪 NEXORA | Leave Settings",
            description=(
                "📢 انتخاب کانال Leave\n"
                "🟢 فعال کردن\n"
                "🔴 غیرفعال کردن\n"
                "🔄 مشاهده وضعیت"
            ),
            color=discord.Color.purple()
        )


        await interaction.response.send_message(
            embed=embed,
            view=LeaveSettingsView(),
            ephemeral=True
        )


    # =====================================================
    # AUTOROLE
    # =====================================================

    @discord.ui.button(
        label="🎭 Auto Role",
        style=discord.ButtonStyle.blurple,
        row=0
    )
    async def autorole(
        self,
        interaction,
        button
    ):

        embed = discord.Embed(
            title="🎭 NEXORA | Auto Role Settings",
            description=(
                "👤 Member Role\n"
                "🤖 Bot Role\n"
                "🟢 فعال کردن\n"
                "🔴 غیرفعال کردن\n"
                "🔄 مشاهده وضعیت"
            ),
            color=discord.Color.purple()
        )


        await interaction.response.send_message(
            embed=embed,
            view=AutoRoleSettingsView(),
            ephemeral=True
        )


    # =====================================================
    # LOGS
    # =====================================================

    @discord.ui.button(
        label="📋 Logs",
        style=discord.ButtonStyle.blurple,
        row=1
    )
    async def logs(
        self,
        interaction,
        button
    ):

        embed = discord.Embed(
            title="📋 NEXORA | Logs Settings",
            description=(
                "📋 انتخاب کانال Logs\n"
                "🟢 فعال کردن\n"
                "🔴 غیرفعال کردن\n"
                "🔄 مشاهده وضعیت"
            ),
            color=discord.Color.purple()
        )


        await interaction.response.send_message(
            embed=embed,
            view=LogsSettingsView(),
            ephemeral=True
        )


    # =====================================================
    # TICKET
    # =====================================================

    @discord.ui.button(
        label="🎫 Ticket",
        style=discord.ButtonStyle.blurple,
        row=1
    )
    async def ticket(
        self,
        interaction,
        button
    ):

        embed = discord.Embed(
            title="🎫 NEXORA | Ticket Settings",
            description=(
                "تنظیمات سیستم Ticket\n\n"
                "🎭 انتخاب Support Role\n"
                "📂 انتخاب Ticket Category\n"
                "🟢 فعال کردن\n"
                "🔴 غیرفعال کردن\n"
                "🔄 مشاهده وضعیت"
            ),
            color=discord.Color.purple()
        )


        await interaction.response.send_message(
            embed=embed,
            view=TicketSettingsView(
                interaction.guild
            ),
            ephemeral=True
        )


    # =====================================================
    # GIVEAWAY
    # =====================================================

    @discord.ui.button(
        label="🎁 Giveaway",
        style=discord.ButtonStyle.blurple,
        row=1
    )
    async def giveaway(
        self,
        interaction,
        button
    ):

        embed = discord.Embed(
            title="🎁 NEXORA | Giveaway Settings",
            description=(
                "تنظیمات سیستم Giveaway\n\n"
                "🎁 انتخاب کانال Giveaway\n"
                "🟢 فعال کردن\n"
                "🔴 غیرفعال کردن\n"
                "🔄 مشاهده وضعیت"
            ),
            color=discord.Color.purple()
        )


        await interaction.response.send_message(
            embed=embed,
            view=GiveawaySettingsView(),
            ephemeral=True
        )


    # =====================================================
    # REFRESH
    # =====================================================

    @discord.ui.button(
        label="🔄 Refresh",
        style=discord.ButtonStyle.green,
        row=2
    )
    async def refresh(
        self,
        interaction,
        button
    ):

        settings = get_guild_settings(
            interaction.guild.id
        )


        welcome = settings.get(
            "welcome",
            {}
        )

        leave = settings.get(
            "leave",
            {}
        )

        autorole = settings.get(
            "autorole",
            {}
        )

        logs = settings.get(
            "logs",
            {}
        )

        ticket = settings.get(
            "ticket",
            {}
        )

        giveaway = settings.get(
            "giveaway",
            {}
        )


        await interaction.response.send_message(
            "⚙️ **NEXORA CURRENT SETTINGS**\n\n"
            f"👋 Welcome: "
            f"`{welcome.get('enabled', True)}`\n"

            f"🚪 Leave: "
            f"`{leave.get('enabled', True)}`\n"

            f"🎭 Auto Role: "
            f"`{autorole.get('enabled', True)}`\n"

            f"📋 Logs: "
            f"`{logs.get('enabled', True)}`\n"

            f"🎫 Ticket: "
            f"`{ticket.get('enabled', True)}`\n"

            f"🎁 Giveaway: "
            f"`{giveaway.get('enabled', True)}`",
            ephemeral=True
        )


# =========================================================
# SETTINGS COG
# =========================================================

class Settings(commands.Cog):

    def __init__(
        self,
        bot
    ):

        self.bot = bot


    @commands.command()
    @commands.has_permissions(
        administrator=True
    )
    async def settings(
        self,
        ctx
    ):

        # ایجاد تنظیمات مخصوص همین سرور
        get_guild_settings(
            ctx.guild.id
        )


        embed = discord.Embed(
            title="⚙️ NEXORA SERVER SETTINGS",
            description=(
                "از دکمه‌های زیر برای مدیریت سیستم‌های NEXORA استفاده کنید.\n\n"
                "🔐 فقط Administrator می‌تواند این پنل را استفاده کند.\n\n"
                f"🏠 Server: **{ctx.guild.name}**"
            ),
            color=discord.Color.purple()
        )


        embed.set_footer(
            text=(
                f"NEXORA Server Management | "
                f"Server ID: {ctx.guild.id}"
            )
        )


        await ctx.send(
            embed=embed,
            view=SettingsView()
        )


    @settings.error
    async def settings_error(
        self,
        ctx,
        error
    ):

        if isinstance(
            error,
            commands.MissingPermissions
        ):

            await ctx.send(
                "❌ شما دسترسی Administrator ندارید."
            )


# =========================================================
# SETUP
# =========================================================

async def setup(bot):

    await bot.add_cog(
        Settings(bot)
    )