from handlers import fill_form, main_menu
from config import bot
from db import get_db_connection

# Save first name to database
def save_first_name(message):
    if message.text != "🔙 Back to Menu":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f""" UPDATE users SET first_name='{message.text}' WHERE nickname='{message.from_user.username}' """)
        conn.commit()
        fill_form(bot, message)
    else:
        main_menu(bot, message)

# Save last name to database
def save_last_name(message):
    if message.text != "🔙 Back to Menu":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f""" UPDATE users SET last_name='{message.text}' WHERE nickname='{message.from_user.username}' """)
        conn.commit()
        fill_form(bot, message)
    else:
        main_menu(bot, message)

# Save phone to database
def save_phone(message):
    if message.text != "🔙 Back to Menu":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f""" UPDATE users SET phone='{message.text}' WHERE nickname='{message.from_user.username}' """)
        conn.commit()
        fill_form(bot, message)
    else:
        main_menu(bot, message)

# Save email to database
def save_email(message):
    if message.text != "🔙 Back to Menu":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f""" UPDATE users SET email='{message.text}' WHERE nickname='{message.from_user.username}' """)
        conn.commit()
        fill_form(bot, message)
    else:
        main_menu(bot, message)

# Save birth date to database
def save_birth_date(message):
    if message.text != "🔙 Back to Menu":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f""" UPDATE users SET birth_date='{message.text}' WHERE nickname='{message.from_user.username}' """)
        conn.commit()
        fill_form(bot, message)
    else:
        main_menu(bot, message)