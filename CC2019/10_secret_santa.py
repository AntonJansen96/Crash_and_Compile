# 10 - SECRET SANTA(RKLAAS)

# Difficulty: medium

# You and 19 other monopolists decide to give each
# other presents. Using the well known formula
# of secret Santa, you each write down your name
# on a straw and put them into a hat. One at a
# time you pick a straw from the hat, untill
# everybody has a straw with a name, that is not
# his or her own name. If somebody draws their own
# name, the entire process starts over (all straws
# 	are returned to the hat). What is the expected
# amount of times the process of drawing from the
# hat is done? That is what is the amount of times
# the process of drawing straws is done on average?
# (a redraw meaning the process starts over)
# (answer accurate up till 4 decimal places)

# EXPLANATION
# factorial(n) is the total amount of permutations.
# subfactorial(n) is the amount of derangements (a permutation such that 
# no element in a set appears in its original position, i.e. nobody draws themselves).

import numpy as np

def factorial(n):
	g = 1
	for i in xrange(1,n+1):
		g *= i
	return g

def subfactorial(n):
	return round(factorial(n)/np.exp(1))

p_win  = subfactorial(20)/factorial(20)
p_fail = 1 - p_win

print('%.4f' % (p_fail/p_win))
