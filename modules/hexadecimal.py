#!/usr/bin/python
# -*- coding: UTF-8 -*-

#import traceback
import base64
import http

def enhex(bot):
    if bot.getMessage().startswith('!hex '):
        integer = 0
        text = bot.getMessage()[5:]
        for char in text:
            integer |= ord(char)
            integer <<= 8
        integer >>= 8
        bot.response(str(hex(integer)).replace('L', ''))

def unhex(bot):
    if bot.getMessage().startswith('!unhex '):
        try:
            integer = int(bot.getMessage()[7:], 16)
            text = ''
            while integer > 0:
                text = chr(integer % 256) + text
                integer >>= 8
            bot.response(text.strip('\001'))
        except:
            #print traceback.print_exc()
            bot.response('error')

def base64en(bot):
    if bot.getMessage().startswith('!base64 '):
        bot.response(base64.b64encode(bot.getMessage()[8:]))

def base64de(bot):
    if bot.getMessage().startswith('!unbase64 '):
        try:
            bot.response(base64.b64decode(bot.getMessage()[10:]))
        except TypeError:
            bot.response('error')

def paste(bot):
    if bot.getMessage().startswith('!paste ') and bot.isGod(bot.getSenderNick()):
        try:
            data = http.gethttp(bot.getMessage()[7:])
            integer = int(data, 16)
            text = ''
            while integer > 0:
                text = chr(integer % 256) + text
                integer >>= 8
            bot.response(text.strip('\001'))
            bot.line = 'H'
        except:
            bot.response('error')

functions = [enhex, unhex, base64en, base64de, paste]
