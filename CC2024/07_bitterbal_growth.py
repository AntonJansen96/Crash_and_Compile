#!usr/bin/env python3

array = [1]


def generateNthRow(N):  # Generates the Nth row in Pascal's triangle.
    prev = 1
    for idx in range(1, N + 1):
        curr = (prev * (N - idx + 1)) // idx
        prev = curr
        array.append(curr)


generateNthRow(1984)

factor = 0  # Find the factor.
for idx in range(len(array)):
    factor += array[idx] / (10**idx)
print(factor)
