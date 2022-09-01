from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    CallbackContext, 
    MessageHandler, 
    Filters
)
user_data = dict()
#Stages
STEP_ONE, STEP_TWO, STEP_THREE, STEP_FOUR = range(4)



def start(update: Update, context: CallbackContext) -> None:
    menu(update, context)


def menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Enter_Info", callback_data="user_info"),
            InlineKeyboardButton("User_search", callback_data="User_search"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Send or receive info ?", reply_markup=reply_markup)


   

def user_name(update, context) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="enter your name")
    return STEP_TWO


def user_adress(update, context):
    chat = update.effective_chat
    user_data['name'] = update.message.text 

    context.bot.send_message(chat_id=chat.id, text="enter your city")
    return STEP_THREE    


def user_phone(update, context):
    chat = update.effective_chat
    user_data['city'] = update.message.text 

    context.bot.send_message(chat_id=chat.id, text="enter your phone ")
    return STEP_FOUR    


def user_finish(update, context):
    chat = update.effective_chat
    user_data['phone'] = update.message.text
    
    user_text = "Thanks " + user_data.get('name') + " 😉"

    delimetr = '-------------------'

    fh = open('test.txt', 'a')
    
    user_info_list = user_data.values()
    # user_info_list['User_name'] = user_data['name']
    # user_info_list['User_city'] = user_data['city']
    # user_info_list['User_phone'] = user_data['phone']
    fh.write(';'.join(user_info_list) + '\n')
    fh.close()


    context.bot.send_message(chat_id=chat.id, text=user_text)
    return ConversationHandler.END  
    
def User_search(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Ім'я", callback_data="1"),
            InlineKeyboardButton("Місто", callback_data="2"),
        ],
        [
            InlineKeyboardButton("Номер телефону", callback_data="3")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose one of the options  :", reply_markup=reply_markup)
    
    user_data['phone'] = update.message.text
    
    user_search = '123-99-99'
    
    fh = open('test-denys.txt')
    while True:
        line = fh.readline().rstrip('\n')
        user_info = line.split('|')
        if user_info[2] == user_search:
            print(user_info[0])
            break
    
        if not line:
            break

    fh.close()



def cancel(update, context):
    update.message.reply_text('Cancelled by user. Send /menu to start again')
    return ConversationHandler.END

def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to start using this bot. \nThis bot can send & receive info. ")


def main() -> None:
    """Run the bot."""
    updater = Updater(token='5784290831:AAEhaiVK0uoNnxl3mLB3dw4dGNZeZJL6iZc')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("menu", menu))
    # dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CallbackQueryHandler(User_search, pattern="User_search"))

    branch_user_handler = ConversationHandler(
        entry_points = [CallbackQueryHandler(user_name, 'user_info')], 
        states={
            STEP_TWO:   [MessageHandler(Filters.text & (~ Filters.command), user_adress)],
            STEP_THREE: [MessageHandler(Filters.text & (~ Filters.command), user_phone)],
            STEP_FOUR:  [MessageHandler(Filters.text & (~ Filters.command), user_finish)]
        }, 
        fallbacks=[CommandHandler("stop", cancel)]
    )

    dispatcher.add_handler(branch_user_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()