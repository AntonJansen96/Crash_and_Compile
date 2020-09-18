# 13 - FIBONACCI RATIOS

# Difficulty: medium

# In the well-known Fibonacci-sequence the ratio between F(n + 1) and F(n)
# converges to phi (= 1.61803....), which is also known as the golden ratio.
# The Fibonacci-sequence can be generalized by F(n) = F(n-2) + m*F(n-1),
# with F(1) = 0 and F(2) = 1, where m is an integer. If m = 1 you obtain
# the Fibonacci-sequence, and for m = 2 you obtain F(n) = F(n - 2) + 2F(n-1),
# which also has a similar ratio known as the silver ratio. What is the
# sum of the ratios for m starting at 1 and ending with 1000?
# (answer accurate to 4 decimal places)

def F(n,m):
	a = 0; b = 1
	for i in xrange(1,n):
		b, a = a+m*b, b
	return b

n = 100

total = 0
for m in xrange(1,1000+1):
	ratio = F(n+1,m)/float(F(n,m))

	total += ratio

print('%.4f' % (total))
