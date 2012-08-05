import time

lastwhois = 0

nicks = ['zee']
last_idles = [0]
checktime = 30

def whois(bot):
    global lastwhois
    global last_idles
    if time.time() > lastwhois + checktime:
        lastwhois = time.time()
        for nick in nicks:
            bot.send('WHOIS '+nick+' '+nick)
    
    if bot.getCommand() == '317':
        nick = bot.getLine().split()[3]
        if nick in nicks:
            last_idle = last_idles[nicks.index(nick)]
            idle = int(bot.getLine().split()[4])
            print nick + ': '+str(idle)
            if idle < last_idle + checktime: # failaa koska irkista ei tuu dataa checktimen tiheydella
                bot.notice('pantteri', nick+': '+str(idle))
                last_idles[nicks.index(nick)] = idle

functions = [whois]
