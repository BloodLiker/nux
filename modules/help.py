#!/usr/bin/python 
# -*- coding: UTF-8 -*-

def showhelp(bot):
    if bot.getMessage() == '!help':
        print 'dest = '+bot.getDestination()
        print 'modules: ' + str(bot.modules)
        print 'functions: ' + str(bot.functions)
        bot.response("!help !ud !define !calc !slogan !hate !fweather !lj !blog !day !hex !unhex !wiki !short !base64 !unbase64")

def mui(bot):
    bot.addGod('pantteri')

functions = [showhelp]#, mui]
#lineCommands = {'!help': showhelp}
