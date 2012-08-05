#!/usr/bin/python
# -*- coding: UTF-8 -*-

def isDigit(character):
    if character == '0':
        return True
    elif character == '1':
        return True
    elif character == '2':
        return True
    elif character == '3':
        return True
    elif character == '4':
        return True
    elif character == '5':
        return True
    elif character == '6':
        return True
    elif character == '7':
        return True
    elif character == '8':
        return True
    elif character == '9':
        return True
    else:
        return False

def printcolor(irctext):
    text = ''
    add = ''
    normaltext = True
    bold = False
    underline = False
    inverse = False
    colorbold = False
    fgcolorcode = 0
    colorchar = 0

    for character in irctext:
        if colorchar == 2 and isDigit(character):
            fgcolorcode = character
            normaltext = False
            if character == '0' or character == '1':
                colorchar = 1
            else:
                colorchar = 0
           # continue

        elif colorchar == 1 and isDigit(character):
            colorchar = 0
            normaltext = False
            if fgcolorcode == '0':
                fgcolorcode = character
            else:
                fgcolorcode = fgcolorcode + character
            
        elif colorchar == 2:
            add = character
            normaltext = False
            fgcolorcode = ''
            colorchar = 0

        if 1==1 or colorchar == 0:
            if character == '\002':
                bold = not bold
                normaltext = False
            elif character == '\037':
                underline = not underline
                normaltext = False
            elif character == '\026':
                inverse = not inverse
                normaltext = False
            elif character == '\003':
                colorchar = 2
            elif normaltext:
                text = text + character

        if not normaltext:
            normaltext = True
            text = text + '\033[0'
            if fgcolorcode in ['0','4','8','9','11','12','13','14']:
                colorbold = True
            if bold or colorbold:
                text = text + ';1'
                colorbold = False
            if underline:
                text = text + ';4'
            if inverse:
                text = text + ';7'
            if fgcolorcode:
                    #black
                if fgcolorcode == '1' or fgcolorcode == '14':
                    text = text + ';30'
                    #red
                elif fgcolorcode == '5' or fgcolorcode == '4':
                    text = text + ';31'
                    #green
                elif fgcolorcode == '3' or fgcolorcode == '9':
                    text = text + ';32'
                    #yellow
                elif fgcolorcode == '7' or fgcolorcode == '8':
                    text = text + ';33'
                    #blue
                elif fgcolorcode == '2' or fgcolorcode == '12':
                    text = text + ';34'
                    #magenta
                elif fgcolorcode == '6' or fgcolorcode == '13':
                    text = text + ';35'
                    #cyan
                elif fgcolorcode == '10' or fgcolorcode == '11':
                    text = text + ';36'
                    #white
                elif fgcolorcode == '15' or fgcolorcode == '0':
                    text = text + ';37'
            text = text+'m'
            text = text + add
            add = ''

    print text+'\033[0m'

