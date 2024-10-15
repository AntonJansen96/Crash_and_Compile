#!/usr/bin/env python3

from random import randint
from numpy import mean


def growthFactor(n, number):
    return abs(number) ** (1 / n)


store = []

for repeat in range(1000):  # repeat "measurement" 1000x for more accurate result.

    chain = [1, 1, 1]  # initial.

    for n in range(1, 2300):

        if randint(0, 1) == 1:
            chain.append(chain[-1] + chain[-2] + chain[-3])
        else:
            chain.append(chain[-1] - chain[-2] - chain[-3])

    factor = growthFactor(n, chain[-1])

    store.append(factor)
    print(f"n = {1 + repeat}, {factor}")

print(f"mean = {mean(store):.3f}")
