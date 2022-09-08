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
            InlineKeyboardButton("Enter_info", callback_data="user_info"),
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
    fh.write(';'.join(user_info_list) + '\n')
    fh.close()


    context.bot.send_message(chat_id=chat.id, text=user_text)
    return ConversationHandler.END  


def User_search(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text="Use /search_name to search contact by name. \nThis bot can search contact`s by adress just write /search_adress. \nAlso you can search some-body of you`recantacts by /search_phone ")



def search_name(update, context):
    chat = update.effective_chat
    search_name = context.args[0]

    result = 'Contact not found'

    fh = open('test.txt', 'r')
    while True:
        person_line = fh.readline().rstrip('\n')
        person_list = person_line.split(';')
        if person_list[0] == search_name:
            result = person_line
            break
        if not person_line:
            break
    fh.close()

    user_data['phone'] = update.message.text
    context.bot.send_message(chat_id=chat.id, text=result)

def search_adress(update, context):
    chat = update.effective_chat
    search_adress = context.args[0]

    result = 'Contact not found'

    fh = open('test.txt', 'r')
    while True:
        person_line = fh.readline().rstrip('\n')
        person_list = person_line.split(';')
        if person_list[1] == search_adress:
            result = person_line
            break
        if not person_line:
            break
    fh.close()

    user_data['phone'] = update.message.text
    context.bot.send_message(chat_id=chat.id, text=result)


def search_phone(update, context):
    chat = update.effective_chat
    search_phone = context.args[0]

    result = 'Contact not found'

    fh = open('test.txt', 'r')
    while True:
        person_line = fh.readline().rstrip('\n')
        person_list = person_line.split(';')
        if person_list[2] == search_phone:
            result = person_line
            break
        if not person_line:
            break
    fh.close()

    user_data['phone'] = update.message.text
    context.bot.send_message(chat_id=chat.id, text=result)

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
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("cancel", cancel))
    dispatcher.add_handler(CommandHandler("search_name", search_name))
    dispatcher.add_handler(CommandHandler("search_adress", search_adress))
    dispatcher.add_handler(CommandHandler("search_phone", search_phone))
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