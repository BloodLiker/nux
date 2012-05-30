import socket
import time

#network = raw_input( 'Network: ' ) 
network = '194.197.235.247'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

irc.connect ( ( network, port ) )
nick = raw_input( 'Nick: ' )
irc.send ( 'NICK ' + nick + '\r\n' )
irc.send ( 'USER ' + raw_input( 'User: ' ) + ' PyIRC PyIRC :' + raw_input( 'Ircname: ' ) + 'x\r\n' 
)
channel = raw_input( 'Channel: #' )
irc.send ( 'JOIN #' + channel + '\r\n' )

#time.sleep(0.5)
while 1:
	msg = raw_input( '<' + nick + '> ' )
	
	irc.send ( 'PRIVMSG #' + channel + ' ' + raw_input() + '\r\n' )
#irc.send ( 'PART #' + channel+   '\r\n' )
#irc.send ( 'QUIT\r\n' )
#irc.close()
#print("done")
