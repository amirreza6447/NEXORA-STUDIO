import discord
from discord.ext import commands
from datetime import timedelta

from modules.logs import create_log

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # =========================
    # KICK
    # =========================

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):

        if member == ctx.author:
            await ctx.send("❌ You can't kick yourself.")
            return

        if member.top_role >= ctx.author.top_role:
            await ctx.send(
                "❌ You can't kick a member with an equal or higher role."
            )
            return

        if member.top_role >= ctx.guild.me.top_role:
            await ctx.send(
                "❌ I can't kick this member because their role is higher than mine."
            )
            return

        try:
            await member.kick(reason=reason)

            await create_log(
    self.bot,
    ctx.guild,
    "🛡️ Kick Log",
    f"👤 User: {member.mention}\n"
    f"👮 Moderator: {ctx.author.mention}\n"
    f"📝 Reason: {reason}",
    discord.Color.red()
)

            embed = discord.Embed(
                title="🛡️ NEXORA MODERATION",
                color=discord.Color.red()
            )

            embed.add_field(
                name="👤 User",
                value=member.mention,
                inline=False
            )

            embed.add_field(
                name="🔨 Action",
                value="Kick",
                inline=True
            )

            embed.add_field(
                name="👮 Moderator",
                value=ctx.author.mention,
                inline=True
            )

            embed.add_field(
                name="📝 Reason",
                value=reason,
                inline=False
            )

            await ctx.send(embed=embed)

        except discord.Forbidden:
            await ctx.send(
                "❌ I don't have permission to kick this member."
            )


    # =========================
    # BAN
    # =========================

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):

        if member == ctx.author:
            await ctx.send("❌ You can't ban yourself.")
            return

        if member.top_role >= ctx.author.top_role:
            await ctx.send(
                "❌ You can't ban a member with an equal or higher role."
            )
            return

        if member.top_role >= ctx.guild.me.top_role:
            await ctx.send(
                "❌ I can't ban this member because their role is higher than mine."
            )
            return

        try:
            await member.ban(reason=reason)

            await create_log(
    self.bot,
    ctx.guild,
    "🔨 Ban Log",
    f"👤 User: {member}\n"
    f"🆔 ID: {member.id}\n"
    f"👮 Moderator: {ctx.author.mention}\n"
    f"📝 Reason: {reason}",
    discord.Color.dark_red()
)

            embed = discord.Embed(
                title="🛡️ NEXORA MODERATION",
                color=discord.Color.dark_red()
            )

            embed.add_field(
                name="👤 User",
                value=f"{member} ({member.id})",
                inline=False
            )

            embed.add_field(
                name="🔨 Action",
                value="Ban",
                inline=True
            )

            embed.add_field(
                name="👮 Moderator",
                value=ctx.author.mention,
                inline=True
            )

            embed.add_field(
                name="📝 Reason",
                value=reason,
                inline=False
            )

            await ctx.send(embed=embed)

        except discord.Forbidden:
            await ctx.send(
                "❌ I don't have permission to ban this member."
            )


    # =========================
    # UNBAN
    # =========================

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id: int):

        try:

            user = await self.bot.fetch_user(user_id)

            await ctx.guild.unban(user)

            await create_log(
    self.bot,
    ctx.guild,
    "✅ Unban Log",
    f"👤 User: {user}\n"
    f"🆔 ID: {user.id}\n"
    f"👮 Moderator: {ctx.author.mention}",
    discord.Color.green()
)

            embed = discord.Embed(
                title="🛡️ NEXORA MODERATION",
                color=discord.Color.green()
            )

            embed.add_field(
                name="👤 User",
                value=f"{user} ({user.id})",
                inline=False
            )

            embed.add_field(
                name="🔨 Action",
                value="Unban",
                inline=True
            )

            embed.add_field(
                name="👮 Moderator",
                value=ctx.author.mention,
                inline=True
            )

            await ctx.send(embed=embed)

        except discord.NotFound:
            await ctx.send(
                "❌ This user is not banned."
            )

        except discord.Forbidden:
            await ctx.send(
                "❌ I don't have permission to unban users."
            )


    # =========================
    # TIMEOUT
    # =========================

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def timeout(
        self,
        ctx,
        member: discord.Member,
        minutes: int,
        *,
        reason="No reason provided"
    ):

        if member == ctx.author:
            await ctx.send("❌ You can't timeout yourself.")
            return

        if member.top_role >= ctx.author.top_role:
            await ctx.send(
                "❌ You can't timeout a member with an equal or higher role."
            )
            return

        if member.top_role >= ctx.guild.me.top_role:
            await ctx.send(
                "❌ I can't timeout this member because their role is higher than mine."
            )
            return

        if minutes <= 0:
            await ctx.send(
                "❌ Timeout duration must be greater than 0."
            )
            return

        if minutes > 40320:
            await ctx.send(
                "❌ Maximum timeout duration is 28 days."
            )
            return

        try:

            duration = discord.utils.utcnow() + timedelta(
                minutes=minutes
            )

            await member.timeout(
                duration,
                reason=reason
            )

            await create_log(
    self.bot,
    ctx.guild,
    "⏳ Timeout Log",
    f"👤 User: {member.mention}\n"
    f"⏱️ Duration: {minutes} minutes\n"
    f"👮 Moderator: {ctx.author.mention}\n"
    f"📝 Reason: {reason}",
    discord.Color.orange()
)

            embed = discord.Embed(
                title="🛡️ NEXORA MODERATION",
                color=discord.Color.orange()
            )

            embed.add_field(
                name="👤 User",
                value=member.mention,
                inline=False
            )

            embed.add_field(
                name="🔨 Action",
                value=f"Timeout • {minutes} minutes",
                inline=True
            )

            embed.add_field(
                name="👮 Moderator",
                value=ctx.author.mention,
                inline=True
            )

            embed.add_field(
                name="📝 Reason",
                value=reason,
                inline=False
            )

            await ctx.send(embed=embed)

        except discord.Forbidden:
            await ctx.send(
                "❌ I don't have permission to timeout this member."
            )


    # =========================
    # UNTIMEOUT
    # =========================

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def untimeout(self, ctx, member: discord.Member):

        try:

            await member.timeout(None)

            await create_log(
    self.bot,
    ctx.guild,
    "🔓 Untimeout Log",
    f"👤 User: {member.mention}\n"
    f"👮 Moderator: {ctx.author.mention}",
    discord.Color.green()
)

            embed = discord.Embed(
                title="🛡️ NEXORA MODERATION",
                color=discord.Color.green()
            )

            embed.add_field(
                name="👤 User",
                value=member.mention,
                inline=False
            )

            embed.add_field(
                name="🔨 Action",
                value="Timeout Removed",
                inline=True
            )

            embed.add_field(
                name="👮 Moderator",
                value=ctx.author.mention,
                inline=True
            )

            await ctx.send(embed=embed)

        except discord.Forbidden:
            await ctx.send(
                "❌ I don't have permission to remove timeout."
            )


    # =========================
    # CLEAR
    # =========================

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):

        if amount <= 0:
            await ctx.send(
                "❌ Amount must be greater than 0."
            )
            return

        try:

            deleted = await ctx.channel.purge(
                limit=amount + 1
            )

            await create_log(
                self.bot,
                ctx.guild,
                "🧹 Clear Log",
                f"👮 Moderator: {ctx.author.mention}\n"
                f"🗑️ Deleted Messages: {len(deleted) - 1}\n"
                f"📍 Channel: {ctx.channel.mention}",
                discord.Color.blue()
            )

            message = await ctx.send(
                f"🧹 **NEXORA MODERATION**\n"
                f"Deleted **{len(deleted) - 1}** messages."
            )

            await message.delete(delay=5)

        except discord.Forbidden:
            await ctx.send(
                "❌ I don't have permission to delete messages."
            )


    # =========================
    # ERROR HANDLER
    # =========================

    @kick.error
    @ban.error
    @unban.error
    @timeout.error
    @untimeout.error
    @clear.error
    async def moderation_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):

            await ctx.send(
                "❌ You don't have permission to use this command."
            )

        elif isinstance(error, commands.MissingRequiredArgument):

            await ctx.send(
                "❌ Missing required argument.\n"
                f"Use `{ctx.prefix}help` for help."
            )

        elif isinstance(error, commands.BadArgument):

            await ctx.send(
                "❌ Invalid user, ID or number."
            )


# =========================
# SETUP
# =========================

async def setup(bot):

    await bot.add_cog(
        Moderation(bot)
    )