# 5 - PAULUS NUMBER

# Difficulty: medium

# A Paulus number is a number for which the second greatest common divisor with 12345678 is 3.
# An example of a Paulus number is 12. What is the sum of all Paulus numbers below 1000?

# Use second-greatest common denominator algorithm:
# first calculate gcd using Euclidian algorithm, then find largest divider of gcd.

def sgcd(a,b):
	while b != 0:
		a, b = b, a % b
	
	n = a-1
	while n != 0:
		if a % n == 0:
			return n
		n -= 1
	return 1

count = 0
for i in xrange(1, 1000):
	if sgcd(i, 12345678) == 3:
		count += i

print(count)
