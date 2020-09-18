# 7 - INTEGERS IN A ROW

# Difficulty: easy

# If you write down all integers from 1 to 10 in
# a row you can obtain a new number 12345678910.
# Construct a similar number for integers 1 to 10000.
# What is the sum of the product of each digit in this
# number times its position/index (starting at 1)?
# Example for 123 it is 1*1 + 2*2 + 3*3 = 14

z = ''
for i in xrange(1,10000+1):
	z = z+str(i)

total = 0
for i in xrange(0,len(z)):
	total += (i+1) * int(z[i])

print(total)
