import socket
import time

network = raw_input("Network: ") 
#network = '194.197.235.247'
port = 6667
nick = raw_input("Nick: ")
user = raw_input("User: ")
ircname = raw_input("Ircname: ")
channel = raw_input("Channel: #")
message = raw_input("Message: ")

irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
print("connecting...")
irc.connect ( ( network, port ) )
irc.send ( 'NICK ' + nick  + '\r\n' )
irc.send ( 'USER ' + user + ' PyIRC PyIRC :' + ircname + '\r\n' )
print("connected")
irc.send ( 'JOIN #' + channel + '\r\n' )

irc.send ( 'PRIVMSG ' + raw_input( '/msg ') + '\r\n' )
time.sleep ( 5 )
data = irc.recv ( 4096 )
irc.send ( 'PRIVMSG NickServ identify ' + raw_input( 'NickServ password:') + '\r\n' )
time.sleep ( 5 )
data = irc.recv ( 4096 )
print ( data )

while True:
	irc.send ( 'PRIVMSG #' + channel + ' ' + message + '\r\n' )
