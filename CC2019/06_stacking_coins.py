# 6 - STACKING COINS

# Difficulty: medium

# Take four circles of radius 1 at the corners,
# (0,0), (0,1), (1,0), (1,1). Compute the area of
# intersection between the four circles with an
# error smaller than 0.001.

dt    = 0.0005
count = 0

for i in xrange(0, int(1/dt)+1):
	for j in xrange(0, int(1/dt)+1):

		x = i*dt
		y = j*dt

		if (x**2 + y**2)**0.5 < 1:
			if ((1-x)**2 + y**2)**0.5 < 1:
				if (x**2 + (1-y)**2)**0.5 < 1:
					if ((1-x)**2 + (1-y)**2)**0.5 < 1:
						count += 1
                    
print('%.4f' % (count* dt**2))
