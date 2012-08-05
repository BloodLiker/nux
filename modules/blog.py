#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

allowedNicks = ['pantteri', 'Kivi', 'juniori', 'Jukkeri', 'jaakaappi', 'TK009', 'kokos']

def blog(bot):
    if bot.getSenderNick() in allowedNicks and bot.getMessage().startswith('!blog '):
        f = open('/home/fotonit/pantteri/public_html/index.html', 'r')
        page = f.read()
        f.close()
        #print page
        start = page[:page.find('<span class="blog">')+19]
        end = page[page.find('<span class="blog">')+19:]
        new = '\n\t\t\t<p>'+bot.getMessage()[6:].replace('<', '&lt;').replace('>', '&gt;')+'<br />\n\t\t\t<i id="timestamp">- '+bot.getSenderNick()+' '+date()+'</i></p>\n'
        bot.response(date())
        bot.message('pantteri', bot.getSenderNick()+' - '+date())
        f = open('/home/fotonit/pantteri/public_html/index.html', 'w')
        f.write(start+new+end)
        f.close()

def date():
    date = time.strftime('%a %-d. %b %Y %R')
    en = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fi = ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su', 'tammikuuta', 'helmikuuta', 'maaliskuuta', 'huhtikuuta', 'toukokuuta', 'kesäkuuta', 'heinäkuuta', 'elokuuta', 'syyskuuta', 'lokakuuta', 'marraskuuta', 'joulukuuta']
    for eni, fii in zip(en, fi):
        date = date.replace(eni, fii)
    return date

functions = [blog]
