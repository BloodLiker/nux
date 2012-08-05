#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import http
import traceback
reload(http)

def slogan(bot):
    message = bot.getMessage()
    if message.startswith('!slogan '):
        data = http.gethttp('http://www.sloganmaker.com/sloganmaker.php?user='+urllib2.quote(message[8:])).split('\n')
        for line in data:
            if line.find("<p>") != -1:
                slogan = http.cleanHTML(line)
                print slogan
                bot.response(slogan)
                break

def hate(bot):
    message = bot.getMessage()
    if message.startswith('!hate '):
        data = http.gethttp('http://www.sloganmaker.com/hate/sloganmaker.php?user='+urllib2.quote(message[6:])).split('\n')
        for line in data:
            if line.find("<p>") != -1:
                hate = http.cleanHTML(line)
                print hate
                bot.response(hate)
                break

functions = [slogan, hate]
