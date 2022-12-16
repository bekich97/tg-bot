from handlers import *
from actions import *
from config import bot
from datetime import datetime
from db import create_users_table
from automation import run_automation

# User texts handler
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == "🏠 Main Menu":
        main_menu(bot, message)
    elif message.text == "📝 Fill Form":
        fill_form(bot, message)
    elif message.text == "🔙 Back to Menu":
        main_menu(bot, message)
    else:
        main_menu(bot, message)

# Inline buttons callback data handler 
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🔙 Back to Menu')
    markup.add(item1)

    if call.data == "first_name_fill":
        sent = bot.send_message(
            call.message.chat.id,
            'Write your first name:',
            reply_markup=markup
        )
        bot.register_next_step_handler(sent, save_first_name)
    elif call.data == "last_name_fill":
        sent = bot.send_message(
            call.message.chat.id,
            'Write your last name:',
            reply_markup=markup
        )
        bot.register_next_step_handler(sent, save_last_name)
    elif call.data == "email_fill":
        sent = bot.send_message(
            call.message.chat.id,
            'Write your email:',
            reply_markup=markup
        )
        bot.register_next_step_handler(sent, save_email)
    elif call.data == "phone_fill":
        sent = bot.send_message(
            call.message.chat.id,
            'Write your phone:',
            reply_markup=markup
        )
        bot.register_next_step_handler(sent, save_phone)
    elif call.data == "birth_date_fill":
        sent = bot.send_message(
            call.message.chat.id,
            'Write your birth date:',
            reply_markup=markup
        )
        bot.register_next_step_handler(sent, save_birth_date)
    elif call.data == "send":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f""" UPDATE users SET chat_id='{call.message.chat.id}', sent=1, sent_date='{str(datetime.now())}' WHERE nickname='{call.message.chat.username}' """)
        conn.commit()
        bot.send_message(
            call.message.chat.id,
            'Your request has been added to the queue!',
            reply_markup=markup
        )
        flag = 0
        # Try to fill form for 5 times if not success
        while flag < 5:
            res = run_automation(call.message.chat.username)
            if res:
                flag = 10
                bot.send_message(
                    call.message.chat.id,
                    'Seccessfully! Here is image link: https://picsum.photos/id/237/200/300',
                    reply_markup=markup
                )
            else:
                flag += 1
                if flag == 5:
                    bot.send_message(
                        call.message.chat.id,
                        'Unseccessfully!',
                        reply_markup=markup
                    )

# Create users table
create_users_table()

bot.infinity_polling()
