#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import irc
import modules

try:
    network = sys.argv[3]
    serverport = 6667
    god = sys.argv[2]
    if len(sys.argv) > 4:
        serverport = int(sys.argv[4])

    bot = irc.Bot(network, serverport, sys.argv[1], 'pantterin botti')
    bot.addGod(god)
    
    while 1:
        if bot.cycle():
            reload(irc)
            copy = getattr(irc, 'Bot')
            bot.__class__ = copy
            print '\n\033[37;41m*** RELOADED MODULES ***\033[0m\n'
except IndexError:
    print 'Usage: nux.py <nick> <god> <network> [<port>]'
