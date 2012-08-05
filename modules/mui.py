import time

lastmui = '24:00'

def mui(bot):
    #bot.addGod('pantteri')
    #print 'pantteri'
    if bot.getMessage().find('Mui.') != -1:
        global lastmui
        if lastmui != time.strftime('%R'):
            bot.response('\00309Mui.')
            print lastmui
            lastmui = time.strftime('%R')
    if bot.getCommand() == 'JOIN':
        bot.message(bot.getTrailing(), 'Mui. '+bot.getSenderNick())
        lastmui = time.strftime('%R')

#def kvantit(bot):
#    bot.send('JOIN #kvantit')

functions = [mui] #, kvantit]
