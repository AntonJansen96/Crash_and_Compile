# 12 - PITJE SANS

# Difficulty: medium

# You are playing a game of klaverjas. What is the chance you are
# gauranteed to make a pitje sans, with just looking at your own cards,
# when you can play your cards in random order. You start the game.
# Example: you have all cards of 1 color, or A 10 of every color.
# Round your answer to 2 decimal number, e.g.: 1.23e-3

import itertools

def checkpitjesans(hand):
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

	return False

def binom(N,n):

	def factorial(n):
		g = 1
		for i in xrange(1,n+1):
			g *= i
		return g

	num = factorial(N)
	denom = factorial(n)*factorial(N-n)
	return num/denom

cards = ['A1','A2','A3','A4','A5','A6','A7','A8','B1','B2','B3','B4','B5','B6','B7','B8',
'C1','C2','C3','C4','C5','C6','C7','C8','D1','D2','D3','D4','D5','D6','D7','D8']

sans  = 0
total = binom(32,8)
hands = itertools.combinations(cards,8)

for i in xrange(0,total):
	hand = next(hands)

	if checkpitjesans(hand) is True:
		sans += 1

print('%.2E' % (sans/float(total)))
