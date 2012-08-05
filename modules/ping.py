#!/usr/bin/python
# -*- coding: UTF-8 -*-

def ping(bot):
    if bot.getMessage().startswith('ping '):
        bot.response('pong '+bot.getMessage()[5:])
    elif bot.getMessage() == 'ping':
        bot.response('pong')

functions = [ping]
