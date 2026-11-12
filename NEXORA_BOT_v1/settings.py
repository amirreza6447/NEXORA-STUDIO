import json
import os
import copy


SETTINGS_FILE = "settings.json"


# ==================================================
# DEFAULT SETTINGS FOR EACH SERVER
# ==================================================

DEFAULT_SERVER_SETTINGS = {
    "welcome": {
        "enabled": True,
        "channel_id": None
    },

    "leave": {
        "enabled": True,
        "channel_id": None
    },

    "autorole": {
        "enabled": True,
        "member_role_id": None,
        "bot_role_id": None
    },

    "logs": {
        "enabled": True,
        "channel_id": None
    },

    "ticket": {
        "enabled": True,
        "support_role_id": None,
        "category_id": None
    },

    "giveaway": {
        "enabled": True,
        "channel_id": None
    }
}


# ==================================================
# CREATE NEW SERVER SETTINGS
# ==================================================

def create_server_settings():

    return copy.deepcopy(
        DEFAULT_SERVER_SETTINGS
    )


# ==================================================
# LOAD ALL SETTINGS
# ==================================================

def load_settings():

    # اگر فایل وجود ندارد
    if not os.path.exists(
        SETTINGS_FILE
    ):

        data = {}

        save_settings(data)

        return data


    try:

        with open(
            SETTINGS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)


        if not isinstance(
            data,
            dict
        ):

            print(
                "❌ SETTINGS FILE FORMAT ERROR"
            )

            return {}


        return data


    except Exception as e:

        print(
            "❌ SETTINGS LOAD ERROR:",
            e
        )

        return {}


# ==================================================
# SAVE ALL SETTINGS
# ==================================================

def save_settings(data):

    try:

        with open(
            SETTINGS_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )


        print(
            "✅ SETTINGS SAVED"
        )


    except Exception as e:

        print(
            "❌ SETTINGS SAVE ERROR:",
            e
        )


# ==================================================
# GET SETTINGS FOR ONE SERVER
# ==================================================

def get_guild_settings(guild_id):

    settings = load_settings()

    guild_id = str(
        guild_id
    )


    # اگر سرور هنوز تنظیمات ندارد
    if guild_id not in settings:

        settings[guild_id] = (
            create_server_settings()
        )

        save_settings(
            settings
        )


    return settings[
        guild_id
    ]


# ==================================================
# GET ONE SETTING
# ==================================================

def get_setting(
    guild_id,
    section,
    key
):

    guild_settings = get_guild_settings(
        guild_id
    )


    return guild_settings.get(
        section,
        {}
    ).get(
        key
    )


# ==================================================
# SET ONE SETTING
# ==================================================

def set_setting(
    guild_id,
    section,
    key,
    value
):

    settings = load_settings()

    guild_id = str(
        guild_id
    )


    # ایجاد تنظیمات برای سرور جدید
    if guild_id not in settings:

        settings[guild_id] = (
            create_server_settings()
        )


    # ایجاد بخش در صورت نبودن
    if section not in settings[guild_id]:

        settings[guild_id][section] = {}


    # ذخیره مقدار
    settings[guild_id][section][key] = (
        value
    )


    save_settings(
        settings
    )


# ==================================================
# GET ALL SETTINGS
# ==================================================

def get_all_settings():

    return load_settings()