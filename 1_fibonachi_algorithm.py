
# 1)
# стандартная функция поиска чисел Фибоначчи работает крайне долго с n > 30
def fib1(n):
	assert n >= 0
	return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


# 2)
# поэтому будем сохранять в словарь уже вычисленные значения, чтобы программа больше их не считала
cache = {}
def fib2(n):
	assert n >= 0
	if n not in cache:
		cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
	return cache[n]


# print(fib1(32))
# print(fib2(50))


# 3)
# второй вариант имеет минус - в словарь cache может зайти кто угодно и сделать с ним что угодно. поэтому создадим
# декоратор для функции. в декораторе будет происходить всё так как нам требуется
def deko(f):
	my_cache = {}
	def inner(n):
		if n not in my_cache:
			my_cache[n] = f(n)
		return my_cache[n]
	return inner

# функцию fib1, которая ни чего не знает про кэширование, теперь можно обернуть в декоратор и использовать
# fib1 = deko(fib1)
# print(fib1(58))


# 4)
# если вызвать функцию fib2 с аргументом 8000, то программа выдаст ошибку, тк рекурсия имеет ограничение. Поэтому
# напишем функцию через итерацию
def fib3(n):
	assert n >= 0
	num1, num2 = 0, 1
	for _ in range(n - 1):
		num1, num2 = num2, num1 + num2
	return num2


# print(fib3(5))


# Для трёх функций построим график зависимости времени от величины "n"
import time
import matplotlib.pyplot as plt

def timed(f, arg, n_iter=50):
	acc = float('inf')
	for _ in range(n_iter):
		t0 = time.perf_counter()
		f(arg)
		t1 = time.perf_counter()
		acc = min(acc, t1 - t0)
	return acc


def compare(fs, args):
	plt.figure(figsize=(12, 7))
	for f in fs:
		plt.plot(args, [timed(f, arg) for arg in args])
		plt.legend(fs)
	plt.grid(True)
	plt.show()


compare([fib1, fib2, fib3], range(1, 11))
