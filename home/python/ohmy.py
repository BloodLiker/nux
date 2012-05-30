import ircMath
import socket

network = 'irc.paivola.fi'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
irc.recv ( 4096 )
irc.send ( 'NICK ohmy\r\n' )
irc.send ( 'USER ohmy PyIRC PyIRC :kisulin botti\r\n' )
irc.send ( 'JOIN #pyirc\r\n' )
irc.send ( 'PRIVMSG #pyirc :Mui.\r\n' )
while True:
	data = irc.recv ( 4096 )
	if data.find ( 'PING' ) != -1:
		irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
	elif data.find ( 'PRIVMSG' ) != -1:
		message = ':'.join ( data.split ( ':' ) [ 2: ] )
		if message.lower().find ( '%ohmy' ) == 0:
			nick = data.split ( '!' ) [ 0 ].replace ( ':', '' )
			destination = ''.join ( data.split ( ':' ) [ :2 ] ).split ( ' ' ) [ -2 ]
			function = message.split ( ' ' ) [ 1 ]
			if function == 'exec':
				try:
                                        args = message.split ( ' ' ) [ 2: ]
                                        print ( args )
					print ( args [ 2 : 4 ] )
					#exec ( args [ 2 : -6 ] )
                                        #irc.send ( 'PRIVMSG ' +  destination + ' :' + nick + ': ' + s$
                                except:
                                        pass
				
                        if function == 'calc':
				try:
					args = message.split ( ' ' ) [ 2: ]
					solution = ircMath.arithmatic ( args )
					irc.send ( 'PRIVMSG ' +  destination + ' :' + nick + ': ' + solution + '\r\n' )
				except:
					pass
			if function == 'sin':
				try:
					args = message.split ( ' ' ) [ 2: ]
					solution = ircMath.sine ( args )
					irc.send ( 'PRIVMSG ' +  destination + ' :' + nick + ': ' + solution + '\r\n' )
				except:
					pass
			if function == 'cos':
				try:
					args = message.split ( ' ' ) [ 2: ]
					solution = ircMath.cosine ( args )
					irc.send ( 'PRIVMSG ' +  destination + ' :' + nick + ': ' + solution + '\r\n' )
				except:
					pass
			if function == 'tan':
				try:
					args = message.split ( ' ' ) [ 2: ]
					solution = ircMath.tangent ( args )
					irc.send ( 'PRIVMSG ' +  destination + ' :' + nick + ': ' + solution + '\r\n' )
				except:
					pass


	
