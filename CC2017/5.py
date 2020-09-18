def mersprim(n):
	x = [1,2,3,5,7,13,17,19,31,61,89,107,127,521,607,1279,2203,2281,3217,
	4253,4423,9689,9941,11213,19937,21701,23209,44497,86243,110503,132049,
	216091,756839,859433
	]
	return 2**x[n-1] - 1

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def isPrime(n):
    from math import sqrt; from itertools import count, islice
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

for i in range(1,16):
	a = mersprim(i)
	b = "{0:b}".format(a)
	c = bin(a).count("1")
	d = isPrime(c)

	print("Mersene prime:    %s" % (a))
	print("Binary form:      %s" % (b))
	print("Sum of binary:    %s" % (c))
	print("Sum is prime?:    %s" % (d))
	print("")

#Solution is the 9th mersenne prime for which the sum of digits in base 2 is prime.