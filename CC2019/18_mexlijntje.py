# 18 - MEXLIJNTJE

# Difficulty: hard

# What is the probability that you get mex during a mexlijntje? .
# Some clarification: During a mexlijntje, one may throw at most three
# times where each 1 or 2 may be kept at most once. Mex is a 1 and a 2.
# Throwing a 3 and a 1 the player has to rethrow without keeping the 1,
# but without losing a try. This assignment may of course also be solved by hand.

import random

def playmex():
	alist = []
	blist = []

	rounds = 1
	fresh  = 1

	while rounds < 4:
		
		if fresh == 1:
			a = random.randint(1,6)
			b = random.randint(1,6)

		if fresh != 1:
		
			if rounds == 2:
				if alist[0] in [1,2]:
					a = alist[0]
					b = random.randint(1,6)
				elif blist[0] in [1,2]:
					a = random.randint(1,6)
					b = blist[0]
				else:
					a = random.randint(1,6)
					b = random.randint(1,6)

			if rounds == 3:
				if alist[0] in [1,2]:
					a = random.randint(1,6)
					if blist[1] in [1,2]:
						b = blist[1]
					else:
						b = random.randint(1,6)
				elif blist[0] in [1,2]:
					b = random.randint(1,6)
					if alist[1] in [1,2]:
						a = alist[1]
					else:
						a = random.randint(1,6)
				elif alist[1] in [1,2]:
					a = alist[1]
					b = random.randint(1,6)
				elif blist[1] in [1,2]:
					b = blist[1]
					a = random.randint(1,6)
				else:
					a = random.randint(1,6)
					b = random.randint(1,6)

		if a + b == 3:
			return True

		elif sorted([a,b]) == [1,3]:
			fresh = 1

		else:
			alist.append(a)
			blist.append(b)
			rounds += 1
			fresh = 0

	return False

total = 10**5
mex   = 0

for i in xrange(0,total):
	if playmex() is True:
		mex += 1

print('%.3f' % (mex/float(total)))
