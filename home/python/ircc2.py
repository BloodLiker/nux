import socket
import time

#network = raw_input("Network: ") 
network = '194.197.235.247'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

print("connecting...")
irc.connect ( ( network, port ) )
irc.send ( 'NICK ' + raw_input("Nick: ") + '\r\n' )
irc.send ( 'USER ' + raw_input("User: ") + ' PyIRC PyIRC :' + raw_input("Ircname: ") + 'x\r\n' 
)
print("connected")
channel = raw_input("Channel: #")
irc.send ( 'JOIN #' + channel + '\r\n' )

time.sleep(0.5)
while 1:
#	print("rdy")
#	message = raw_input("[" + channel + "] ")
#	print("message received")
#	if len(message) > 0:
#		irc.send ( 'PRIVMSG #' + channel + ' ' + message + '\r\n' )
#		print("message sent")
	data = irc.recv ( 4096 )
#	print("data received")
	if data.find ( 'PING' ) != -1:
#		print("ping")
		irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
	elif data.find ( 'PRIVMSG' ) != -1:
#		print("privmsg")
		nick = data.split ( '!' ) [ 0 ].replace ( ':', '' )
		message = ':'.join ( data.split ( ':' ) [ 2: ] )
#		print nick + ':', message
		destination = ''.join ( data.split ( ':' ) [ :2 ] ).split ( ' ' ) [ -2 ]
		if destination == channel:
			destination = 'PRIVATE'
		print '[', destination, '] <', nick + '> ', message
#	elif data.find ( 'ACTION' ) != -1:
#		print '[', destination, 
	else:
#		print("something")
		print data
#irc.send ( 'PART #' + channel+   '\r\n' )
irc.send ( 'QUIT\r\n' )
irc.close()
print("done")
