#!/usr/bin/env python


"""Get random lines for various characters in the film Die Hard."""


from random import choice
import re
import os

from config import BOT_DATA_DIR
from errbot.utils import PLUGINS_SUBDIR


class DieHard(object):
    CHARACTERS = {
        "mcclane": r"MCCLANE",
        "hans": r"HANS",
        "takagi": r"TAKAGI",
        "ellis": r"ELLIS",
        "holly": r"HOLLY",
        "powell": r"POWELL",
        "argyle": r"ARGYLE",
        "thornburg": r"THORNBURG",
        "robinson": r"ROBINSON",
        "bigjohnson": r"BIG JOHNSON",
        "littlejohnson": r"LITTLE JOHNSON"
    }


    def __init__(self):
        super(DieHard, self).__init__()
        self.lines = {}
        for name, name_re in DieHard.CHARACTERS.iteritems():
            self.lines[name] = self.get_lines(name_re)


    def get_random(self, name):
        """Get a random line for the given character's name."""
        if name in self.lines:
            return choice(self.lines[name])
        else:
            return ("Sorry, is \"%s\" in Die Hard?  I only know of " % name +
                    ", ".join(DieHard.CHARACTERS.keys()[:-1]) + " and " +
                    DieHard.CHARACTERS.keys()[-1] + ".")


    def get_lines(self, name):
        """Get a list of lines from the Die Hard film script for the given
        charater's name.
        """
        BEGIN_RE = re.compile(r"^\s+%s\s+" % name)
        END_RE = re.compile(r"^\s*%")
        lines = []
        script_path = "dieHard.txt"
        if not os.path.exists(script_path):
            script_path = os.path.join(BOT_DATA_DIR, PLUGINS_SUBDIR,
                                       "err-diehardbot", "dieHard.txt")
        with open(script_path) as f:
            in_line_block = False
            line = []
            for l in f:
                if BEGIN_RE.search(l):
                    in_line_block = True
                    line = []
                if END_RE.search(l):
                    if in_line_block and len(line):
                        raw_line = " ".join(line)
                        # Remove (sotto voce) direction.
                        lines.append(re.subn(r"[ ]?\(.*?\)", "", raw_line)[0])
                    in_line_block = False
                if in_line_block:
                    if not BEGIN_RE.search(l):
                        line.append(l.strip())
        return lines


if __name__ == "__main__":
    dh = DieHard()
    for c in DieHard.CHARACTERS:
        print "%s: %s" % (c, dh.get_random(c))
