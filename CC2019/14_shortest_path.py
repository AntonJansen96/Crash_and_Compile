# 14 - SHORTEST PATH

# Difficulty: medium

# You are given 10 2-d points, starting at the first one, what
# is the shortest path that visits all these points. Answer the
# question as the indexes of the points [starting at 0], e.g. 0123456789.
# These are the points: [0.68, 0.55], [0.27, 0.15], [0.11, 0.67], [0.32, 0.79],
# [0.87, 0.09], [1.00, 0.70], [0.45, 0.61], [0.95, 0.02], [0.12, 0.23], [0.38, 0.81]

import itertools

points = [[0.27,0.15], [0.11,0.67], [0.32,0.79], [0.87,0.09], [1.00,0.70], [0.45,0.61], [0.95,0.02], [0.12,0.23], [0.38,0.81]]
perms  = list(itertools.permutations(points))

bestlength = 100

for path in perms:

	coord  = [0.68,0.55]
	length = 0

	for i in path:
		
		length += ( ( abs(coord[0] - i[0]) )**2 + ( abs(coord[1] - i[1]) )**2 )**0.5

		coord[0] = i[0]
		coord[1] = i[1]

	if length < bestlength:
		bestlength = length
		bestpath   = path

def order(original,new):
	z = []
	for i in new:
		for j in xrange(0,len(original)):
			if i == original[j]:
				z.append(j)
				break
	return z

def formatorder(z):
	string = '0'
	for i in z:
		string = string + str(i+1)
	return string

# print(bestlength)
# print(bestpath)
print(formatorder(order(points,bestpath)))
