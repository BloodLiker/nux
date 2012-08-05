#!/usr/bin/python
# -*- coding: UTF-8 -*-

import http
import re
reload(http)

def (bot):
    if bot.getMessage().startswith('!wiki '):
        wikipedia = http.gethttp('http://en.wikipedia.org/wiki/'+http.quote(bot.getMessage()[6:]))
        paragraph = wikipedia[wikipedia.find('<p>'):]
        paragraph = paragraph[:paragraph.find('</p>')]
        bot.response(http.printable(http.unescape(http.styleHTML(paragraph).decode('UTF-8'))), 1)

functions = [wiki]
