# 19 - RECAMAN

# Difficulty: easy

# During one of your daily scoutings of the obscure depths of youtube,
# you come across a music video called 'spooky numbers'. In this video
# the numbers of the Recaman sequence are mapped to piano keys, resulting
# in a somewhat spooky melody. After studying the sequence a bit, you notice
# that there are repeating numbers, something you hadn't expected beforehand.
# The first repeating number is 42 (first repeat, 2 occurences when only
# considering the first 100 Recaman numbers), but what is the first
# number with the maximum amount of repeats when only considering the first
# 100000 Recaman numbers? The Recaman sequence is defined as follows:
# the first term, a(0) = 0. a(n) = a(n - 1) - n, if positive and not already
# in the sequence, otherwise it is a(n - 1) + n. The first terms are given by:
# 0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, ...... Format the answer as
# follows: number_occurences (i.e 123456_78).

N   = [0] * 10**6
a_1 = 0

for n in xrange(1, 100000):
	x = a_1 - n
	if x > 0 and N[x] < 1:
		N[x] += 1
		a_1 = x
	else:
		y = a_1 + n
		N[y] += 1
		a_1 = y

print('%s_%s' % (N.index(max(N)), max(N)))
