import logging
from telegram import InlineQueryResultArticle, InlineQueryResult, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

smallChar = [i for i in range(97,123)]
bigChar = [i for i in range(65,91)]
front = 0
rear  = 25
def Encoding(bot,update):
    msg = update.message.text
    temp = list(msg)
    for i in range(len(msg)):
        if( 97 <= ord(temp[i]) <= 122 ):
            if(ord(temp[i])+13 > 122):
                new = (13 - (smallChar[rear] - ord(temp[i]))) + front - 1
            else:
                new = ((ord(temp[i]) + 13) % 25) + 3
            temp[i] = chr(smallChar[new])
            msg = "".join(temp)
        elif( 65 <= ord(temp[i]) <= 90 ):
            if (ord(temp[i]) + 13 > 90 ):
                new = (13 - (bigChar[rear] - ord(temp[i]))) + front - 1
            else:
                new = ((ord(temp[i]) + 13) % 25) + 10
            temp[i] = chr(bigChar[new])
            msg = "".join(temp)
        else:
            msg = "".join(temp)
    bot.send_message(chat_id=update.message.chat_id, text= msg)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="""
               Hello , Habariooo ???? :)))

Welcome To My First Bot !!!! :|

Type Your Text To Encode/Decode It...

               """)

def inline_encode(bot, update):
    if update.inline_query:
        msg = update.inline_query.query
        #msg = query
        temp = list(msg)
        for i in range(len(msg)):
            if (97 <= ord(temp[i]) <= 122):
                if (ord(temp[i]) + 13 > 122):
                    new = (13 - (smallChar[rear] - ord(temp[i]))) + front - 1
                else:
                    new = ((ord(temp[i]) + 13) % 25) + 3
                temp[i] = chr(smallChar[new])
                msg = "".join(temp)
            elif (65 <= ord(temp[i]) <= 90):
                if (ord(temp[i]) + 13 > 90):
                    new = (13 - (bigChar[rear] - ord(temp[i]))) + front - 1
                else:
                    new = ((ord(temp[i]) + 13) % 25) + 10
                temp[i] = chr(bigChar[new])
                msg = "".join(temp)
            else:
                msg = "".join(temp)

        result = list()
        result.append(InlineQueryResultArticle(id=msg.upper(),title='ROT13',input_message_content= InputTextMessageContent(msg)))
        bot.answerInlineQuery(update.inline_query.id, result)



def main():
    token = '415483744:AAELVd7S_2foXZibiK35OLiLcKfxRPPvolY'
    TelegramBot = Updater(token)
    TelegramBot.dispatcher.add_handler(CommandHandler('start', start))

    msg = MessageHandler(Filters.text, Encoding)
    TelegramBot.dispatcher.add_handler(msg)
    inline_caps_handler = InlineQueryHandler(inline_encode)
    TelegramBot.dispatcher.add_handler(inline_caps_handler)
    #TelegramBot.dispatcher.add_handler(InlineQueryHandler(inline_encode))

    TelegramBot.start_polling()
    TelegramBot.idle()

if __name__ == '__main__':
    main()