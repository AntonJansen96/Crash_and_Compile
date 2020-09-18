# 3 - CANNONBALL PYRAMID

# Difficulty: easy

# You make a stack of cannonballs in a close packed
# arrangement in the shape of a 4-sided pyramid,
# how many layers high will your stack be if you lay down
# 917609701 cannonballs?

i = 0
balls = 0

while True:
	balls += (i+1)**2
	if balls == 917609701:
		print(i+1)
		break
	i += 1
