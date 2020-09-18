# 11 - JUFFEN_WAITING_FOR_TURN

# Difficulty: medium

# During a barbeque in September you decide to teach
# some freshmen the game of 'Juffen', which quickly
# turns into a true Jufmania. Before long 18 freshmen
# and you play a game, and you notice that during
# some of the longer games there are quite a few
# turns in which you do not have to say anything.
# After consulting the almanac you are interested in
# finding out what the highest amount of turns is that
# somebody is currently waiting on the 190329th turn.
# (i.e. excluding possible higher numbers during earlier
# turns)

def checkjuf(n):
	if n in [1,2,3,4,5,6,8,9]:
		return False
	elif n % 7 == 0 or (str(n)).find('7') != -1 or str(n) == str(n)[::-1]:
		return True
	else:
		return False

waiting = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

p	   = 0
a      = 1

for n in xrange(1,101):

	for i in xrange(0,19):
		if p == i:
			waiting[i] = 0

		if p != i:
			waiting[i] = waiting[i] + 1

	if checkjuf(n) is True:
		p += a
		a *= -1
	else:
		p += a

	if p == 19:
		p = 0
	elif p == -1:
		p = 18

	# print(n,p,waiting)

print(max(waiting)+1)
