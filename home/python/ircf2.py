import socket
import time

#network = raw_input("Network: ") 
network = '194.197.235.247'
port = 6667
nick = "tews" #raw_input("Nick: ")
user = "tewe" #raw_input("User: ")
ircname = "tewe" # raw_input("Ircname: ")
channel = "ylis" #raw_input("Channel: #")
message = "tuska" # raw_input("Message: ")

while True:
	irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
	print("connecting...")
	irc.connect ( ( network, port ) )
	irc.send ( 'NICK ' + nick  + '\r\n' )
	irc.send ( 'USER ' + user + ' PyIRC PyIRC :' + ircname + '\r\n' )
	print("connected")
	irc.send ( 'JOIN #' + channel + '\r\n' )
	
	time.sleep(0.5)
	for i in range(6):
#		irc.send ( 'PRIVMSG #' + channel + ' ' + message + '\r\n' )
		irc.send ( 'KNOCK #' + channel + ' ' + message + '\r\n' )
	time.sleep(0.5)
	irc.send ( 'PART #' + channel+   '\r\n' )
	irc.send ( 'QUIT\r\n' )
	irc.close()
	print("done")

