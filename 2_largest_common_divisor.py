# ------------------------ Пишем функцию поиска наибольшего общего делителя ------------------------

# 1) интуитивное решение
def gcd1(a, b):
	assert a >= 0 and b >= 0
	for d in reversed(range(max(a, b) + 1)):
		if d == 0 or a % d == b % d == 0:
			return d

# print(gdc1(0, 0))


# 2) алгоритм Евклида
# наибольший общий делитель можно найти между меньшим числом и остатком от деления большего числа на меньшее
def gcd2(a, b):
	while a and b:
		if a >= b:
			a %= b
		else:
			b %= a
	return max(a, b)

# print(gdc2(10, 8))


# 3) алгоритм Евклида - рекурсивный вариант
def gcd3(a, b):
	assert a >= 0 and b >= 0
	if a == 0 or b == 0:
		return max(a, b)
	elif a >= b:
		return gcd3(a % b, b)
	else:
		return gcd3(a, b % a)

# print(gdc3(10, 8))


# 4) можно упростить рекурсию (тк после (a % b, b) всегда идёт (a, b % a))
def gcd4(a, b):
	assert a >= 0 and b >= 0
	if a == 0 or b == 0:
		return max(a, b)
	else:
		return gcd4(b % a, a)

# print(gcd4(10, 8))
