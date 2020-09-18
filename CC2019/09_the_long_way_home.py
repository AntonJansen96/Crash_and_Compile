# 9 - THE LONG WAY HOME

# Difficulty: easy

# After a game of monopony, you want to walk home but you're so drunk you're
# for all intents and purposes doing a random walk. You are only capably of
# walking up, down, left and right. Being quite tired you will only be able to
# do 100 steps before you fall asleep. Lets define the distance from your
# starting point by using the Manhattan metric, that is the shortest path you
# can take from your current position to the starting point by only doing the steps:
# 'left', 'right', 'up', and 'down'. (For example if your current position is [2, -3],
# then your Manhattan distance from your origin is 5.) What is the chance that
# during a random walk of 100 steps you end up within a distance of 10, using the
# Manhattan metric, from your initial position? (answer up to 2 decimal places)

# There exist 4^100 = 1.6e60 possibile combinations, so permutations are ruled out.
# We used random.

import random

total = 10**5
count = 0

for i in xrange(0,total):

	coord1 = 0
	coord2 = 0

	for i in xrange(1,101):
		
		x = random.randint(1,4)
		
		if x == 1: 
			coord1 += 1
		elif x == 2:
			coord1 -= 1
		elif x == 3:
			coord2 += 1
		elif x == 4:
			coord2 -= 1

	if abs(coord1) + abs(coord2) < 11:
		count += 1

print('%.2f' % (count/float(total)))
