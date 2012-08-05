import http

def fweather(bot):
    if bot.getMessage().startswith('!fweather'):
        FUCKINGPLACE = bot.getMessage()[9:]
        try:
            if len(FUCKINGPLACE) > 1:
                FUCKINGPLACE = FUCKINGPLACE[1:]
                FUCKINGDATA = http.gethttp('http://thefuckingweather.com/?where='+http.quote(FUCKINGPLACE)+'&unit=c')
            else:
                FUCKINGDATA = http.gethttp('http://thefuckingweather.com/?unit=c&random=True')
            FUCKINGWEATHER = FUCKINGDATA[FUCKINGDATA.find('<div class="content">')+21:FUCKINGDATA.find('</>')]

            if FUCKINGDATA.find('I CAN&#39;T FIND THAT SHIT') == -1:
                FUCKINGTEMPERATURE = http.cleanHTML(http.classContent(FUCKINGWEATHER, 'temperature', 'class', '</p>'))
                FUCKINGLOCATION = http.classContent(FUCKINGDATA, 'locationDisplaySpan', 'id')
                FUCKINGREMARK = http.classContent(FUCKINGWEATHER, 'remark')
                FUCKINGFLAVOR = http.classContent(FUCKINGWEATHER, 'flavor')
                
                bot.response(http.unescape('\00312['+FUCKINGLOCATION+'] \00304\002'+FUCKINGTEMPERATURE+' \00308'+FUCKINGREMARK+' \002\00311['+FUCKINGFLAVOR+']').encode("UTF-8"))

            else:
                bot.response('\002\00304INVALID FUCKING LOCATION')
                            
        except Exception as FUNCKINGEXCEPTION:
            print 'FUCKING EXCEPTION WITH THE FUCKING WEATHER IN "'+FUCKINGPLACE+'"'
            print FUNCKINGEXCEPTION
            print FUCKINGPLACE
            bot.response('\002\00304INVALID FUCKING LOCATION')

functions = [fweather]
