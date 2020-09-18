# 16 - PTIJE SANS SMART

# Difficulty: hard

# "You are playing a game of klaverjas. What is the chance you are gauranteed
# to make a pitje, with just looking at your own cards. You must play cards
# in the smart order and you start the game. E.g. if you have 5 hearts
# including the 3 highest your gauranteed to make all those slagen
# \nRound your answer to 2 decimal number, e.g.: 1.23e-3"

# Runtime ~ 60s

def binom(N,n):

	def factorial(n):
		g = 1
		for i in range(1,n+1):
			g *= i
		return g

	num = factorial(N)
	denom = factorial(n)*factorial(N-n)
	return num/denom

def pitjesanssmart(hand):
	
	# SPEEDUP #########################################

	if 'A1' not in hand and 'B1' not in hand and 'C1' not in hand and 'D1' not in hand:
		return False
	
	# CHECK PITJE SANS DUMB ###########################
	
	count = 0

	for i in ['A1','A2','A3','A4','A5','A6','A7','A8']:
		if i in hand:
			count += 1
		else:
			break

	for i in ['B1','B2','B3','B4','B5','B6','B7','B8']:
		if i in hand:
			count += 1
		else:
			break

	for i in ['C1','C2','C3','C4','C5','C6','C7','C8']:
		if i in hand:
			count += 1
		else:
			break

	for i in ['D1','D2','D3','D4','D5','D6','D7','D8']:
		if i in hand:
			count += 1
		else:
			break

	if count == 8:
		return True

	# CHECK PITJE SANS SMART ##########################

	TOTAL = [0, 0, 0, 0]

	for i in ['A1','A2','A3','A4','A5','A6','A7','A8']:
		if i in hand:
			TOTAL[0] += 1

	for i in ['B1','B2','B3','B4','B5','B6','B7','B8']:
		if i in hand:
			TOTAL[1] += 1

	for i in ['C1','C2','C3','C4','C5','C6','C7','C8']:
		if i in hand:
			TOTAL[2] += 1

	for i in ['D1','D2','D3','D4','D5','D6','D7','D8']:
		if i in hand:
			TOTAL[3] += 1

	F1 = ['A1','B1','C1','D1']
	F2 = ['A2','B2','C2','D2']
	F3 = ['A3','B3','C3','D3']

	for i in range(0,4):

	# CHECK 7-CARD MAIN HAND

		if TOTAL[i] == 7 and F1[i] in hand:			# if main hand is 7 cards including A
	
			for j in range(0,4):
				if j != i and F1[j] in hand:		# check side hand for A
					return True

	# CHECK 6-CARD MAIN HAND

		if TOTAL[i] == 6 and F1[i] in hand and F2[i] in hand:			# if main hand is 6 cards including A-10
			
			for j in range(0,4):
				if j != i and F1[j] in hand and F2[j] in hand:			# check side hand for A-10
					return True
			
			count = 0													# check side hand for A and A
			for j in range(0,4):
				if i != j:
					count += hand.count(F1[j])
			if count > 1:
				return True

	# CHECK 5-CARD MAIN HAND

		if TOTAL[i] == 5 and F1[i] in hand and F2[i] in hand and F3[i] in hand:		# if main hand is 5 cards including A-10-K

			for j in range(0,4):
				if j != i and F1[j] in hand and F2[j] in hand and F3[j] in hand:	# check side hand for A-10-K
					return True
			
			for j in range(0,4):													# check side hand for A-10 and A
				if j != i and F1[j] in hand and F2[j] in hand:
					for k in range(0,4):
						if k != i and k != j and F1[k] in hand:
								return True

			count = 0																# check side hand for A and A and A
			for j in range(0,4):
				if i != j:
					count += hand.count(F1[j])
			if count > 2:
				return True

	return False

#######################################################

import itertools

cards = ['A1','A2','A3','A4','A5','A6','A7','A8','B1','B2','B3','B4','B5','B6','B7','B8',
'C1','C2','C3','C4','C5','C6','C7','C8','D1','D2','D3','D4','D5','D6','D7','D8']

sans  = 0
total = binom(32, 8)
hands = itertools.combinations(cards, 8)

for i in range(0, total):
	hand = next(hands)

	if pitjesanssmart(hand) is True:
		sans += 1

print('%.2E' % (sans / float(total)))
