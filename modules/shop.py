import discord
from discord.ext import commands

from database.database import get_connection
from settings import get_all_settings


# =========================================================
# NEXORA SHOP CONFIG
# =========================================================

SHOP_BANNER = (
    "https://media.discordapp.net/attachments/1380593437635514470/"
    "1545894339379732490/NEXORA_BOT_big_stars_animated_4s.gif"
    "?ex=6a9e768b&is=6a9d250b"
    "&hm=105dc83e9294999cfdb8a47950ab89abd2aedf2457af99f9105f6206089592ef"
    "&=&width=1280&height=512"
)


COLOR = 0x8A2BE2



# =========================================================
# PRODUCTS
# =========================================================

PRODUCTS = {


    "nex": {

        "name": "🪙 NEX COIN STORE",

        "items": [

            {
                "name": "💎 Starter NEX Pack",
                "cash": "500,000 تومان",
                "nex": 500
            },

            {
                "name": "🔥 Pro NEX Pack",
                "cash": "950,000 تومان",
                "nex": 1000
            },

            {
                "name": "👑 Premium NEX Pack",
                "cash": "4,500,000 تومان",
                "nex": 5000
            }

        ]

    },


    "gift": {

        "name": "🎁 GIFT CARD STORE",

        "items": [

            {
                "name": "🎮 PlayStation Gift Card 10$",
                "cash": "950,000 تومان",
                "nex": 1000
            },

            {
                "name": "⚫ Steam Gift Card 10$",
                "cash": "950,000 تومان",
                "nex": 1000
            },

            {
                "name": "🟢 Xbox Gift Card 10$",
                "cash": "950,000 تومان",
                "nex": 1000
            }

        ]

    },


    "gaming": {

        "name": "🎮 GAME TOP UP",

        "items": [

            {
                "name": "🔫 Call Of Duty CP",
                "cash": "از 220,000 تومان",
                "nex": 250
            },

            {
                "name": "🔥 PUBG UC",
                "cash": "از 250,000 تومان",
                "nex": 300
            },

            {
                "name": "💎 Free Fire Diamonds",
                "cash": "از 280,000 تومان",
                "nex": 350
            },

            {
                "name": "⚽ eFootball Coins",
                "cash": "از 280,000 تومان",
                "nex": 350
            },

            {
                "name": "🟩 Roblox Robux",
                "cash": "از 250,000 تومان",
                "nex": 300
            },

            {
                "name": "🏰 Clash Of Clans",
                "cash": "از 250,000 تومان",
                "nex": 300
            },

            {
                "name": "👑 Clash Royale",
                "cash": "از 250,000 تومان",
                "nex": 300
            },

            {
                "name": "💥 Brawl Stars",
                "cash": "از 500,000 تومان",
                "nex": 600
            },

            {
                "name": "⚔️ Valorant Points",
                "cash": "از 1,150,000 تومان",
                "nex": 1500
            },

            {
                "name": "🎯 Fortnite V-Bucks",
                "cash": "از 2,250,000 تومان",
                "nex": 3000
            }

        ]

    },


    "subscription": {

        "name": "⭐ GAMING SUBSCRIPTIONS",

        "items": [

            {
                "name": "🔵 PlayStation Plus Essential",
                "cash": "از 2,450,000 تومان",
                "nex": 3000
            },

            {
                "name": "🟢 Xbox Game Pass Ultimate",
                "cash": "4,250,000 تومان",
                "nex": 5000
            },

            {
                "name": "💜 Discord Nitro",
                "cash": "2,250,000 تومان",
                "nex": 3000
            },

            {
                "name": "🟣 Minecraft Java & Bedrock",
                "cash": "6,950,000 تومان",
                "nex": 8000
            },

            {
                "name": "🔥 Battle.net Balance",
                "cash": "از 4,650,000 تومان",
                "nex": 5500
            }

        ]

    },


    "accounts": {

        "name": "🎮 GAME ACCOUNTS",

        "items": [

            {
                "name": "🎮 PlayStation Account",
                "cash": "تماس با پشتیبانی",
                "nex": 0
            },

            {
                "name": "⚫ Steam Account",
                "cash": "تماس با پشتیبانی",
                "nex": 0
            },

            {
                "name": "🟣 Full Gaming Account Pack",
                "cash": "تماس با پشتیبانی",
                "nex": 0
            }

        ]

    }

}
# =========================================================
# EMBED BUILDERS
# =========================================================


def main_shop_embed():

    embed = discord.Embed(

        title="🟣 𝗡𝗘𝗫𝗢𝗥𝗔 𝗦𝗛𝗢𝗣",

        description=(

            "🎮 **NEXORA GAMING MARKET**\n\n"

            "Welcome to the official NEXORA Store.\n\n"

            "Choose your category:\n\n"

            "🪙 NEX COINS\n"
            "🎁 GIFT CARDS\n"
            "🔫 GAME TOP UP\n"
            "⭐ SUBSCRIPTIONS\n"
            "🎮 GAME ACCOUNTS\n\n"

            "━━━━━━━━━━━━━━━━━━\n"

            "🪙 Buy with NEX Coin\n"
            "🎫 Secure purchase with Ticket System"

        ),

        color=COLOR

    )


    embed.set_image(

        url=SHOP_BANNER

    )


    embed.set_footer(

        text="NEXORA SHOP SYSTEM • Season 1 🟣"

    )


    return embed





def category_embed(category):


    data = PRODUCTS[category]


    embed = discord.Embed(

        title=data["name"],

        description="Select your product:\n\n",

        color=COLOR

    )


    for item in data["items"]:


        embed.description += (

            "━━━━━━━━━━━━━━\n"

            f"**{item['name']}**\n"

            f"💵 Cash Price: **{item['cash']}**\n"

            f"🪙 NEX Price: **{item['nex']} NEX**\n"

        )


    embed.set_footer(

        text="NEXORA SHOP • Secure Purchase"

    )


    return embed





def product_embed(category, index):


    item = PRODUCTS[category]["items"][index]


    embed = discord.Embed(

        title=item["name"],

        description=(

            "🛒 **Product Information**\n\n"

            f"💵 Cash Price:\n"
            f"**{item['cash']}**\n\n"

            f"🪙 NEX Price:\n"
            f"**{item['nex']} NEX**\n\n"

            "Choose payment method."

        ),

        color=COLOR

    )


    return embed





# =========================================================
# TICKET CREATOR FROM SHOP
# =========================================================


async def create_shop_ticket(
    interaction,
    product
):

    guild = interaction.guild

    user = interaction.user


    settings = get_all_settings()

    ticket_settings = settings.get(
        "ticket",
        {}
    )


    support_role_id = ticket_settings.get(
        "support_role_id"
    )


    category_id = ticket_settings.get(
        "category_id"
    )


    support_role = None


    if support_role_id:

        support_role = guild.get_role(
            support_role_id
        )


    category = None


    if category_id:

        category = guild.get_channel(
            category_id
        )


    channel_name = (
        f"ticket-buy-{user.name.lower()}"
    )


    existing = discord.utils.get(
        guild.text_channels,
        name=channel_name
    )


    if existing:


        await interaction.response.send_message(

            f"❌ شما یک تیکت باز دارید:\n{existing.mention}",

            ephemeral=True

        )

        return



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


        overwrites[support_role] = discord.PermissionOverwrite(

            view_channel=True,

            send_messages=True,

            read_message_history=True

        )



    channel = await guild.create_text_channel(

        name=channel_name,

        category=category,

        overwrites=overwrites,

        reason="NEXORA Shop Purchase"

    )



    embed = discord.Embed(

        title="🛒 NEXORA PURCHASE",

        description=(

            f"👤 Buyer: {user.mention}\n\n"

            f"📦 Product:\n"
            f"**{product['name']}**\n\n"

            f"💵 Cash Price:\n"
            f"**{product['cash']}**\n\n"

            f"🪙 NEX Price:\n"
            f"**{product['nex']} NEX**\n\n"

            "Support will continue your order."

        ),

        color=COLOR

    )



    close_button = discord.ui.Button(

        label="🔒 بستن تیکت",

        style=discord.ButtonStyle.red,

        custom_id="close_ticket_button"

    )


    view = discord.ui.View(timeout=None)

    view.add_item(close_button)



    if support_role:


        content = (

            f"{user.mention} "

            f"{support_role.mention}"

        )

    else:

        content = user.mention



    await channel.send(

        content=content,

        embed=embed,

        view=view

    )



    await interaction.response.send_message(

        f"✅ تیکت خرید ساخته شد:\n{channel.mention}",

        ephemeral=True

    )
    # =========================================================
# SHOP VIEWS
# =========================================================


class MainShopView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=None)



    @discord.ui.button(
        label="🪙 NEX COINS",
        style=discord.ButtonStyle.primary,
        custom_id="nexora_shop_nex"
    )
    async def nex(
        self,
        interaction,
        button
    ):

        await interaction.response.edit_message(

            embed=category_embed("nex"),

            view=CategoryView("nex")

        )



    @discord.ui.button(
        label="🎁 GIFT CARDS",
        style=discord.ButtonStyle.success,
        custom_id="nexora_shop_gift"
    )
    async def gift(
        self,
        interaction,
        button
    ):

        await interaction.response.edit_message(

            embed=category_embed("gift"),

            view=CategoryView("gift")

        )



    @discord.ui.button(
        label="🔫 GAME TOP UP",
        style=discord.ButtonStyle.secondary,
        custom_id="nexora_shop_gaming"
    )
    async def gaming(
        self,
        interaction,
        button
    ):

        await interaction.response.edit_message(

            embed=category_embed("gaming"),

            view=CategoryView("gaming")

        )



    @discord.ui.button(
        label="⭐ SUBSCRIPTIONS",
        style=discord.ButtonStyle.primary,
        custom_id="nexora_shop_subscription"
    )
    async def subscription(
        self,
        interaction,
        button
    ):

        await interaction.response.edit_message(

            embed=category_embed("subscription"),

            view=CategoryView("subscription")

        )



    @discord.ui.button(
        label="🎮 ACCOUNTS",
        style=discord.ButtonStyle.secondary,
        custom_id="nexora_shop_accounts"
    )
    async def accounts(
        self,
        interaction,
        button
    ):

        await interaction.response.edit_message(

            embed=category_embed("accounts"),

            view=CategoryView("accounts")

        )






class CategoryView(discord.ui.View):


    def __init__(self, category):

        super().__init__(timeout=None)

        self.category = category



        for index, item in enumerate(
            PRODUCTS[category]["items"]
        ):


            self.add_item(

                ProductButton(

                    item["name"],

                    category,

                    index

                )

            )


        self.add_item(
            BackButton()
        )






class ProductButton(discord.ui.Button):


    def __init__(
        self,
        name,
        category,
        index
    ):

        super().__init__(

            label=name[:80],

            style=discord.ButtonStyle.primary

        )


        self.category = category

        self.index = index



    async def callback(
        self,
        interaction
    ):


        await interaction.response.edit_message(

            embed=product_embed(

                self.category,

                self.index

            ),

            view=PurchaseView(

                self.category,

                self.index

            )

        )






class PurchaseView(discord.ui.View):


    def __init__(
        self,
        category,
        index
    ):

        super().__init__(timeout=None)

        self.category = category

        self.index = index





    @discord.ui.button(

        label="🪙 خرید با NEX",

        style=discord.ButtonStyle.success

    )
    async def buy_nex(

        self,

        interaction,

        button

    ):


        item = PRODUCTS[self.category]["items"][self.index]


        user_id = str(
            interaction.user.id
        )



        conn = get_connection()

        cursor = conn.cursor()



        cursor.execute(

            """

            SELECT nex_balance

            FROM users

            WHERE discord_id = ?

            """,

            (user_id,)

        )


        data = cursor.fetchone()



        if not data:


            conn.close()


            await interaction.response.send_message(

                "❌ کیف پول شما پیدا نشد.",

                ephemeral=True

            )

            return



        balance = data[0]



        if balance < item["nex"]:


            conn.close()


            await interaction.response.send_message(

                "❌ موجودی NEX شما کافی نیست.",

                ephemeral=True

            )

            return




        cursor.execute(

            """

            UPDATE users

            SET nex_balance = nex_balance - ?

            WHERE discord_id = ?

            """,

            (

                item["nex"],

                user_id

            )

        )


        conn.commit()

        conn.close()



        await interaction.response.send_message(

            (

                "✅ خرید موفق بود!\n\n"

                f"🛒 محصول:\n"
                f"**{item['name']}**\n\n"

                f"🪙 پرداخت شده:\n"
                f"**{item['nex']} NEX**"

            ),

            ephemeral=True

        )







    @discord.ui.button(

        label="🎫 خرید با تیکت",

        style=discord.ButtonStyle.danger

    )
    async def buy_ticket(

        self,

        interaction,

        button

    ):


        item = PRODUCTS[self.category]["items"][self.index]


        await create_shop_ticket(

            interaction,

            item

        )







class BackButton(discord.ui.Button):


    def __init__(self):

        super().__init__(

            label="⬅ BACK",

            style=discord.ButtonStyle.secondary

        )



    async def callback(

        self,

        interaction

    ):


        await interaction.response.edit_message(

            embed=main_shop_embed(),

            view=MainShopView()

        )






# =========================================================
# SHOP COG
# =========================================================


class Shop(commands.Cog):


    def __init__(self, bot):

        self.bot = bot





    @commands.command(name="shop")

    async def shop(

        self,

        ctx

    ):


        await ctx.send(

            embed=main_shop_embed(),

            view=MainShopView()

        )







async def setup(bot):


    await bot.add_cog(

        Shop(bot)

    )


    print(

        "SHOP MODULE LOADED"

    )