#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import HTMLParser
import re

h = HTMLParser.HTMLParser()

def quote(text):
	return urllib2.quote(text).replace('/', '%2F')
	
def unescape(html):
    return h.unescape(html)

def cleanHTML(html):
	return printable(re.sub(' +',' ',re.sub(r'<[^>]*>','',html))).strip(' ')
	#return printable(html.translate(dict.fromkeys(range(32)))).strip(' ')

def styleHTML(html):
    htmltable = ['</b>', '<b>', '<u>', '</u>']
    irctable = ['\002', '\002', '\037', '\037']
    html = html.replace('<b>', '\002').replace('</b>', '\002').replace('<u>', '\037').replace('</u>', '\037')
    return re.sub(' +',' ',re.sub(r'<[^>]*>','',html)).strip(' ')

def printable(text):
    text = text.replace('\n',' ').replace('\r', ' ')
    return re.sub('[\x00-\x1f]','',text)

def open(url):
    try:
        print 'Fetching '+url
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        data = opener.open(url)
        print data.info()
        return data
    except Exception as e:
        print e

def gethttp(url):
    try:
        print 'Fetching '+url
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        data = opener.open(url)
        print data.info()
        return ''.join(data)
    except Exception as e:
        print e

def geturl(url):
    try:
        return ''.join(urllib2.urlopen(url).geturl())
    except Exception as e:
        print 'geturl Mozilla'
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        return ''.join(urllib2.urlopen(url).geturl())

def classContent(html, classname, type='class', end='<'):
	html = html[html.find(type+'="'+classname+'"'):]
	return html[html.find('>')+1 : html.find(end)]

#def table(html):
#    table = html[html.find('<table'):]

def cleanRow(html):
    row = []
    for column in html.split('<td'):
        row.append(cleanHTML(column[column.find('>')+1:column.find('</td>')]))
    return row[1:]

def row(html):
    row = []
    for column in html.split('<td'):
        row.append(column[column.find('>')+1:column.find('</td>')])
    return row[1:]


'''def unescape(html):
	unescaped = ''
	for part in html.split('&#'):
		try:
			unescaped += chr(int(part.split(';')[0]))+part.split(';')[1]
		except:
			unescaped += part
	return unescaped'''
