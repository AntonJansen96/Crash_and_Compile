#!/bin/python3

# The local government has started an inquiry into the finances of most of the
# landlords in Groningen. These landlords are suspected of fraudulent behaviour.
# Consider the following case: The income of the landords shows exponential growth,
# but for some reason the growth rate is never a power of 10. To test whether their
# income declarations are fraudulent, we take a look at the distribution of the
# first digits of their incomes. This raises the following question, what is the
# fraction of 7's in the distribution of the first digits? TL:DR: In a series of
# numbers that show exponential growth, what is the fraction of numbers that start
# with a 7? Note that the exponential growth rate should never be a power of 10,
# or very close to a power of 10.

number = 2.0
growthfactor = 1.05

total = 10000
found = 0

for i in range(0, total):
    number *= growthfactor

    if (int(str(number)[0]) == 7):
        found += 1

print(found / float(total))

# 0.58
# instant
