# 10.9 Модуль itertools
""""""


"""   *   *   *   Task   *   *   *   """


#  10.9-1
"""
Реализуйте функцию drop_while_negative(), которая принимает один аргумент:
iterable — итерируемый объект, элементами которого являются целые числа
Функция должна возвращать итератор, генерирующий все числа итерируемого объекта iterable, 
начиная с первого неотрицательного числа.
"""
from itertools import dropwhile

def drop_while_negative(iterable):
    for el in dropwhile(lambda x: x < 0, iterable):
        yield el


numbers = [-3, -2, -1, 0, 1, 2, 3]
print(*drop_while_negative(numbers))
# 0 1 2 3


#  10.9-2
"""
Реализуйте функцию drop_this(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект
obj — произвольный объект
Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого объекта iterable, 
начиная с элемента, не равного obj.
"""
from itertools import dropwhile

def drop_this(iterable, obj):
    for el in dropwhile(lambda x: x == obj, iterable):
        yield el


numbers = [0, 0, 0, 1, 2, 3]
print(*drop_this(numbers, 0))
# 1 2 3

iterator = iter('bbbbeebee')
print(*drop_this(iterator, 'b'))
# e e b e e


#  10.9-3
"""
Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект
predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()
Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, 
для которого функция predicate вернула значение True. Если такого элемента нет, 
функция first_true() должна вернуть значение None
"""
# Ожидаемое решение по теме
from itertools import filterfalse

def first_true(iterable, predicate):
    res = filter(predicate, iterable)
    return next(res, None)

# Вариант
def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    res = filterfalse(lambda x: not predicate(x), iterable)
    return next(res, None)


numbers = [2, 1, 1, 1, 1, 2, 4, 5, 6]
print(first_true(numbers, lambda num: num % 2 == 0))
# 2

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
print(first_true(numbers, lambda num: num > 10))
# 100

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
print(first_true(numbers, None))
# 69

numbers = iter([])
print(first_true(numbers, lambda num: num == 200))
# None


#  10.9-4
"""
Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект
n — натуральное число
Функция должна возвращать итератор, 
генерирующий последовательность из первых n элементов итерируемого объекта iterable.
"""
from itertools import islice

def take(iterable, n):
    yield from islice(iterable, n)


print(*take(range(10), 5))
# 0 1 2 3 4

iterator = iter('beegeek')
print(*take(iterator, 22))
# b e e g e e k

iterator = iter('beegeek')
print(*take(iterator, 1))
# b


#  10.9-5
"""
Реализуйте функцию take_nth(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект
n — натуральное число
Функция должна возвращать n-ый по счету элемент итерируемого объекта iterable. 
Если итерируемый объект iterable содержит менее n элементов, функция должна вернуть значение None
"""
from itertools import islice

def take_nth(iterable, n):
    return next(islice(iterable, n - 1, n), None)


numbers = [11, 22, 33, 44, 55]
print(take_nth(numbers, 3))
# 33

iterator = iter('beegeek')
print(take_nth(iterator, 4))
#g

iterator = iter('beegeek')
print(take_nth(iterator, 10))
# None


#  10.9-6
"""
Реализуйте функцию first_largest(), которая принимает два аргумента в следующем порядке:
iterable — итерируемый объект, элементами которого являются целые числа
number — произвольное число
Функция должна возвращать индекс первого элемента итерируемого объекта iterable, который больше number. 
Если таких элементов нет, функция должна вернуть число −1
"""
from itertools import compress, count

# Ожидаемое решение по теме
def first_largest(iterable, number):
    res = list(compress(count(), (el > number for el in iterable)))
    if res:
        return res[0]
    return -1


# Короче
def first_largest(iterable, number):
    res = next(compress(count(), (el > number for el in iterable)), -1)


# Вариант
def first_largest(iterable, number):
    for idx, el in enumerate(iterable):
        if el > number:
            return idx
    return -1


numbers = [10, 2, 14, 7, 7, 18, 20]
print(first_largest(numbers, 11))
# 2

iterator = iter([-1, -2, -3, -4, -5])
print(first_largest(iterator, 10))
# -1

iterator = iter([18, 21, 14, 72, 73, 18, 20])
print(first_largest(iterator, 10))
# 0
