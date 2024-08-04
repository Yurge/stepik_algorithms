
# стандартная функция поиска чисел Фибоначчи работает крайне долго с n > 30
def fib1(n):
	assert n >= 0
	return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


# поэтому будем сохранять в словарь уже вычисленные значения, чтобы программа больше их не считала
cache = {}
def fib2(n):
	assert n >= 0
	if n not in cache:
		cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
	return cache[n]


print(fib1(32))
print(fib2(80))
