#  10.8 Модуль itertools
""""""


"""   *   *   *   Task   *   *   *   """


#  10.8-1
"""
Реализуйте функцию tabulate(), которая принимает один аргумент:
func — произвольная функция
Функция tabulate() должна возвращать итератор, 
генерирующий бесконечную последовательность возвращаемых значений функции func 
сначала с аргументом 1, затем 2, затем 3, и так далее.
"""
from itertools import count

# Вариант преподавателя
def tabulate(func):
    return map(func, count(1))

# Хорошее решение
def tabulate(func):
    for el in count(1):
        yield func(el)

func = lambda x: x
values = tabulate(func)
print(next(values))  # 1
print(next(values))  # 2

func = lambda x: x ** 2
values = tabulate(func)
for _ in range(100):
    print(next(values))
# 1
# 2
# ...
# 1000


def func(n):
    return 'beegeek' * n

values = tabulate(func)
for _ in range(10):
    print(next(values))
# beegeek
# beegeekbeegeek
# beegeekbeegeekbeegeek
# beegeekbeegeekbeegeekbeegeek


#  10.8-2
"""
Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:
n — натуральное число
Функция должна возвращать итератор, генерирующий последовательность из n чисел, 
каждое из которых является факториалом очередного натурального числа.
"""
from itertools import accumulate
import operator
def factorials(n):
    yield from accumulate(range(1, n + 1), operator.mul)
    # yield from accumulate(range(1, n + 1), lambda x, y: x * y)


numbers = factorials(6)
print(*numbers)
# 1 2 6 24 120 720


#  10.8-3
"""
Функция alnum_sequence()
Реализуйте функцию alnum_sequence(), которая не принимает никаких аргументов.
Функция должна возвращать итератор, 
циклично генерирующий бесконечную последовательность натуральных чисел и заглавных латинских букв:
1,A,2,B,3,C,..,X,25,Y,26,Z
"""
from itertools import cycle
from string import ascii_uppercase as letter

def alnum_sequence():
    n = cycle(range(1, 27))
    s = cycle(letter)
    res = (el for item in zip(n, s) for el in item)
    yield from cycle(res)

# Вариант
def alnum_sequence():
    for el in zip(cycle(range(1, 27)), cycle(letter)):
        yield from el

def alnum_sequence():
    n = cycle(range(1, 27))
    s = cycle(letter)
    while True:
        yield next(n)
        yield next(s)

# Что бы такого еще выдумать? 🙃
def alnum_sequence():
    n = cycle(range(1, 27))
    s = cycle(letter)
    for _ in cycle(letter):
        yield from (next(n), next(s))

alnum = alnum_sequence()
print(*(next(alnum) for _ in range(55)))
# 1 A 2 B 3 C 4 D 5 E 6 F 7 G 8 H 9 I 10 J 11 K 12 L 13 M 14 N 15 O
# 16 P 17 Q 18 R 19 S 20 T 21 U 22 V 23 W 24 X 25 Y 26 Z 1 A 2


#  10.8-4
"""
Функция roundrobin() 🌶️
Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных аргументов, 
каждый из которых является итерируемым объектом.
Функция должна возвращать итератор, 
генерирующий последовательность из элементов всех переданных итерируемых объектов: 
сначала первый элемент первого итерируемого объекта, затем первый элемент второго итерируемого объекта, и так далее; 
после второй элемент первого итерируемого объекта, затем второй элемент второго итерируемого объекта, и так далее.
"""
from itertools import zip_longest

# Слабое место - аргумент fillvalue. Его значение не должно быть равным какому-либо значению из *args
def roundrobin(*args):
    yield from (el for data in zip_longest(*args, fillvalue='') for el in data if el != '')

    # for data in zip_longest(*args, fillvalue=''):
    #     for el in data:
    #         if el != '':
    #             yield el


# По очереди опустошаем итераторы, а если все пустые, то останавливаем цикл while
def roundrobin(*args):
    iters = tuple(iter(el) for el in args)
    while True:
        err_counter = 0
        for el in iters:
            try:
                res = next(el)
            except StopIteration:
                err_counter += 1
            else:
                yield res
        if err_counter == len(iters):
            break


print(*roundrobin('abc', 'd', 'ef'))
# a d e b f c

numbers = [1, 2, 3]
letters = iter('beegeek')
print(*roundrobin(numbers, letters))
# 1 b 2 e 3 e g e e k

print(list(roundrobin()))
# []

