import socket
import string
import time
import sys

if sys.argv[1]:
	server = sys.argv[1]
port = 6667

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
print irc.recv(4096)

def send(data):
	for line in data.split("\r\n"):
		print line
		irc.send(line+"\r\n")
		time.sleep(0.5)
def join(channel, sender):
	if channel[0] == '#' and channel.find(',') == -1:
		send('JOIN '+channel+'\r\n')
	else:
		send('PRIVMSG '+sender+' :huono kanava\r\n')
def part(channel):
	send('PART '+channel+'\r\n')
def msg(to, msg):
	send("PRIVMSG "+to+" :"+msf)

send ("USER nux h h :kiltti botti (nux 2.0)")
send ("NICK nux")

while 1:
	ircmsg = irc.recv(4096).strip("\n\r")
	print ircmsg

	if ircmsg.startswith("PING :"):
		send("PONG :"+ircmsg.split("PING :")[1])
	
	nick = ''
	action = ''
	if ircmsg.split()[0].find("!") != -1:
		nick = ircmsg[1:].split("!")[0]
		action = ircmsg.split()[1]
	print "nick: " + nick
	print "action: " + action
	
	if action == "PRIVMSG" and ircmsg.split()[3].startswith(":!"):
		cmd = ircmsg.split()[3][2:]
		sender = nick
		if ircmsg.split()[2].startswith("#"):
			sender = ircmsg.split()[2]
		
		if cmd == "join": join(ircmsg.split()[4], sender)
		elif cmd == "part": part(ircmsg.split()[4])
		elif cmd == "quit": quit()
	elif action == "INVITE":
		join(ircmsg.split()[3][1:],"")		