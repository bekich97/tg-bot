from telebot import types
from db import get_db_connection

# Main menu view
def main_menu(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🏠 Main Menu')
    item2 = types.KeyboardButton('📝 Fill Form')
    item3 = types.KeyboardButton('✍️ Refill Form')
    item4 = types.KeyboardButton('📙 Help')

    markup.add(item1, item2, item3, item4)
    
    bot.send_message(
        message.chat.id,
        f'Hello, {message.from_user.first_name}! Welcome main menu!', 
        reply_markup=markup
    )

# 📝 Fill Form button click view
def fill_form(bot, message):
    # Get users nickname and create one row if not exists
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO users (nickname) SELECT '{message.from_user.username}' WHERE NOT EXISTS(SELECT 1 FROM users WHERE nickname='{message.from_user.username}')""")
    conn.commit()
    # Get user info to write next to button text
    cursor.execute(f"SELECT * FROM users WHERE nickname='{message.from_user.username}'")
    current_user = cursor.fetchall()[0]
    markup = types.InlineKeyboardMarkup(row_width=1)
    first_name_button = types.InlineKeyboardButton(text=f'First name: {current_user[2] if current_user[2] else ""}', callback_data="first_name_fill", markup="HTML")
    last_name_button = types.InlineKeyboardButton(text=f'Last name: {current_user[3] if current_user[3] else ""}', callback_data="last_name_fill")
    email_button = types.InlineKeyboardButton(text=f'Email: {current_user[4] if current_user[4] else ""}', callback_data="email_fill")
    phone_button = types.InlineKeyboardButton(text=f'Phone: {current_user[5] if current_user[5] else ""}', callback_data="phone_fill")
    birth_date_button = types.InlineKeyboardButton(text=f'Birth date: {current_user[6] if current_user[6] else ""}', callback_data="birth_date_fill")
    # current_user[7] is form sent status, check and create submit button
    if current_user[7]:
        send_button = types.InlineKeyboardButton(text='✅ Already sent', callback_data="already_sent")
    else:
        send_button = types.InlineKeyboardButton(text='📤 Send', callback_data="send")
    markup.add(
        first_name_button,
        last_name_button,
        email_button,
        phone_button,
        birth_date_button,
        send_button
    )
    bot.send_message(
        message.chat.id,
        'Fill the form!', 
        reply_markup=markup
    )
