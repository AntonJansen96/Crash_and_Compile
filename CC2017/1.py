def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

z = 0
for i in range(1,10001):
	z = z + sum_digits(i)

print(z)