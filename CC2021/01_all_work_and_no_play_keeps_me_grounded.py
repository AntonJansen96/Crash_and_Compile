#!/bin/python3

# Playing monopoly for hours and hours and hours and hours and hours on end is 
# bound to drive anybody crazy. The endless cycle of waiting, paying rent, 
# waiting, going to jail, waiting, paying income tax, waiting and winning beauty
# pageants (and waiting) are guaranteed to leave a mark. Being overcome by the
# madness of it all, you decide to start counting. You count the leaves on your
# sad little avocado plant, you count the empty beer bottles in each corner of
# your room, the crust-filled pizza boxes in you hallway, you basicly start to
# count anything. After a while you look down at a piece of paper, where you see
# the following sequence: 1, 1, 4, 8, 2, 8, 4, 12, 3, 1, 12, ... . Obviously, this
# sequence is defined as follows: The sequence starts simply with 2 pre-defined
# terms: A(0) = 1, and A(1) = 1. The following terms are determined in the
# following manner: If A(n - 1) and n are coprime, the n-th term is given by
# A(n - 1) + n + 1. If they are not coprime A(n) is given by: A(n - 1)/gcd(A(n - 1),
# n), where gcd(x, y) is the greatest common divisor between x and y. To you, this
# makes a lot of sense, yet you cannot help but notice that there are multiple
# ones (1's) in the sequence, what is the first time the total number of ones in
# this sequence is equal to 19841012 and you are finally allowed to fly away into 
# the wild blue yonder?

# Euclidian algorithm.
def gcd(x, y):          
    if (x == 0 or y == 0):
        return x + y

    while (y):
        x, y = y, x % y
        
    return x

n_1  = 1
n    = 2
ones = 2

while (True):
    # Do not do this twice but instead store.
    val = gcd(n_1, n)   
    
    if (val == 1):
        n_1 = n_1 + n + 1
    else:
        n_1 = int(n_1 / val)

    if (n_1 == 1):
        ones += 1

    if (ones == 19841012):
        print(n)
        break

    n += 1

# 79364654
# ~20s
