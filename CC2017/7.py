def gcd(a,b):
	while b != 0:
		a, b = b, a % b
	return a

count = 0
for i in xrange(1, 10**6):
	if  gcd(i, 10**6) != 1:
            count += (i % 10**6)

print(count)
