ignores = ["yks"]

def ignore(bot):
    if bot.getSenderNick() in ignores:
        bot.line = 'H' # ignore the message
        print 'ignoring '+bot.getSenderNick()

def clientexited(bot):
    if bot.isGod(bot.getSenderNick()) and bot.getMessage() == '!quit-c':
        import os
        os.system('kill -9 $#')

def brokenpipe(bot):
    if bot.isGod(bot.getSenderNick()) and bot.getMessage() == '!quit-b':
        import socket
        import struct
        bot.connection.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
        #bot.connection.setdefaulttimeout(0)
        #bot.connection.shutdown(socket.SHUT_RD)
        #bot.reloadModules = bot.reload
        #bot.cycle = open
        #bot.modules.append('/')

functions = [ignore, clientexited, brokenpipe]
