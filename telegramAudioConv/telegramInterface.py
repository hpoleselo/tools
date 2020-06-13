import logging

from telegram import (ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#ESTADO1=0 ESTADO2=1
ESTADO1, ESTADO2 = range(2)
counter = 0

""" TODO: 
    1. TEST CONVERSION USING FFMPEG: ffmpeg -i rodrigo.ogg output.mp3
    2. TEST SENDING MP3 AUDIO
    3. bot.send_audio(chat_id=chat_id, audio=open('conv/test.mp3', 'rb'))
    4. colocar iteracao pra mudar o filename
    5. sistema de pastas conv/downloaded
"""

def retrieveToken():
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

def start(update, context):
    logger.debug("Start function has been called!")
    update.message.reply_text('Send me .ogg so that i convert them for you! \nFirst send the audio with the following structure: /conv audio.ogg \nIf you wish to save them, press yes after receiving the converted audio.')
    logger.debug("Going to state 2")
    return ESTADO2


def photo(update, context):
    logger.debug("Photo function has been called.")
    # uploada a ultima mensagem do usuario
    user = update.message.from_user

    # da ultima mensagem pegar a imagem em forma de arquivo (criamos na verdade uma instancia)
    photo_file = update.message.photo[-1].get_file()

    # usando o metodo da instancia para baixar a foto
    photo_file.download('user_photo.jpg')

    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    
    update.message.reply_text('Imagem foi baixada')
    logger.debug("Going to state 2")
    return ESTADO2


def audio(update, context):
    global counter
    user = update.message.from_user
    
    # Reason why the previous options didn't work
    #So it appears that the bot- pass_user_data in the callback function is deprecated and from now on you should use context based callbacks.
    #CallbackContext is an object that contains all the extra context information regarding an Update, error or Job.
    audio_file = context.bot.getFile(update.message.audio.file_id)
    logger.info("File size: %s bytes", audio_file.file_size)
    
    # TODO: get filename using document object
    # TODO: add exception if the directory /conv is not there

    # Building file name
    counter += 1
    audio_path = "./conv/"
    audio_name = str(user.first_name) + "_audio" + str(counter) + ".mp3"
    audio_full = audio_path + audio_name
    audio_file.download(audio_full)
    logger.info("Audio has from %s has been received", user.first_name)    
    update.message.reply_text('Audio has been converted to mp3.')
    logger.info("Sending audio to user...")
    # chat_id for groups is usually negative
    chat_id = update.message.chat_id
    context.bot.send_audio(chat_id=chat_id, audio=open(audio_full, 'rb'))
    logger.info("Audio sent.")
    return ESTADO2


def cancel(update, context):
    """ Funcao de saida caso usuario clique pra sair. """
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    api_key = retrieveToken()
    updater = Updater(api_key, use_context=True)


    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    
    # The ConversationHandler handles 4 other different handlers (in entry_points is trated as a list with to initiate the conversation (e.g: telegram.ext.CommandHandler or telegram.ext.RegexHandler))
    conv_handler = ConversationHandler(
        # the first argument is the name of the command in the chat, in this case /start and then the second argument will be the name of the functin on this program
        # THE PROGRAM WILL RUN THIS AT FIRST
        entry_points=[CommandHandler('start', start)],

        # second collection is a dict, not a list like the previous one. ()
        states={

            # THEN BASED ON THE OUTPUT FROM THE ENTRY_POINT (STARTER), IN THIS CASE IS 0, THEN IT'S GONNA TRANSIT TO STATE 0
            # SINCE THE INDEX 0 OF THE DICTIONARY IS THE MESSAGE HANDLER SO photo() function is called.
            ESTADO1: [MessageHandler(Filters.photo, photo)],

            # It's gonna wait for an audio as a filter
            ESTADO2: [MessageHandler(Filters.audio, audio)]
                    #CommandHandler('skip', skip_photo)]

                    
        },
        # The third collection, a list named fallbacks, is used if the user is currently in a conversation but the state has either no associated handler or the handler 
        # that is associated to the state is inappropriate for the update, for example if the update contains a command, but a regular text message is expected.
        # You could use this for a /cancel command or to let the user know their message was not recognized
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)
    
    # Since we added the conv_handler, which encapsulates all other handlers and their relations, we comment the lines below out
    #dp.add_handler(CommandHandler("start", start))
    #dp.add_handler(CommandHandler("photo", photo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
