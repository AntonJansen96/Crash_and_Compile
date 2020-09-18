# import random
# import fnmatch

# cards = [
# 'A1','A2','A3','A4','A5','A6','A7','A8',
# 'B1','B2','B3','B4','B5','B6','B7','B8',
# 'C1','C2','C3','C4','C5','C6','C7','C8',
# 'D1','D2','D3','D4','D5','D6','D7','D8'
# ]

# A = 10**6
# g = 0

# x = range(1,33)
# x = [i - 1 for i in x]

# for i in range(1,A):

# 	y = random.sample(x,8)

# 	z = []
# 	for j in y:
# 		z.append(cards[j])

# 	if fnmatch.filter(z,'A?') == ['A1'] or fnmatch.filter(z,'B?') == ['B1'] \
# 	or fnmatch.filter(z,'C?') == ['C1'] or fnmatch.filter(z,'D?') == ['D1']:
# 		g = g +1

# print(g/float(A))

# 0.126735

# NEW METHOD ########################

def binom(N,n):

	def factorial(n):
		g = 1
		for i in xrange(1,n+1):
			g *= i
		return g

	num = factorial(N)
	denom = factorial(n)*factorial(N-n)
	return num/denom

import itertools
import fnmatch

cards = ['A1','A2','A3','A4','A5','A6','A7','A8','B1','B2','B3','B4','B5','B6','B7','B8',
'C1','C2','C3','C4','C5','C6','C7','C8','D1','D2','D3','D4','D5','D6','D7','D8']

count = 0
total = binom(32,8)
hands = itertools.combinations(cards,8)

for i in xrange(0,total):
	hand = next(hands)

	# if 'A1' in hand or 'B1' in hand or 'C1' in hand or 'D1' in hand:
	# 	count += 1

	if fnmatch.filter(hand, 'A?') == ['A1'] or fnmatch.filter(hand, 'B?') == ['B1'] \
	or fnmatch.filter(hand, 'C?') == ['C1'] or fnmatch.filter(hand,' D?') == ['D1']:
		count += 1

print('%.4f' % (count/float(total)))
