from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from logging import getLogger

from grjm.config import TG_TOKEN
#from grjm.config import TG_API_URL

logger = getLogger(__name__)

#декоратор для логирования
def debug_requests(f):
    def inner(*args, **kwargs):
        try:
            logger.info(f"Обращение в метод {f.__name__}")
            return f(*args, **kwargs)
        except:
            logger.exception(f"Ошибка в  функции {f.__name__}")
            raise
    return inner


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id.update.message.chat_id,
        text="Hi, I'm GeraJimo",
    )

def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    user_text = update.message.text
    text=f"You id is: {chat_id} and you send me {user_text}"
    bot.send_message(
        chat_id=chat_id,
        text=text,
    )
    
def main():
    bot = Bot(
        token=TG_TOKEN,
        #base_url=TG_API_URL,
    )
    
    updater = Updater(
        bot=bot,
    )
    
    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    
    #download updates
    updater.start_polling()
    #don't off while all updaters is working
    updater.idle()
    
if __name__='__main__':
    main()
