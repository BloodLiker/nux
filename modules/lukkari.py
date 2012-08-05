import http
reload(http)

def lj(bot):
    if bot.getMessage().startswith('!lj'):
        #f = open('lukkari.html')
        #lukkari = f.read()
        #f.close()
        lukkari = http.gethttp('http://ranssi.paivola.fi/lj.php')
        today = lukkari[lukkari.find('<tr class="today">'):]
        tomorrow = today[today.find('<tr class="odd">'):]
        today = http.row(today[:today.find('</tr>')])
        tomorrow = http.cleanRow(tomorrow[:tomorrow.find('</tr>')])
        otsikko = http.row(lukkari[:lukkari.find('</tr>')])
        nuoret = otsikko[1]
        vanhat = otsikko[3]
        for i in range(len(today)):
            if not today[i] and i != 5:
                today[i] = 'luokka'
            else:
                if today[i].find('<span class="nrc">') != -1:
                    today[i] = '\00303'+http.cleanHTML(today[i])+'\003'
                elif today[i].find('<span class="koe">') != -1:
                    today[i] = '\00307'+http.cleanHTML(today[i])+'\003'
                elif today[i].find('<span class="vlh">') != -1:
                    today[i] = '\00306'+http.cleanHTML(today[i])+'\003'
                elif today[i].find('<span class="yo">') != -1:
                    today[i] = '\00304\002'+http.cleanHTML(today[i])+'\003\002'
                else:
                    today[i] = http.cleanHTML(today[i])

        bot.response(nuoret+': [\002Aamu:\002 '+today[1]+'] [\002IP1:\002 '+today[2]+'] [\002IP2:\002 '+today[3]+'] [\002Ilta:\002 '+today[4]+']')
        bot.response(vanhat+': [\002Aamu:\002 '+today[6]+'] [\002IP1:\002 '+today[7]+'] [\002IP2:\002 '+today[8]+'] [\002Ilta:\002 '+today[9]+']')
        if today[5]:
            bot.response('Muuta: '+today[5])

functions = [lj]
