def to_base_5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n /= 5
    return int(s)

def shiftright(n):
	string = str(n)
	last   = string[-1:]
	new    = string[:-1]
	return int(last+new)

g = 0
for i in xrange(1,390625):
	x = to_base_5(i)
	y = to_base_5(3*i)
	z = shiftright(x)
	if y == z:
		print("i in base 10: %s" % (i))
		print("i in base  5: %s" % (x))
		print("3*i in base5: %s" % (y))
		print("shifted in 5: %s" % (z))
		print("")
		g = g + i

print("Sum in base-10: %s" % (g))
print("Sum in base-5 : %s" % (to_base_5(g)))