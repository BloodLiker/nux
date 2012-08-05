#!/usr/bin/python
# -*- coding: UTF-8 -*-

import fnmatch

#autoopUsers = ['apalmu', 'apouru', 'cshakes', 'ehelenius', 'jaakaappi', 'jimberg', 'jjantunen', 'jlappi', 'jtofferi', 'kivi', 'kkinnunen', 'kvoutilain', 'llaaki', 'nassikka', 'pantteri', 'ptoivanen', 'rolli', 'rraty', 'rvilppula', 'susku', 'zee']
channels = {
'#kvantit':
        ['*!apalmu@evo.paivola.fi',
         '*!apouru@evo.paivola.fi',
         '*!cshakes@evo.paivola.fi',
         '*!ehelenius@evo.paivola.fi',
         '*!evuojolain@evo.paivola.fi',
         '*!jaakaappi@evo.paivola.fi',
         '*!jijas@evo.paivola.fi',
         '*!jimberg@evo.paivola.fi',
         '*!jjantunen@evo.paivola.fi',
         '*!jlappi@evo.paivola.fi',
         '*!jseppala@evo.paivola.fi',
         '*!jtofferi@evo.paivola.fi',
         '*!juniori@evo.paivola.fi',
         '*!kivi@evo.paivola.fi',
         '*!kkinnunen@evo.paivola.fi',
         '*!kvoutilain@evo.paivola.fi',
         '*!llaaki@evo.paivola.fi',
         '*!mijas@evo.paivola.fi',
         '*!mkauppila@evo.paivola.fi',
         '*!nassikka@evo.paivola.fi',
         '*!pantteri@evo.paivola.fi',
         '*!phaelthor@evo.paivola.fi',
         '*!ptoivanen@evo.paivola.fi',
         '*!rhaapasuo@evo.paivola.fi',
         '*!rolli@evo.paivola.fi',
         '*!rraty@evo.paivola.fi',
         '*!rvilppula@evo.paivola.fi',
         '*!spoyri@evo.paivola.fi',
         '*!susku@evo.paivola.fi'],
'#nux': 
        ['*!pantteri@evo.paivola.fi',
         'TK009!*@*.paivola.fi'],
'#pingishuone':
        ['*!pantteri@evo.paivola.fi',
         '*!tkinnunen@evo.paivola.fi',
         '*!jimberg@evo.paivola.fi',
         '*!kivi@evo.paivola.fi',
         '*!apalmu@evo.paivola.fi',
         '*!jaakaappi@evo.paivola.fi']}

def autoop(bot):
    if bot.getCommand() == 'JOIN':
        channel = bot.getTrailing()
        user = bot.getSender()
        if channel in channels:
            for mask in channels[channel]:
                if fnmatch.fnmatch(user, mask):
                    bot.send('MODE '+channel+' +o '+bot.getSenderNick())
        #if user[user.find('@')+1:] == 'evo.paivola.fi' and user[user.find('!')+1:user.find('@')] in autoopUsers:
            #bot.send('MODE #kvantit +o '+bot.getSenderNick())

functions = [autoop]
