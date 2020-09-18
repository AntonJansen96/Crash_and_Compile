# 4 - PYTHAGOREAN QUADRUPLES

# Difficulty: easy

# A pythagorean triple is a combination of positive integers,
# a, b, and c, such that a^2 + b^2 = c^2.
# For example 3^2 + 4^2 = 5^2.
# This problem can be naturally extended by looking at
# Pythagorean quadruples. These are positive integers,
# a,b,c, and d, such that a^2 + b^2 + c^2 = d^2.
# How many quadruples exist for which d is strictly
# smaller than 10000?

# Brute force:

quadruples = 0

for i in xrange(1,101):
	for j in xrange(1,101):
		for k in xrange(1,101):

			dd = i**2 + j**2 + k**2
			d  = dd**0.5

			if int(d) == d and d < 100:
				quadruples += 1

print(quadruples)
