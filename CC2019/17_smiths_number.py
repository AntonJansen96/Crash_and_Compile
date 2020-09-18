# 17 - SMITHS_NUMBER

# Difficulty: medium

# You've come across a 'joenbuis' video by 'getalnvrind'
# on the subject of Smit's numbers, which are numbers
# that have a special property. The sum of the digits of a
# Smit's number is equal to the sum of the digits of numbers
# composing its prime factorization. Maybe an example explains
# this more clearly:
# 666 = 2 x 3 x 3 x 37, while 6 + 6 + 6 = 18 = 2 + 3 + 3 + (3 + 7).
# What is the sum of all Smit's numbers between 3630000 and 3639999 (inclusive)?

def isprime(n):
	for i in xrange(3,int(n**0.5)+1,2):
		if n % i == 0:
			return False
	return True

def primefactors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

def sum_digits(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s

count = 0

for i in xrange(3630000,3639999+1):

	if isprime(i) is False:

		facs = ''
		for j in primefactors(i):
			facs += str(j)

		if sum_digits(i) == sum_digits(int(facs)):
			count += i

print(count)
