# http://ubuntuforums.org/showthread.php?t=1493702
# v_1.5

# NickServ stuff identify update etc
# !maze
# !ban kick when joins (ban 3s autojoin client)
# scands
# !ud urban dictionary
# !ef english-finnish
# !fe finnish-english
# !pic (spam)
# !ascii art
# !figlet (spam)
# draw ascii art when someone says OhCrap.png etc (spam)
# notice if caps (XD IRC DNS :D HS)
# !paste

import socket
import re
import time
import urllib
import httplib
import HTMLParser

network = 'irc.paivola.fi'
port = 6667
target = 'Felix'
ownnick = 'nux'
gods = ['Felix']

def send( cats ):
	if cats.count( "\r\n" ) > 4:
		print 'too many lines'
		# todo: rewrite this awful shit
		# todo: send rest of lines private (code to !wa section)
		irc.send( cats.split( "\r\n" )[0] + '\r\n' )
		irc.send( cats.split( "\r\n" )[1] + '\r\n' )
		irc.send( cats.split( "\r\n" )[2] + '\r\n' )
		irc.send( cats.split( "\r\n" )[3] + ' [ more... ]\r\n' )
	else:
		irc.send( cats )
	print '^^ ' + cats

topicLock = False
topic = ''
h = HTMLParser.HTMLParser()
irc = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
irc.connect( ( network, port ) )
print ':> ' + irc.recv( 4096 )
send( 'NICK '+ownnick+'\r\n' )
send( 'USER nux h h :Felixin IRC botti\r\n' )
send( 'PRIVMSG '+target+':Mui.\r\n' )

# main loop
while True:
	data = irc.recv( 4096 )
	print ':> ' + data + '---'

	# PING
	if data.find( 'PING' ) != -1:
		send( 'PONG ' + data.split() [ 1 ] + '\r\n' )

	# todo: VERSION

	# Where does the message come from (channel or nick)
	if re.match( '^:[^!]*![^@]*@[^ ]* PRIVMSG #', data ):
		target = data.split()[2]
	elif re.match( '^:[^!]*![^@]*@[^ ]* PRIVMSG ' + ownnick, data ):
		target = data[ 1 : data.find( '!' ) ]

	nick = data[ 1:data.find( '!' ) ]

	# Commands
	if re.match( '^:[^!]*![^@]*@[^:]*:!', data ):
		cmd = data[ data[1:].find( ':' ) + 3: data.find( '\r\n' ) ]
		arg = ''
		if cmd.find( ' ' ) != -1:
			arg = cmd[ cmd.find( ' ' ) + 1: ]
			cmd = cmd[ :cmd.find( ' ' ) ]
		print 'nick = "' + nick + '"'
		print 'cmd = "' + cmd + '"'
		print 'arg = "' + arg + '"'

		# God commands
		if nick in gods:

			print '== GOD =='

			# quit
			if cmd == 'quit':
				print 'quit'
				# todo: send privmsg to all channels joined
				send( 'PRIVMSG '+target+' :okei.. :<\r\n' )
				send( 'QUIT :brb kuolen\r\n' )
				time.sleep(2)
				quit()

			# nick
			if cmd == 'nick':
				send( 'NICK ' + arg + '\r\n' )
				ownnick = arg
				print 'ownnick = "' + ownnick + '"'

			# join
			if cmd == 'join':
				if arg[0] == '#' and arg.find( ',' ) == -1:
					send( 'JOIN ' + arg + '\r\n' )
				else:
					send( 'PRIVMSG '+target+' :huono kanava\r\n' )
				# add channel to list

			# part
			if cmd == 'part':
				send( 'PART ' + arg + '\r\n' )
				# remove channel from list

			# make some one a god!
			if cmd == 'god':
				if len(arg.split()) > 0:
					# 1 line
					arg = arg.split()[0]
					if arg in gods:
						send( 'PRIVMSG '+target+' :'+arg+' on jo jumala!\r\n' )
					else:
						gods.append(arg)
						send( 'PRIVMSG '+target+' :'+arg+' on nyt jumala!\r\n' )
				else:
					send( 'PRIVMSG '+target+' :ei ole nikki\r\n' )

			# say
			if cmd == 'say':
				# current PRIVMSG #channel message
				# correct PRIVMSG #channel :message
				send( 'PRIVMSG ' + arg + '\r\n' )

			# topic lock
			# todo: different settings for different channels
			if cmd == 'topic':
				if len(arg) == 0:
					topicLock = False
				else:
					topicLock = True
					topic = arg
					send( 'TOPIC '+target+' :'+topic+'\r\n' )

			# mode
			if cmd == 'mode':
				send( 'MODE ' + arg + '\r\n' )

			# help
			if cmd == 'help':
				send( 'PRIVMSG ' + target + ' :jumalakomennot: !quit !nick !join !part !god !say !topic !mode\r\n' )
				send( 'PRIVMSG ' + target + ' :kuolevaisten komennot: !wa !day !help\r\n' )

			# devil
			if cmd == 'devil':
				if len(arg.split()) > 0:
					arg = arg.split()[0]
					if arg in gods:
						gods.remove(arg)
						send( 'PRIVMSG '+target+' :'+arg+' ei ole enaa jumala!\r\n' )
					else:
						send( 'PRIVMSG '+target+' :'+arg+' ei ollut jumala!\r\n' )
				else:
					send( 'PRIVMSG '+target+' :huono nikki\r\n' )

		# Non-admin commands

		else:
			# help
			if cmd == 'help':
				send( 'PRIVMSG ' + target + ' :kuolevaisten komennot: !wa !day !help\r\n' )

		# Wolfram|Alpha
		if cmd == 'wa':
			result = "ei tuloksia"
			conn = httplib.HTTPConnection("www.wolframalpha.com")
			conn.request("GET", "/input/?i=" + urllib.quote_plus(arg))
			r1 = conn.getresponse()
			wa = r1.read()
			conn.close()
			waLines = wa.split("\n")
			n = 0
			for line in waLines:
				if line.find('stringified') != -1:
					n+=1
					if(n == 2):
						result = line.split('"')[ 3 ].replace("\\n","\r\n")
			print 'wa: ' + result
			# todo: make a nice array
			send( 'PRIVMSG '+target+' :'+
			result.replace("\n", "\nPRIVMSG "+target+" :wa: ")+'\r\n' )

		# What's special in today
		if cmd == 'day':
			conn = httplib.HTTPConnection("en.wikipedia.org")
			conn.request("GET", "/wiki/Main_Page")
			r1 = conn.getresponse()
			fun = r1.read()
			conn.close()
			funLines = fun.split("\n")
			for line in funLines:
				if line.find('<p><b><a href="/wiki/') != -1:
					fun = re.sub( r'<[^>]*>', '', line )
			print fun
			send( 'PRIVMSG '+target+' :'+fun+'\r\n' )

		# Urban Dictionary
		if cmd == 'ud':
			conn = httplib.HTTPConnection("www.urbandictionary.com/")
			conn.request("GET", "/define.php?term=" + arg)
			r1 = conn.getresponse()
			sola = r1.read()
			conn.close()
			saloLines = sola.split("\n")
			for line in saloLines:
				if line.find('class="definition"') != -1:
					sola = re.sub( r'<[^>]*>', '', line )
			print sola
			send( 'PRIVMSG '+target+' :'+sola+'\r\n' )

	# Messages
	elif re.match( '^:[^!]*![^@]*@[^ ]* PRIVMSG', data ):
		msg = data[ data[1:].find( ':' ) + 2: data.find( '\r\n' ) ]
		print 'msg = "' + msg + '"'
#		if msg == 'Mui.':
#			send( 'PRIVMSG '+target+' :Mui.\r\n' )
		if msg == 'Mui. ' + ownnick:
			send( 'PRIVMSG '+target+' :Mui. ' + nick + '\r\n' )
#		if msg.find( 'sola' ) != -1:
#			send( 'PRIVMSG '+target+' :sola!\r\n' )
#		if msg.lower() == 'ok':
#			send( 'PRIVMSG '+target+' :ok\r\n' )
		if msg.find( 'http://' ) != -1:
			url = data.split( 'http://' )[ 1 ].split()[ 0 ]
			conn = httplib.HTTPConnection(url[:url.find("/")])
			conn.request("GET", url[url.find("/"):])
			r1 = conn.getresponse()
			topic = r1.read()
			conn.close()
			print h.unescape( topic[topic.find("<title>")+7:topic.find("</title>")])
#			send( 'PRIVMSG '+target+' :'+ topic[topic.find("<title>")+7:topic.find("</title>")].replace( "&auml;","a").replace( "&ouml","o" ) +'\r\n' )
#		if msg.startswith( ownnick ):
#			send( 'PRIVMSG '+target+' :'+nick+': hm?\r\n' )

	# Auto join
	elif re.match( '^:[^!]*![^@]*@[^ ]* KICK', data ):
		target = data.split()[2]
		send( 'JOIN '+target+'\r\n' )

	# Topic lock
	elif re.match( '^:[^!]*![^@]*@[^ ]* TOPIC', data ) and topicLock:
		if not re.match( '^:'+ownnick+'![^@]*@[^ ]* TOPIC', data ):
			target = data.split()[2]
			send( 'TOPIC '+target+' :'+topic+'\r\n' )

	# Mui. when someone joins
	elif re.match( '^:[^!]*![^@]*@[^ ]* JOIN', data ):
		target = data.split()[2][1:]
		if re.match( '^:'+ownnick, data ):
			send( 'PRIVMSG '+target+' :Mui.\r\n' )
		else:
			send( 'PRIVMSG '+target+' :Mui. '+nick+'\r\n' )
