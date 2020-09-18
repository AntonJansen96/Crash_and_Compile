def triang(n):
	return n*(n+1)/2

z     = 0
total = 0

for i in range(1,10**6+1):
	total = total + triang(i)

	if str(total).find('33') != -1:
		z = z + 1

print(z)