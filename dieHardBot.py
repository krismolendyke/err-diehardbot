#!/usr/bin/env python


"""A bot which will respond to various Die Hard character name commands and
mentions and respond with a random line spoken by that character in the film.
"""

from errbot import botcmd
from errbot.botplugin import BotPlugin
from errbot.utils import get_sender_username
import config
import logging

from dieHard import DieHard


def generate(character):
    f = lambda self, mess, args: "(%s) %s" % (character,
            self.diehard.get_random(character))
    f.__name__ = character
    f.__doc__ = "Get a random quote from %s." % character.title()
    return f


class DieHardBotBuilder(type):
    def __new__(mcs, name, bases, classDict):
        newClassDict = dict(classDict.items() +
                            [(character, botcmd(generate(character)))
                            for character in DieHard.CHARACTERS])
        return super(DieHardBotBuilder, mcs).__new__(mcs, name, bases,
                                                     newClassDict)


class DieHardBot(BotPlugin):
    __metaclass__ = DieHardBotBuilder
    min_err_version = "1.6.0"


    def __init__(self):
        super(BotPlugin, self).__init__()
        self.diehard = DieHard()


    def callback_message(self, conn, mess):
        """Listen for Die Hard mentions and interject random lines from those
        characters who were mentioned.
        """
        logging.debug("mess.getFrom().getStripped(): " + mess.getFrom().getStripped())
        logging.debug("config.BOT_IDENTITY['username']: " + config.BOT_IDENTITY["username"])
        logging.debug("get_sender_username(mess): " + get_sender_username(mess))
        logging.debug("config.CHATROOM_FN: " + config.CHATROOM_FN)
        if (mess.getFrom().getStripped() == config.BOT_IDENTITY["username"]) or (get_sender_username(mess) == config.CHATROOM_FN):
            logging.debug("Ignore a message from myself")
            return False

        message = ""
        for character in DieHard.CHARACTERS:
            if mess.getBody().find("(%s)" % character) != -1:
                message += "(%s) %s  " % (character, self.diehard.get_random(character))
        if message:
            self.send(mess.getFrom(), message, message_type=mess.getType())
