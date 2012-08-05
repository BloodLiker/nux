#!/usr/bin/python
# -*- coding: UTF-8 -*-

import http
import time
import traceback
reload(http)

def title(bot):
    message = bot.getMessage()
    if message.find('://') != -1:
        for link in message.split():
            if link.find('http://') != -1 or link.find('https://') != -1:
                try:
                    realurl = http.geturl(link)
                    if realurl.find('://www.youtube.com/watch') != -1:
                        data = http.gethttp(realurl)
                        bot.response(youtube(data))
                    else:
                        rawdata = http.open(realurl)
                        data = ''.join(rawdata)
                        headers = rawdata.info()
                        if headers.getheaders('Content-Type')[0].startswith('text/html'):
                            if data.find('<title>') != -1 and data.find('</title>') != -1:
                                title = data[data.find('<title>')+7:]
                                title = title[:title.find('</title>')]
                                print 'Title: '+http.unescape(http.cleanHTML(title))+' (at '+host(realurl)+')'
                                #try:
                                bot.response('Title: '+http.unescape(http.cleanHTML(title))+' (at '+host(realurl)+')')
                                #except:
                                    #bot.response('Title: '+http.unescape(http.cleanHTML(title)).encode('UTF-8')+' (at '+host(realurl)+')')

                            else:
                                bot.response('No title (at '+host(realurl)+')')

                        else:
                            content_length = '???'
                            if len(headers.getheaders('Content-Length')) > 0:
                                content_length = str(round(int(headers.getheaders('Content-Length')[0])/1024.0,1))+' KB'
                            else:
                                content_length = '???' 
                            info = '['+content_length+' file, type: '+headers.getheaders('Content-Type')[0]+']'
                            bot.response(info+' (at '+host(realurl)+')')

                    if realurl != link:
                        bot.response('Direct link: '+realurl)
                    if len(link) > 70 and not message.startswith('!short '):
                        short = http.gethttp('http://www.dy.fi/?c=redir_add&bml=1&url='+http.quote(realurl))
                        if short.find('">http://dy.fi/') != -1:
                            short = short[short.find('">http://dy.fi/')+2:]
                            short = short[:short.find('<')]
                            bot.response('Short link: '+short)

                except:
                    traceback.print_exc()
                        
def short(bot):
    if bot.getMessage().startswith('!short '):
        url = http.geturl(bot.getMessage()[7:]) 
        short = http.gethttp('http://www.dy.fi/?c=redir_add&bml=1&url='+http.quote(url))
        if short.find('">http://dy.fi/') != -1:
            short = short[short.find('">http://dy.fi/')+2:]
            short = short[:short.find('<')]
            bot.response('Short link: '+short)
        else:
            bot.response('Error')

def host(url):
    hostStart = url.find('://')+3
    hostEnd = url[hostStart:].find('/')+hostStart
    return url[hostStart:hostEnd]

def hilightHost(url):
    hostStart = url.find('://')+3
    hostEnd = url[hostStart:].find('/')+hostStart
    return url[:hostStart]+'\002'+url[hostStart:hostEnd]+'\002'+url[hostEnd:]

def youtube(data):
    title = data[data.find('<meta name="title" content="')+28:]
    title = http.cleanHTML(title[:title.find('">')])

    duration = data[data.find('<meta itemprop="duration" content="PT')+37:]
    duration = http.cleanHTML(duration[:duration.find('">')])
    uploader = data[data.find('class="yt-user-name author"'):]
    uploader = uploader[uploader.find('>')+1:]
    uploader = uploader[:uploader.find('<')]
    minutes = duration[:duration.find('M')]
    seconds = duration[duration.find('M')+1:duration.find('S')]
    if int(minutes) > 59:
        hours = int(minutes)/60
        if int(minutes)%60 < 10:
            minutes = str(hours)+':0'+str(int(minutes)%60)
        else:
            minutes = str(hours)+':'+str(int(minutes)%60)
    if int(seconds) < 10:
        seconds = '0'+seconds

    return '\00315[\00300You\00304Tube\00315]\003 \002'+title+'\002 ('+minutes+':'+seconds+') by '+uploader

functions = [short, title]
