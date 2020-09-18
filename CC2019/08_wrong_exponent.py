# 8 - WRONG EXPONENT

# Difficulty: easy

# When learning a new programming language you might
# make mistakes you don't expect. For example one might
# confuse the operators exponent and xor. In
# this case 8 to the power of 2 will not end up
# being 64 (taking the exponent), but rather 10
# (doing bitwise xor). There are occasions when one
# might get lucky and both operations will give the
# same answer. If for example you store your numbers
# as 8-bit integers, then 4 to the
# fourth power = 256 = 0, and 4 xor 4 will also yield 0.
# For this exercise assume overflows are handled
# by restarting at 0, what is the amount of
# combinations one can get the right answer
# with the wrong operator for bases
# ranging from 0 to 256 and powers from 0 to 256?

total = 0
for i in xrange(0,256):
	for j in xrange(0,256):
		if i**j % 256 == i^j:
			total += 1

print(total)
