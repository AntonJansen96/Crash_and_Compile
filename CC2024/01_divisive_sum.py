#!/usr/bin/env python3

from euler import Primes

primes = Primes()

count = 0
for num in range(1, 241012 + 1):
    count += len(primes.factors(num))

print(count)
