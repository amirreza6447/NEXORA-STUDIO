import sqlite3
import os


DB_PATH = "database/nexora.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():

    os.makedirs("database", exist_ok=True)

    conn = get_connection()
    cursor = conn.cursor()

    # =========================
    # USERS TABLE
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        discord_id TEXT PRIMARY KEY,

        xp INTEGER DEFAULT 0,

        level INTEGER DEFAULT 1,

        nex_balance INTEGER DEFAULT 0,

        purchased_nex INTEGER DEFAULT 0,

        reward_nex INTEGER DEFAULT 0,

        rank TEXT DEFAULT 'Membership',

        last_daily INTEGER DEFAULT 0,

        daily_retry INTEGER DEFAULT 0

    )
    """)


    # =========================
    # MEMBERS RECOVERY TABLE
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (

        discord_id TEXT PRIMARY KEY,

        joined_at INTEGER,

        welcomed INTEGER DEFAULT 0

    )
    """)


    # =========================
    # SHOP PRODUCTS TABLE 🛒
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        description TEXT,

        nex_price INTEGER DEFAULT 0,

        cash_price TEXT DEFAULT 'تماس با پشتیبانی',

        stock INTEGER DEFAULT -1,

        type TEXT DEFAULT 'item'

    )
    """)


    # =========================
    # PURCHASE HISTORY TABLE
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS purchases (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        discord_id TEXT,

        product_id INTEGER,

        payment_type TEXT,

        price INTEGER,

        purchased_at INTEGER

    )
    """)


    # =========================
    # SAFE COLUMN MIGRATIONS
    # =========================

    # last_daily
    try:

        cursor.execute("""
            ALTER TABLE users
            ADD COLUMN last_daily INTEGER DEFAULT 0
        """)

        print("LAST DAILY COLUMN ADDED")

    except sqlite3.OperationalError:

        pass


    # daily_retry
    try:

        cursor.execute("""
            ALTER TABLE users
            ADD COLUMN daily_retry INTEGER DEFAULT 0
        """)

        print("DAILY RETRY COLUMN ADDED")

    except sqlite3.OperationalError:

        pass


    # =========================
    # SAVE DATABASE
    # =========================

    conn.commit()
    conn.close()


def create_user(discord_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO users
    (
        discord_id
    )
    VALUES (?)
    """,

    (str(discord_id),))

    conn.commit()
    conn.close()