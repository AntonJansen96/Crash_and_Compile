# 2 - EXPONENT MODULATION

# Difficulty: easy

# How many numbers N between 0 and 123456789
# are there for which mod(N ^ 12345, 17) == 3?

# Brute force:

count = 0
for i in range(1, 123456789):
	if (i ^ 12345) % 17 == 3:
		count += 1

print(count)
