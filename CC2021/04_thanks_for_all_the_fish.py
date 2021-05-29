#!/bin/python3

# The past few years we've excelled at making excellent coding and drinking
# competitions. We hope that you've had a most excellent time playing the crash
# and compile(s). While this is likely our last and most excellent competition we
# hope you a most excellent future full of crashing and compiling. On that note:
# an excellent number is a hexadecimal number that can be interpreted as a decimal
# number in scientific notation. An example is the hexadecimal number 1E0 (base 16),
# which is 480 (base 10), but when read as if it were in scientific notation, it can
# be interpreted as 1*10^0, which is 1. Another example is 4240 (base 16), which can
# be read as 4240 in base 10, while it is actually 16960 in base 10. What is the
# sum of excellent numbers under a million? (1E6, 1000000_10, F4240_16).

import string

alphabet = string.ascii_lowercase
alphabet = alphabet.replace('e', '')

def isexcellent(Input):
    for letter in Input:
        if letter in alphabet:
            return False

    if (Input.count('e') == 0):
        return True
    
    elif (Input.count('e') == 1 and Input[0] != 'e' and Input[-1] != 'e'):
        return True

    return False

total = 0
lim   = 10**6
for decimal in range(1, lim):
    
    hexadecimal = hex(decimal)[2:]
    
    if (isexcellent(hexadecimal)):
        # print(decimal, hexadecimal)
        total += decimal

print(total)

# 41250444165
# instant
