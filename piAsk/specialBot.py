#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from typing import Dict

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

SEND_AUDIO, SEND_PHOTO, SEND_QUESTIONARIO = range(3)

reply_keyboard = [
    ['SIM (tem surpresa)', 'Não (TRISTE)'],
    ['Xô Pensá...'],
    ['SiSáia'],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Sou um bot criado por henrivis especialmente pra Pi, o Henrique fez uma surpresa ESPECIAL pra Pi! Para prosseguir por favor, digite TEILE para gerar um codigo QR."
    )

    return SEND_PHOTO

def send_photo(update: Update, context: CallbackContext) -> int:
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=open('qr.png', 'rb'))
    update.message.reply_text(
        "Depois de abrir o código QR digite TEILE novamente, por favor."
    )
    return SEND_AUDIO

def send_audio(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Agora que você já viu o video dá pra ter uma noção de onde eu quero chegar? Escuta essa música aqui..."
    )
    chat_id = update.message.chat_id
    context.bot.send_audio(chat_id=chat_id, audio=open('diversasQ.mp3', 'rb'))
    update.message.reply_text(
        "Digite TEILE de novo, plzplzplz"
    )
    return SEND_QUESTIONARIO


def questionario(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "ENHAIN, QUAL VAI SER? Agora vai ter que escolher... Ou eu ou eu? Aceita namorar comigo, pi?\n Para responder, use a ferrament indicada na imagem abaixo rs",
        reply_markup=markup,
    )
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=open('instrucao.jpg', 'rb'))
    return ConversationHandler.END

def cancel(update, context):
    """ Funcao de saida caso usuario clique pra sair. """
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def main() -> None:
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1367811881:AAFLHmQEFZnC8Qew-MG0jHddVd4FzJ8RJt0", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={

            SEND_PHOTO: [MessageHandler(Filters.all, send_photo)],
            SEND_AUDIO: [MessageHandler(Filters.all, send_audio)],
            SEND_QUESTIONARIO: [MessageHandler(Filters.all, questionario)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()