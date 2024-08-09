import time
import matplotlib.pyplot as plt


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
# при помощи удельного веса (цена 1 кг) и начинать перебирать с самого дорогого.

n, weight_max = 3, 7				# Кол-во видов продуктов и максимальный вес рюкзака
data = ['20 4', '18 3', '14 2']		# 3 вида продуктов. Сумма и общий вес каждого


def max_cost_bag(items, w):
	goods = [[int(s[0]), int(s[1])] for s in [one.split(' ') for one in items]]		# Все продукты
	key = lambda x: x[0] / x[1]														# Цена 1 кг
	goods_sort = sorted(goods, key=key, reverse=True)								# Сортируем. По убыванию
	bag = 0
	for thing in goods_sort:
		if thing[1] <= w:
			bag += thing[0]
			w -= thing[1]
		else:
			bag += thing[0] * w / thing[1]
			break
	return f'{bag:.3f}'


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
def timed(func, arg):
	acc = float('inf')
	t0 = time.perf_counter()
	func(arg)
	t1 = time.perf_counter()
	acc = t1 - t0
	return acc


#
def compare(funcs, items):
	plt.figure(figsize=(12, 7))
	for func in funcs:
		result = [timed(func, item) for item in items]
		plt.plot(items, result)
	plt.legend(funcs)
	plt.grid(True)
	plt.show()


# compare([maximum_of_terms, maximum_of_terms_2], range(1, 100))

