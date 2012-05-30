import socket
import time

network = '194.197.235.247'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

print("connecting...")
irc.connect ( ( network, port ) )
irc.send ( 'NICK tews\r\n' )
irc.send ( 'USER tahan_ei_voi_laittaa_roottia PyIRC PyIRC :ASDF\r\n' )
print("connected")
irc.send ( 'JOIN #pyirc\r\n' )

#time.sleep(0.5)
for i in range(6):
        irc.send ( 'PRIVMSG #pyirc asdf\r\n' )
irc.send ( 'PART #pyirc\r\n' )
irc.send ( 'QUIT\r\n' )
time.sleep(0.5)
irc.close()
print("done")
