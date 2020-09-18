# 15 - RECURSIVE_JUF

# Difficulty: medium

# During a game of 'recursive juffen', you wonder at what number you've started 'juf'
# amount of new games of 'Juf'. What juf-number is the number that corresponds
# to the 7th recursively started game of 'Juffen' (1 original game, 7 recursions)?

def checkjuf(n):
	if n in [1,2,3,4,5,6,8,9]:
		return False
	elif n % 7 == 0 or (str(n)).find('7') != -1 or str(n) == str(n)[::-1]:
		return True
	else:
		return False

level0 = []; level1 = []; level2 = []; level3 = []
level4 = []; level5 = []; level6 = []; level7 = []

x = 0; y = 0; z = 0; k = 0; l = 0; m = 0; n = 0

i = 0
while True:
	if checkjuf(i) is False:
		level0.append(i)
	else:
		x += 1
		if checkjuf(x) is False:
			level1.append(x)
		else:
			y += 1
			if checkjuf(y) is False:
				level2.append(y)
			else:
				z += 1
				if checkjuf(z) is False:
					level3.append(z)
				else:
					k += 1
					if checkjuf(k) is False:
						level4.append(k)
					else:
						l += 1
						if checkjuf(l) is False:
							level5.append(l)
						else:
							m += 1
							if checkjuf(m) is False:
								level6.append(m)
							else:
								n += 1
								if checkjuf(n) is False:
									level7.append(n)
									print(i)
									break
	i += 1
