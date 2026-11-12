import discord
from discord.ext import commands

from settings import get_all_settings


print("TICKET MODULE LOADED - SETTINGS VERSION")


# =========================================================
# CLOSE TICKET VIEW
# =========================================================

class TicketCloseView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)


    @discord.ui.button(
        label="🔒 بستن تیکت",
        style=discord.ButtonStyle.red,
        custom_id="close_ticket_button"
    )
    async def close_ticket(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        settings = get_all_settings()

        ticket_settings = settings.get(
            "ticket",
            {}
        )


        support_role_id = ticket_settings.get(
            "support_role_id"
        )


        support_role = None


        if support_role_id:

            support_role = interaction.guild.get_role(
                support_role_id
            )


        is_support = (
            support_role
            and support_role in interaction.user.roles
        )


        is_admin = (
            interaction.user.guild_permissions.administrator
        )


        if not is_support and not is_admin:

            await interaction.response.send_message(
                "❌ شما دسترسی بستن تیکت را ندارید.",
                ephemeral=True
            )

            return


        await interaction.response.send_message(
            "🔒 تیکت بسته شد."
        )


        await interaction.channel.delete()


# =========================================================
# TICKET VIEW
# =========================================================

class TicketView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=None)


        self.add_item(
            discord.ui.Button(
                label="🛒 خرید",
                style=discord.ButtonStyle.green,
                custom_id="ticket_buy"
            )
        )


        self.add_item(
            discord.ui.Button(
                label="❓ سوال",
                style=discord.ButtonStyle.blurple,
                custom_id="ticket_question"
            )
        )


        self.add_item(
            discord.ui.Button(
                label="🛠 مشکل سرور",
                style=discord.ButtonStyle.gray,
                custom_id="ticket_server"
            )
        )


    async def interaction_check(
        self,
        interaction: discord.Interaction
    ):

        custom_id = interaction.data["custom_id"]


        if custom_id == "ticket_buy":

            await self.create_ticket(
                interaction,
                "خرید",
                "buy"
            )


        elif custom_id == "ticket_question":

            await self.create_ticket(
                interaction,
                "سوال",
                "question"
            )


        elif custom_id == "ticket_server":

            await self.create_ticket(
                interaction,
                "مشکل سرور",
                "server"
            )


        return True


    async def create_ticket(
        self,
        interaction,
        ticket_type,
        ticket_name
    ):

        guild = interaction.guild
        user = interaction.user


        # =================================================
        # LOAD SETTINGS
        # =================================================

        settings = get_all_settings()

        ticket_settings = settings.get(
            "ticket",
            {}
        )


        enabled = ticket_settings.get(
            "enabled",
            True
        )


        support_role_id = ticket_settings.get(
            "support_role_id"
        )


        category_id = ticket_settings.get(
            "category_id"
        )


        # =================================================
        # CHECK ENABLED
        # =================================================

        if not enabled:

            await interaction.response.send_message(
                "🔴 سیستم Ticket در حال حاضر غیرفعال است.",
                ephemeral=True
            )

            return


        # =================================================
        # CHANNEL NAME
        # =================================================

        safe_name = user.name.lower()

        channel_name = (
            f"ticket-{ticket_name}-{safe_name}"
        )


        existing = discord.utils.get(
            guild.text_channels,
            name=channel_name
        )


        if existing:

            await interaction.response.send_message(
                "❌ شما یک تیکت باز دارید.",
                ephemeral=True
            )

            return


        # =================================================
        # SUPPORT ROLE
        # =================================================

        support_role = None


        if support_role_id:

            support_role = guild.get_role(
                support_role_id
            )


        # =================================================
        # CATEGORY
        # =================================================

        category = None


        if category_id:

            category = guild.get_channel(
                category_id
            )


            if category and not isinstance(
                category,
                discord.CategoryChannel
            ):

                category = None


        # =================================================
        # PERMISSIONS
        # =================================================

        overwrites = {

            guild.default_role:
                discord.PermissionOverwrite(
                    view_channel=False
                ),

            user:
                discord.PermissionOverwrite(
                    view_channel=True,
                    send_messages=True,
                    read_message_history=True
                )

        }


        if support_role:

            overwrites[support_role] = (
                discord.PermissionOverwrite(
                    view_channel=True,
                    send_messages=True,
                    read_message_history=True
                )
            )


        # =================================================
        # CREATE CHANNEL
        # =================================================

        try:

            channel = await guild.create_text_channel(

                name=channel_name,

                category=category,

                overwrites=overwrites,

                reason="NEXORA Ticket System"

            )


        except discord.Forbidden:

            await interaction.response.send_message(
                "❌ بات دسترسی ساخت کانال Ticket را ندارد.",
                ephemeral=True
            )

            return


        except Exception as e:

            print(
                "❌ TICKET CREATE ERROR:",
                e
            )

            await interaction.response.send_message(
                "❌ هنگام ساخت تیکت خطایی رخ داد.",
                ephemeral=True
            )

            return


        # =================================================
        # EMBED
        # =================================================

        embed = discord.Embed(

            title=f"🎫 NEXORA | {ticket_type}",

            description=(

                f"سلام {user.mention} 👋\n\n"

                f"نوع درخواست: **{ticket_type}**\n\n"

                "لطفاً درخواست خود را کامل توضیح دهید.\n"

                "پشتیبانی در اسرع وقت پاسخ می‌دهد.\n\n"

                "برای بستن تیکت از دکمه زیر استفاده کنید 🔒"

            ),

            color=discord.Color.blurple()

        )


        embed.set_footer(
            text="NEXORA Ticket System"
        )


        # =================================================
        # CONTENT
        # =================================================

        if support_role:

            content = (
                f"{user.mention} "
                f"{support_role.mention}"
            )

        else:

            content = user.mention


        # =================================================
        # SEND TICKET MESSAGE
        # =================================================

        await channel.send(

            content=content,

            embed=embed,

            view=TicketCloseView()

        )


        # =================================================
        # RESPONSE
        # =================================================

        await interaction.response.send_message(

            f"✅ تیکت ساخته شد: {channel.mention}",

            ephemeral=True

        )


# =========================================================
# TICKET COG
# =========================================================

class Ticket(commands.Cog):

    def __init__(self, bot):

        self.bot = bot


    @commands.command()
    @commands.has_permissions(
        administrator=True
    )
    async def ticketpanel(self, ctx):

        settings = get_all_settings()

        ticket_settings = settings.get(
            "ticket",
            {}
        )


        if not ticket_settings.get(
            "enabled",
            True
        ):

            await ctx.send(
                "🔴 سیستم Ticket غیرفعال است."
            )

            return


        embed = discord.Embed(

            title="🎮 NEXORA SUPPORT",

            description=(

                "برای ارتباط با پشتیبانی یکی از گزینه‌ها را انتخاب کنید:\n\n"

                "🛒 خرید\n"
                "❓ سوال\n"
                "🛠 مشکل سرور"

            ),

            color=discord.Color.blurple()

        )


        embed.set_footer(
            text="NEXORA Support System"
        )


        view = TicketView()


        print(
            "BUTTON COUNT:",
            len(view.children)
        )


        await ctx.send(

            embed=embed,

            view=view

        )


    @ticketpanel.error
    async def ticketpanel_error(
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
        Ticket(bot)
    )