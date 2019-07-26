from telegram import Bot
from telegram.ext import Updater, CommandHandler
import logging
import surfForecast
import re



class TeleBot(object):
    def __init__(self):
        TOKEN = self.retrieveToken()
        # On version 12 use_context is mandatory, on 13 this will be default
        self.updater = Updater(token=TOKEN, use_context=True)

        self.dispatcher = self.updater.dispatcher
        
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

    def retrieveToken(self):
        """ Retrieves the Token from the txt file. """
        try:
            with (open("tokAccess.txt")) as fileRead:
                lines = fileRead.readlines()
                # Remove the \n in the txt file
                lines_wout_n = [s.replace('\n','') for s in lines]
                # Getting token
                return lines_wout_n[0]
        except(KeyboardInterrupt):
            print("Proccess interrupted, could not get the Token.")


    def checkBot(self):
        """ Hello World to check if the bot is working """
        bot = telegram.Bot(token=TOKEN)
        print(bot.get_me())

    def start(self, update, context):
        """ Callback function to send a message """
        print("Request to send message made")
        context.bot.send_message(chat_id=update.message.chat_id, text="Sou o bot barril das mares, para saber sobre as mares atualmente em Vilas do Atlântico use /mares")

    def fodase(self, update, context):
        """ Just prints text when the command /start is given on the bot chat """
        context.bot.send_message(chat_id=update.message.chat_id, text="FODASE CARALHO!")

    def mares(self, update, context):
        """ Just prints text when the command /start is given on the bot chat """
        sf = surfForecast()
        print(sf)
        context.bot.send_message(chat_id=update.message.chat_id, text=strDasMares)

    def helloWorld(self):
        """ Sent to the polling so when the message is sent on the channel we show the responses. """
        # The second argument is the callback function self.start()
        startHandler = CommandHandler('start', self.start)
        # We pass the start function to our Bot, so when we write "/start" on telegram he should reply whats in self.start()
        self.dispatcher.add_handler(startHandler)

        fodaseHandler = CommandHandler('fodase', self.fodase)
        self.dispatcher.add_handler(fodaseHandler)

        maresHandler = CommandHandler('mares', self.mares)
        self.dispatcher.add_handler(maresHandler)




    def runBot(self):
        print("Tentou rodar o bot")
        self.updater.start_polling()
        self.helloWorld()



def run():
    tb = TeleBot()
    tb.runBot()

if __name__ == "__main__":
    run()



    