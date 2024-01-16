#!/usr/bin/python3
# prints a string in uppercase followed by a new line

def uppercase(str):
    str_bis = ''
    for i in str:
        if ord(i) == 97:
            str_bis += 'A'
            continue
        if ord(i) == 98:
            str_bis += 'B'
            continue
        if ord(i) == 99:
            str_bis += 'C'
            continue
        if ord(i) == 100:
            str_bis += 'D'
            continue
        if ord(i) == 101:
            str_bis += 'E'
            continue
        if ord(i) == 102:
            str_bis += 'F'
            continue
        if ord(i) == 103:
            str_bis += 'G'
            continue
        if ord(i) == 104:
            str_bis += 'H'
            continue
        if ord(i) == 105:
            str_bis += 'I'
            continue
        if ord(i) == 106:
            str_bis += 'J'
            continue
        if ord(i) == 107:
            str_bis += 'K'
            continue
        if ord(i) == 108:
            str_bis += 'L'
            continue
        if ord(i) == 109:
            str_bis += 'M'
            continue
        if ord(i) == 110:
            str_bis += 'N'
            continue
        if ord(i) == 111:
            str_bis += 'O'
            continue
        if ord(i) == 112:
            str_bis += 'P'
            continue
        if ord(i) == 113:
            str_bis += 'Q'
            continue
        if ord(i) == 114:
            str_bis += 'R'
            continue
        if ord(i) == 115:
            str_bis += 'S'
            continue
        if ord(i) == 116:
            str_bis += 'T'
            continue
        if ord(i) == 117:
            str_bis += 'U'
            continue
        if ord(i) == 118:
            str_bis += 'V'
            continue
        if ord(i) == 119:
            str_bis += 'W'
            continue
        if ord(i) == 120:
            str_bis += 'X'
            continue
        if ord(i) == 121:
            str_bis += 'Y'
            continue
        if ord(i) == 122:
            str_bis += 'Z'
            continue
        str_bis += i
    print('{}'.format(str_bis))
