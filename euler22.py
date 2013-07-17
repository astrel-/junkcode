#Project Euler
#Problem 22
#real	0m0.042s

import re

def char_position(letter):
    return ord(letter) - 96

with open('names') as file:
    s = file.read().lower()
names = re.sub(r'",?"?',' ',s).split()
names.sort()
#print "\n".join(names)

def method1(names):
    result = 0
    for idx, val in enumerate(names):
        a = 0
        for elem in val:
            a += char_position(elem)
        result += a*(idx+1)
    print result

method1(names)