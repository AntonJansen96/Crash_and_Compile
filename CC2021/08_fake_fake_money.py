#!/bin/python3

# While printing fake monopoly money, you've accidentally printed bills ranging
# from 1$ to 1000$. What is the sum of all the numbers counting from 1 to (and
# including) 1000 containing at least one hole (0, 4, 6, 8, 9)?

total = 0
for bill in range(1, 1001):
    billstring = str(bill)
    if '0' in billstring or '4' in billstring or '6' in billstring or '8' in billstring or '9' in billstring:
        total += bill
print(total)
