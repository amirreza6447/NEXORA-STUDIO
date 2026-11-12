import os

from dotenv import load_dotenv

load_dotenv()


# =========================
# BOT SETTINGS
# =========================

TOKEN = os.getenv("DISCORD_TOKEN")

PREFIX = "!"





# ==================================================
# MAIN NEXORA SERVER
# ==================================================

MAIN_SERVER_ID = 1537575549445083270

MAIN_SUPPORT_ROLE_ID = 1537579922661576714

MAIN_WELCOME_CHANNEL_ID = 1537579943893016609

MAIN_LEAVE_CHANNEL_ID = 1539697715217436733

MAIN_MEMBER_ROLE_ID = 1537579928491401216

MAIN_BOT_ROLE_ID = 1537579929573793915

MAIN_LOG_CHANNEL_ID = 1540478117322297394

MAIN_GIVEAWAY_CHANNEL_ID = 1537579967309807778

GIVEAWAY_CHANNEL_ID = MAIN_GIVEAWAY_CHANNEL_ID


# ==================================================
# NEXORA SHOP SERVER
# ==================================================

SHOP_SERVER_ID = 1539043824469413948

SHOP_SUPPORT_ROLE_ID = 1541495743104155739

SHOP_WELCOME_CHANNEL_ID = 1539666014755758200

# سرور شاپ چنل Leave ندارد
SHOP_LEAVE_CHANNEL_ID = None

SHOP_MEMBER_ROLE_ID = 1541497527633969282

SHOP_BOT_ROLE_ID = 1541497807133999104

SHOP_LOG_CHANNEL_ID = 1539669205958533271

SHOP_TICKET_CHANNEL_ID = 1539668772908961893


# ==================================================
# MULTI SERVER SETTINGS
# ==================================================

SERVER_SETTINGS = {
    MAIN_SERVER_ID: {
        "welcome_channel": MAIN_WELCOME_CHANNEL_ID,
        "leave_channel": MAIN_LEAVE_CHANNEL_ID,
        "member_role": MAIN_MEMBER_ROLE_ID,
        "bot_role": MAIN_BOT_ROLE_ID,
        "log_channel": MAIN_LOG_CHANNEL_ID,
        "support_role": MAIN_SUPPORT_ROLE_ID,
        "giveaway_channel": MAIN_GIVEAWAY_CHANNEL_ID,
        "ticket_channel": None,
    },

    SHOP_SERVER_ID: {
        "welcome_channel": SHOP_WELCOME_CHANNEL_ID,
        "leave_channel": SHOP_LEAVE_CHANNEL_ID,
        "member_role": SHOP_MEMBER_ROLE_ID,
        "bot_role": SHOP_BOT_ROLE_ID,
        "log_channel": SHOP_LOG_CHANNEL_ID,
        "support_role": SHOP_SUPPORT_ROLE_ID,
        "giveaway_channel": None,
        "ticket_channel": SHOP_TICKET_CHANNEL_ID,
    }
}