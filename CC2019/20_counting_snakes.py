# 20 - COUNTING SNAKES

# Difficulty: hard

# In the proof that shows there are as many quotients as there are
# numbers one constructs a (infinite) matrix containing all quotients.
# The top row consists of 1/1 1/2 1/3 1/4 .... etc, the second row of
# 2/1 2/2 2/3 2/4 .... etc, all the way to the botom. By counting the
# quotients in a specific way one can show that at a certain point any
# quotient will be counted. This is done by starting at the first
# quotient 1/1, then moving one step to the right 1/2, the second quotient,
# then moving down and to the left (diagonally) to count 2/1, this is
# followed by a step downwards, then right and up (diagonally) untill
# you end up in the first row, then right one step and then left and down again. 
# This way you snake through the matrix, counting all quotients.
# For clarity, take a look at the first bit of the matrix, where the
# number corresponds to when you arrive at that particular spot. 
# 1 2 6 7 15 16 28 29 45 46
# 3 5 8 14 17 27 30 44 47 65
# 4 9 13 18 26 31 43 48 64 69
# 10 12 19 25 32 42 49 63 70 88
# 11 20 24 33 41 50 62 71 87 96
# 21 23 34 40 51 61 72 86 97 115
# 22 35 39 52 60 73 85 98 114 127
# 36 38 53 59 74 84 99 113 128 146
# 37 54 58 75 83 100 112 129 145 162
# 55 57 76 82 101 111 130 144 163 181
# What number do you count when arriving at the quotient 14/2019?

# Runtime ~ 70s on i5 7600k @ 4.6 GHz

# EXPLANATON
# Looked up the pattern in the numerator and denominator on https://oeis.org/.
# Found following generating formula for the sequences for Mathematica:
# Table[Join[Range[2 n - 1], Reverse@Range[2 n - 2]], {n, 4}] // Flatten
# Table[Join[Range[2 n], Reverse@Range[2 n - 1]], {n, 4}] // Flatten
# Worked these functions out in python (gen_nums, gen_denoms)
# Generate large list of nums and denoms (both in the order of path of snake).
# Search for n for which num = 14 and denom = 2019.

def genNums(number):
	A = []
	for idx in range(0, number + 1):
		a = range(1, 2 * idx)
		b = range(1, 2 * idx - 1)[::-1]
		A += (a + b)
	return A

def genDenoms(number):
	A = []
	for idx in range(0, number + 1):
		a = range(1, 2 * idx + 1)
		b = range(1, 2 * idx)[::-1]
		A += (a + b)
	return A

lim = 1200

A = genNums(lim)
B = genDenoms(lim)

num = 1
while True:
	if A[num - 1] == 14 and B[num - 1] == 2019:
		print(num)
		break
	num += 1
