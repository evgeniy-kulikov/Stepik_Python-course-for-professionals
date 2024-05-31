# 10.10 Модуль itertools
""""""


"""   *   *   *   Task   *   *   *   """


#  10.10-1
"""
Реализуйте функцию sum_of_digits(), которая принимает один аргумент:
iterable — итерируемый объект, элементами которого являются натуральные числа
Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в итерируемом объекте iterable.
"""
from itertools import chain
from collections import Counter


# Хорошее решение
def sum_of_digits(iterable):
    data = chain.from_iterable(map(str, iterable))
    return sum(map(int, data))

# Разложение на элементы
def sum_of_digits(iterable):
    data = chain.from_iterable(map(str, iterable))
    sum = 0
    for el in data:
        sum += int(el)
    return sum


# Нестандартное решение
def sum_of_digits(iterable):
    data = chain.from_iterable(map(str, iterable))
    return sum(k * v for k, v in Counter(map(int, data)).items())


print(sum_of_digits([13, 20, 41, 2, 2, 5]))
# 20

print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
# 46

print(sum_of_digits([123456789]))
# 45


#  10.10-2
"""
Реализуйте функцию is_rising(), которая принимает один аргумент:
iterable — итерируемый объект, элементами которого являются числа
Функция должна возвращать True, если элементы итерируемого объекта расположены строго по возрастанию, 
или False в противном случае.
"""
from itertools import pairwise, starmap
from operator import lt

def is_rising(iterable):
    return all(el[0] < el[1] for el in pairwise(iterable))
    # return all(map(lambda el: el[0] < el[1], pairwise(iterable)))
    # return all(starmap(lambda a, b: a < b, pairwise(iterable)))


# Хорошее решение
def is_rising(iterable):
    return all(starmap(lt, pairwise(iterable)))


print(is_rising([1, 2, 3, 4, 5]))
# True

iterator = iter([1, 1, 1, 2, 3, 4])
print(is_rising(iterator))
# False

iterator = iter(list(range(100, 200)))
print(is_rising(iterator))
# True


#  10.10-3
"""
Реализуйте функцию max_pair(), которая принимает один аргумент:
iterable — итерируемый объект, элементами которого являются числа
Функция должна возвращать единственное число — 
максимальную сумму двух соседних чисел итерируемого объекта iterable
"""
from itertools import pairwise, starmap
from operator import add

def max_pair(iterable):
    return max(starmap(add, pairwise(iterable)))

# Короче
def max_pair(iterable):
    return max(map(sum, pairwise(iterable)))


print(max_pair([1, 8, 2, 4, 3]))
# 10

iterator = iter([1, 2, 3, 4, 5])
print(max_pair(iterator))
# 9

iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
print(max_pair(iterator))
# 0


#  10.10-4
"""
Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект
times — натуральное число
Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, 
зацикленных times раз.
"""
from itertools import chain, tee


def ncycles(iterable, times):
    data = tee(iterable, times)
    yield from chain.from_iterable(data)


# Вариант
def ncycles(iterable, times):
    return (el for itr in tee(iterable, times) for el in itr)


print(*ncycles([1, 2, 3, 4], 3))
# 1 2 3 4 1 2 3 4 1 2 3 4

iterator = iter('bee')
print(*ncycles(iterator, 4))
# b e e b e e b e e b e e

iterator = iter([1])
print(*ncycles(iterator, 10))
# 1 1 1 1 1 1 1 1 1 1


#  10.10-5
"""
Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект
n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность, 
элементами которой являются объединенные в кортежи по n элементов соседние элементы итерируемого объекта iterable. 
Если у элемента не достаточно соседей, то ими становится значение None.
"""
from itertools import repeat, zip_longest

# Сдвиг в итераторах происходит из-за next()
def grouper(iterable, n):
    data = repeat(iter(iterable), n)
    return zip_longest(*data)


# Вариант
def grouper(iterable, n):
    yield from zip_longest(*[iter(iterable)] * n)


numbers = [1, 2, 3, 4, 5, 6]
print(*grouper(numbers, 2))
# (1, 2) (3, 4) (5, 6)

iterator = iter([1, 2, 3, 4, 5, 6, 7])
print(*grouper(iterator, 3))
# (1, 2, 3) (4, 5, 6) (7, None, None)

iterator = iter([1, 2, 3])
print(*grouper(iterator, 5))
# (1, 2, 3, None, None)
