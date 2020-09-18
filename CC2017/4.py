def checkjuf(n):
	if n in [1,2,3,4,5,6,8,9]:
		return False
	elif n % 7 == 0 or (str(n)).find('7') != -1 or str(n) == str(n)[::-1]:
		return True
	else:
		return False

person = 0
n      = 1
a      = 1

while True:
	
	if checkjuf(n) is True:
		person = person + a
		a = -1 * a
	else:
		person = person + a

	if person == 33:
		print(n)
		break

	n = n + 1
