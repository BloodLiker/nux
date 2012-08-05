#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import http
import os

def day(bot):
    # What's special in today
    if bot.getMessage() == '!day':
        date = time.strftime('%B_%e').replace(' ','')
        data = http.gethttp('http://en.wikipedia.org/wiki/'+date).split('\n')
        fun = []
        add = False
        for line in data:
            if add:
                if line.find('Births</span></h2>') != -1:
                    break
                else:
                    print line
                    fun.append(http.cleanHTML(line))
            if line.find('Events</span></h2>') != -1:
                add = True
                print 'adding...'

        # if `date +%-d.%-m.` outputs '-d.-m.', replace '%-d.%-m.' with '%d.%m.'
        # random.choice() did not work
        print fun
        bot.response(time.strftime('%-d.%-m.') + fun[int((time.time()%1*10000000000000000)%(len(fun)-2))+1])

def ping(bot):
    if bot.getMessage().startswith('ping '):
        bot.response('pong '+bot.getMessage()[5:])
    elif bot.getMessage() == 'ping':
        bot.response('pong')

def excessflood(bot):
    if bot.getMessage() == '!quit-e' and bot.isGod(bot.getSenderNick()):
        for i in range(100):
            bot.message(bot.nickname, 'excess flood '*1000)

def clientexited(bot):
    if bot.getMessage() == '!quit-c' and bot.isGod(bot.getSenderNick()):
        quit()

def bigmatix(bot):
    if bot.getMessage() == '!bigmatix' and bot.isGod(bot.getSenderNick()):
        bigmatix = os.popen('cat /home/fotonit/pantteri/ascii/bigmatix.txt').read().split('\n')
        for line in bigmatix:
            bot.response(line)
            time.sleep(3.5)

functions = [day, ping, excessflood, clientexited]
