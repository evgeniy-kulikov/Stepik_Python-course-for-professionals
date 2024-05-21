#  10.2 Итераторы. Часть 2


"""   *   *   *   Task   *   *   *   """


#  10.2-1
"""
Реализуйте функцию filterfalse() с использованием функции filter(), которая принимает два аргумента:
predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
iterable — итерируемый объект
Функция должна работать противоположно функции filter(), 
то есть возвращать итератор, элементами которого являются элементы итерируемого объекта iterable, 
для которых функция predicate вернула значение False.
"""
def filterfalse(predicate, iterable):
    if predicate is None:
        return filter(lambda x: not bool(x), iterable)
    return filter(lambda x: not predicate(x), iterable)

# Вариант
def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    return filter(lambda x: not predicate(x), iterable)


objects = [0, 1, True, False, 17, []]
print(*filterfalse(None, objects))  # 0 False []

numbers = (1, 2, 3, 4, 5)
print(*filterfalse(lambda x: x % 2 == 0, numbers))  # 1 3 5


#  10.2-2
"""
Реализуйте функцию transpose() с использованием функции zip(), которая принимает один аргумент:
matrix — матрица произвольной размерности
Функция должна возвращать транспонированную матрицу matrix.
Под матрицей подразумеваются исключительно вложенные списки.
"""
def transpose(matrix):
    return list(map(list, zip(*matrix)))

# Нестандартное решение
transpose = lambda matrix: list(map(list, zip(*matrix)))

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in transpose(matrix):
    print(row)
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]


matrix = [['1', '2'],
          ['4', '5'],
          ['7', '8'],
          ['3', 4],
          [True, None],
          [9, 80],
          [1, -1]]

print(transpose(matrix))
# [['1', '4', '7', '3', True, 9, 1], ['2', '5', '8', 4, None, 80, -1]]


#  10.2-3
"""
Реализуйте функцию get_min_max(), которая принимает один аргумент:

data — список произвольных объектов, сравнимых между собой
Функция должна возвращать кортеж, в котором 
первым элементом является индекс минимального элемента в списке data, 
вторым — индекс максимального элемента в списке data. 
Если список data пуст, функция должна вернуть значение None.

Если минимальных / максимальных элементов несколько, 
следует вернуть индексы первого по порядку элемента.
"""
def get_min_max(data):
    if data:
        return (data.index(min(data)), data.index(max(data)))


data = [2, 3, 8, 1, 7]
print(get_min_max(data))  # (3, 2)

data = [9]
print(get_min_max(data))  # (0, 0)


#  10.2-4
"""
Реализуйте функцию starmap() с использованием функции map(), которая принимает два аргумента:
func — функция
iterable — итерируемый объект, элементами которого являются коллекции
Функция starmap() должна работать аналогично функции map(), то есть возвращать итератор, 
элементами которого являются элементы итерируемого объекта iterable, 
к которым была применена функция func, 
с единственным отличием: func должна принимать не один аргумент — коллекцию (элемент iterable)
"""
def starmap(func, iterable):
    return map(lambda x: func(*x), iterable)


pairs = [(1, 3), (2, 5), (6, 4)]
print(*starmap(lambda a, b: a + b, pairs))  # 4 7 10


points = [[10], [-9], [2]]
print(*starmap(lambda x: x ** 2, points))  # 100 81 4


#  10.2-5
"""
Реализуйте функцию get_min_max(), которая принимает один аргумент:
iterable — итерируемый объект, элементы которого сравнимы между собой
Функция должна возвращать кортеж, 
в котором первым элементом является минимальный элемент итерируемого объекта iterable, 
вторым — максимальный элемент итерируемого объекта iterable. 
Если итерируемый объект iterable пуст, функция должна вернуть значение None.
"""
def get_min_max(iterable):
    res = iter(iterable)
    try:
        n_min = n_max = next(res)
    except StopIteration:
        return None

    for el in res:
        if el < n_min:
            n_min = el
        elif el > n_max:
            n_max = el
    return n_min, n_max


iterable = iter(range(10))
print(get_min_max(iterable))  # (0, 9)

iterable = [6, 4, 2, 33, 19, 1]
print(get_min_max(iterable))  # (1, 33)

data = iter(['a', 'b', 'c', 'aaa', 'abc', 'cbc', 'bbb'])
print(get_min_max(data))  # ('a', 'cbc')

iterable = iter([])
print(get_min_max(iterable))  # None

iterable = [69]
print(get_min_max(iterable))  # (69, 69)

# data = iter(range(100_000_000))
# print(get_min_max(data))  # (0, 99999999)
