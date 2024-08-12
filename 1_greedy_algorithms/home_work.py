import time
from random import randint
import matplotlib.pyplot as plt
from collections import Counter


# -------------------------------------------------- Жадные алгоритмы ----------------------------------------

# Во время каждой итерации алгоритм выполняет оптимальное действие. Для этого итерируемый объект сначала сортируют


# 1)
# Найти такие точки, которые лежат на всех заданных отрезках. Найденное количество точек должно быть минимальным
def segments_points(data):
	segments = [[int(s[0]), int(s[1])] for s in [x.split(' ') for x in data]]
	segments_sort = sorted(segments, key=lambda x: x[1])
	points = (segments_sort[0][-1],)
	for elem in segments_sort:
		if points[-1] < elem[0]:
			points += elem[0],
	return len(points), *sorted(points)


# print(segments_points(['1 3', '2 5', '3 6']))

# Примеры входных данных
# ['1 10', '2 9', '3 8', '4 7', '5 6'] - 6
# ['1 2', '2 3', '3 4', '4 5', '5 6'] - 2 4 6
# ['1 3', '2 5', '3 6'] - 3
# ['4 4', '5 9', '0 10', '2 8', '4 4', '12 14', '0 8', '3 14', '5 13', '4 6']
# ['4 7', '1 3', '2 5', '5 6']
# ['1 2', '3 4', '5 6', '7 8', '9 10']
# ['1 10', '2 11', '3 8']



# 2)
# Чтобы положить в рюкзак 7 кг продуктов и получить максимальную стоимость рюкзака, нужно отсортировать все продукты
# при помощи удельной цены (те цена 1 кг, тк у нас указан вес товара) и начинать перебирать с самого дорогого.

n, weight_max = 3, 7				# Кол-во видов продуктов и максимальный вес рюкзака
data = ['20 4', '18 3', '14 2']		# 3 вида продуктов. Сумма и общий вес каждого


def max_cost_bag(items, w):
	products = [[int(x) for x in one.split(' ')] for one in items]				# Все продукты
	my_key = lambda x: (x[0] / x[1], x[1])										# сорт по цене за 1 кг и потом по весу
	products_sort = sorted(products, key=my_key, reverse=True)					# Сортируем. По убыванию

	cost_bag = 0
	for cost, weight in products_sort:
		if weight <= w:
			cost_bag += cost
			w -= weight
		else:
			cost_bag += cost * w / weight
			break

	return f'{cost_bag:.3f}'


# print(max_cost_bag(data, weight_max))


# 3)
# Требуется вывести максимальное количество слагаемых и сами эти слагаемые, из которых получается число 'num'
num = 10

def maximum_of_terms(n):
	result, k = [], 0
	for elem in range(1, n + 1):
		if k + elem + elem + 1 > n:
			result.append(n - k)
			return f'{len(result)}\n{" ".join(str(x) for x in result)}'
		result, k = result + [elem], k + elem


# print(maximum_of_terms(num))


def maximum_of_terms_2(n):
	result = []
	summ = 0
	elem = 1
	while summ + elem * 2 + 1 <= n:
		result += [elem]
		summ += elem
		elem += 1
	result.append(n - summ)
	return f'{len(result)}\n{" ".join(str(x) for x in result)}'


# print(maximum_of_terms_2(num))




# -------------------------------------- Проверка времени работы функций --------------------------------------

# функция для замера времени работы подаваемой ей функции
def timed(func, arg, iter=50):
	acc = float('inf')
	for _ in range(iter):
		t0 = time.perf_counter()
		func(arg)
		t1 = time.perf_counter()
		acc = min(acc, t1 - t0)
	return acc


# подаём две функции и получаем график времени
def compare(funcs, items):
	plt.figure(figsize=(12, 7))
	for func in funcs:
		result = [timed(func, item) for item in items]
		plt.plot(items, result)
	plt.legend(funcs)
	plt.grid(True)
	plt.show()


# compare([maximum_of_terms, maximum_of_terms_2], range(1, 100))


# Проверим как меняется время работы функции max_cost_bag в зависимости от количества подаваемых данных
# для этого нужно добавить w = randint(1, 10 ** 3) в функцию timed
def bags():
	n = range(1, 40)
	result = []
	for ind in n:
		acc = []
		for _ in range(ind):
			acc.append(f'{randint(1, 10 ** 3)} {randint(1, 10 ** 3)}')
		result.append(timed(max_cost_bag, acc))
	plt.figure(figsize=(12, 6.5))
	plt.plot(n, result)
	plt.grid(True)
	plt.ylabel('время в секундах')
	plt.xlabel('количество items поданных в функцию max_cost_bag')
	plt.show()


# bags()



# 4)
# Кодировка Хаффмана
def huffman_decrypt(coder, s, crypt):
	result, num = '', ''
	for elem in crypt:
		num += elem
		for key, value in coder.items():
			if num == value:
				result, num = result + key, ''
	print(result == s)


def huffman_crypt(coder, s):
	result = ''.join(coder[elem] for elem in s) or '0'
	print(result)												# выводим закодированную строку
	return huffman_decrypt(coder, s, result)					# отправим код на расшифровку для проверки


def huffman_encode(s):
	h = [(elem, freq) for elem, freq in Counter(s).items()]
	coder = {letter: '' for letter in Counter(s)}				# список с ключами-буквами и пустыми значениями
	if len(h) == 1:
		coder = {h[0][0]: '0'}
	while len(h) > 1:
		h_new = sorted(h, key=lambda x: (x[1], x[0]))			# сортируем полученный список
		left, right = h_new[:2]									# вытаскиваем первые два элемента
		for item in left[0]:
			coder[item] = '0' + coder[item]						# к элементу с меньшей частотой добавляем 0
		for item in right[0]:
			coder[item] = '1' + coder[item]						# к элементу с большей частотой добавляем 1
		h.append((left[0] + right[0], left[1] + right[1]))		# добавляем новый элемент в список
		h.remove(left)											# удаляем из списка первые два элемента
		h.remove(right)
	return huffman_crypt(coder, s)


my_str = 'abcd'
huffman_encode(my_str)
