#Find the sum of the divisors of 99999999989

#Volgens Wolfram:

#Divisors:	1, 16823, 5944243, 99999999989
#Solution:  16823 + 5944243 = 5961066

#######################################

# FIND PRIME FACTORS

def factorinteger(n):
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

facs = factorinteger(99999999989)

print(facs)

# OBSERVE THERE EXIST TWO PRIME FACTORS, AND MORE IMPORTANTLY, NO MULTIPLES.
# THEN, THESE ARE THE ONLY DIVISORS THEREFORE THE ANSWER IS SIMPLY:

print(sum(facs))
