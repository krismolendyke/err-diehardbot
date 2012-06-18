#!/usr/bin/env python


"""A bot which will respond to various Die Hard character name commands and
mentions and respond with a random line spoken by that character in the film.
"""


from errbot.botplugin import BotPlugin
from errbot.jabberbot import botcmd

from dieHard import DieHard


class DieHardBot(BotPlugin):
    def __init__(self):
        super(BotPlugin, self).__init__()
        self.diehard = DieHard()


    @botcmd
    def mcclane(self, mess, args):
        """Get a random McClane line."""
        return "(mcclane) " + self.diehard.get_random("mcclane")


    @botcmd
    def hans(self, mess, args):
        """Get a random Hans line."""
        return "(hans) " + self.diehard.get_random("hans")


    @botcmd
    def takagi(self, mess, args):
        """Get a random Takagi line."""
        return "(takagi) " + self.diehard.get_random("takagi")


    @botcmd
    def ellis(self, mess, args):
        """Get a random Ellis line."""
        return "(ellis) " + self.diehard.get_random("ellis")


    @botcmd
    def holly(self, mess, args):
        """Get a random Holly line."""
        return "(holly) " + self.diehard.get_random("holly")


    @botcmd
    def powell(self, mess, args):
        """Get a random Powell line."""
        return "(powell) " + self.diehard.get_random("powell")


    @botcmd
    def argyle(self, mess, args):
        """Get a random Argyle line."""
        return "(argyle) " + self.diehard.get_random("argyle")


    @botcmd
    def thornburg(self, mess, args):
        """Get a random Thornburg line."""
        return "(thornburg) " + self.diehard.get_random("thornburg")


    @botcmd
    def robinson(self, mess, args):
        """Get a random Robinson line."""
        return "(robinson) " + self.diehard.get_random("robinson")


    @botcmd
    def bigjohnson(self, mess, args):
        """Get a random Big Johnson line."""
        return "(bigjohnson) " + self.diehard.get_random("bigjohnson")


    @botcmd
    def littlejohnson(self, mess, args):
        """Get a random Little Johnson line."""
        return "(littlejohnson) " + self.diehard.get_random("littlejohnson")


    def callback_message(self, conn, mess):
        """Listen for Die Hard mentions and interject random quotes from those
        characters who were mentioned.
        """
        message = ""
        if mess.getBody().find("(hans)") != -1:
            message = "(hans) " + self.diehard.get_random("hans")
        if message:
            self.send(mess.getFrom(), message, message_type=mess.getType())
