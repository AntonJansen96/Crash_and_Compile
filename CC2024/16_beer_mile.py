#!/usr/bin/env python3

from euler import fibonacci

factor = 1.609344

gen = fibonacci()
fibs = [next(gen) for _ in range(100)]

for idx in range(1, len(fibs) - 1):

    a = fibs[idx]
    b = fibs[idx + 1]

    if abs(b - factor * a) > 0.5 * factor:
        print(a, b, a * factor, abs(b - factor * a))
        break
