#!/usr/bin/env python3

from euler import Primes

primes = Primes()
count = 0


def aliquot(num):

    if not primes.isprime(num):  # Primes do not have any proper divisors.

        propDivSum = sum(primes.factors(num, proper=True))

        if propDivSum > 20241012:
            global count
            count += propDivSum
            return

        aliquot(propDivSum)  # Use recursion to generate the sequence.


for num in range(2, 1210 + 1):
    try:
        aliquot(num)
    except RecursionError:  # Hack to take care of things stuck in loops.
        pass

print(count)
