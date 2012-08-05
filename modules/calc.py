import http
import urllib2
import traceback
reload(http)

googletext = '\003[\00312G\00304o\00308o\00312g\00309l\00304e\003]'

def calc(bot):
    message = bot.getMessage()
    if message.startswith('!calc '):
        expression = message[6:]
        try:
            #http://www.google.com/ig/calculator?hl=en&q=1+1
            google = http.gethttp('http://www.google.com/search?ie=UTF-8&q='+urllib2.quote(expression))
#            google = http.gethttp('http://www.google.com/ig/calculator?hl=en&q='+urllib2.quote(expression))
            #print 'http://www.google.com/search?q='+urllib2.quote(expression)
            #print google
#            answer = google[google.find('rhs: "')+6:]
#            answer = answer[:answer.find('",')]
#            if answer:
#                bot.response('\00314[\00312G\00304o\00308o\00312g\00309l\00304e\00314]\00300 '+expression+' = '+answer)
            if google.find('<h2 class="r" dir="ltr"') != -1:
                answer = google[google.find('class="r" dir="ltr"'):]
                answer = answer[answer.find('>')+1:answer.find('</h2>')]
                answer = answer.replace('<sup>', '^(').replace('</sup>', ')')
                print repr(answer)
                answer = http.unescape(answer.decode("UTF-8"))
                print repr(answer)#.encode("UTF-8")
                '''f = open('error.log', 'w')
                f.write(answer)
                for i in answer:
                    f.write(str(ord(i))+i+' ')
                    
                    print ord(i)
                f.close()'''
                bot.response((googletext+' \002'+answer))
            else:
                bot.response(googletext+' \002\00304Could not calculate!')

        except:
            print 'EXCEPTION WITH CALCULATION "'+expression+'"'
            traceback.print_exc()
            bot.response(googletext+' \00305Could not calculate!')

functions = [calc]
