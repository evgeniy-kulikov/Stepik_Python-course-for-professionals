# 3.6 Модуль time
""""""

"""
Работа функций модуля time основывается на системе описания времени. 
Текущее время представляется в виде вещественного значения в секундах, 
прошедших с момента начала эпохи и до сегодняшнего дня. 
Начало эпохи — это полночь 1 января 1970 года (00:00:00 UTC)

Модуль time предоставляет только функции, позволяющие работать со временем:
- отображать информацию о времени, прошедшем с начала эпохи
- преобразовывать значение системного времени к удобному виду
- прерывать выполнение программы (установка паузы) на заданное количество секунд
- измерять время выполнения программы целиком или ее отдельных модулей

!!!
если требуется сравнивать или производить арифметические операции со временем, 
то нужно использовать модуль datetime, а не time
"""

""" *  *  *  *  *  *  *  *  *   """
""" Функция time() """
# Для того чтобы получить количество секунд, прошедших с момента начала эпохи
import time

seconds = time.time()    # получаем количество прошедших секунд в виде float числа
print('Кол-во секунд с начала эпохи =', seconds)
# Кол-во секунд с начала эпохи = 1695022068.879945

nano = time.time_ns()
# Возвращает целочисленное значение, представляющее то же время, прошедшее с эпохи, но в наносекундах


""" *  *  *  *  *  *  *  *  *   """
""" Функция ctime() """
# принимает в качестве аргумента количество секунд, прошедших с начала эпохи, и возвращает строку,
# представляющую собой местное (локальное) время.
import time

seconds = 1695022068.879945
local_time = time.ctime(seconds)
print('Местное время:', local_time)
# Местное время: Mon Sep 18 10:27:48 2023
"""
Примечание. Поскольку местное время связано с нашим языковым стандартом, 
временные метки часто учитывают специфические для локали детали, 
такие как порядок элементов в строке и перевод сокращений дня и месяца. 
Функция ctime() игнорирует эти детали и всегда возвращает строку в следующем порядке:
день недели: Mon
название месяца: Sep
день месяца: 18
часы, минуты, секунды: 10:27:48
год: 2023
"""


# Вызывать функцию ctime() можно и без аргументов,
# в этом случае в качестве аргумента подставляется значение вызова функции time()
import time

local_time = time.ctime()
print('Местное время:', local_time)
# Местное время: Mon Sep 18 10:27:48 2023

# что равнозначно коду:
import time

seconds = time.time()
local_time = time.ctime(seconds)
print('Местное время:', local_time)
# Местное время: Mon Sep 18 10:27:48 2023


""" *  *  *  *  *  *  *  *  *   """
""" Функция sleep() """
#  Используется для добавления задержки в выполнении программы.
#  Эта функция принимает в качестве аргумента количество секунд (secs)
#  и добавляет задержку в выполнении программы на указанное количество секунд.
#  Аргумент secs может быть числом с плавающей точкой (float)
import time

print('Before the sleep statement')
time.sleep(3)
print('After the sleep statement')

#  Иногда может потребоваться задержка на разное количество секунд
import time

for i in [0.3, 1, 3.8, 2]:
    print(f'Waiting for {i} seconds')
    time.sleep(i)
print('The end')
# Waiting for 0.3 seconds
# Waiting for 1 seconds
# Waiting for 3.8 seconds
# Waiting for 2 seconds
# The end


""" *  *  *  *  *  *  *  *  *   """
""" Измерение времени выполнения программы """

import time

start_time = time.time()

for i in range(3):
    print(i)
    time.sleep(1)

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')
# 0
# 1
# 2
# Время работы программы = 3.020331621170044
"""
числовое значение времени, получаемое таким образом, 
может иметь погрешности за счет внутренних особенностей работы компьютера, 
в среде которого выполняется программа.
"""


""" *  *  *  *  *  *  *  *  *   """
""" Функция monotonic() """
"""
Для измерения времени выполнения программы подходит функция monotonic(),
доступная на всех ОС, так как ее результат не зависит от корректировки системных часов.
Используемый таймер в функции monotonic() никогда не вернет при повторном вызове значение, 
которое будет меньше значения, полученного при предыдущем вызове.

Функция monotonic_ns() похожа на monotonic(), но возвращает время в наносекундах. 
Работает не на всех операционных системах.

Принцип работы и применения функции monotonic() такой же, как и у функции time(). 
Однако функция monotonic() дает результат, 
который обладает гарантированной точностью и не зависит от внешних условий.
"""
import time

start_time = time.monotonic()

for i in range(3):
    print(i)
    time.sleep(0.5)

end_time = time.monotonic()

elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')
# 0
# 1
# 2
# Время работы программы = 1.5309999999990396


""" *  *  *  *  *  *  *  *  *   """
""" Функция monotonic() """
# Для самого точного измерения времени выполнения программы следует использовать функцию perf_counter().
# Данная функция использует таймер с наибольшим доступным разрешением,
# что делает эту функцию отличным инструментом для измерения времени выполнения кода на коротких интервалах.
import time

start_time = time.perf_counter()

for i in range(3):
    print(i)
    time.sleep(1)

end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f'Время работы программы = {elapsed_time}')
# 0
# 1
# 2
# Время работы программы = 3.0250506


""""""
"""   *   *   *   Task   *   *   *   """
""""""


#  3.6-01
"""
Реализуйте функцию calculate_it(), которая принимает один или более аргументов в следующем порядке:
func — произвольная функция
*args — переменное количество позиционных аргументов, каждый из которых является произвольным объектом
Функция должна возвращать кортеж, 
первым элементом которого является возвращаемое значение функции func при вызове с аргументами *args, 
а вторым — примерное время (в секундах), затраченное на вычисление этого значения.
Input:  calculate_it(add, 1, 2, 3)
Output: (6, 3.000720262527466)
"""
import time

def calculate_it(func, *args):
    start = time.perf_counter()
    res = func(*args)
    end = time.perf_counter()
    return res, end - start

# def add(a, b, c):
#     time.sleep(3)
#     return a + b + c
#
# s = calculate_it(add, 1, 2, 3)
# print(s)


#  3.6-02
"""
Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
- funcs — список произвольных функций
- arg — произвольный объект
Функция get_the_fastest_func() должна возвращать функцию из списка funcs, 
которая затратила на вычисление значения при вызове с аргументом arg наименьшее количество времени.
"""
import time
def get_the_fastest_func(funcs: list, arg):
    min_time = 1000  # плохое решение
    res = None
    for el in funcs:
        start = time.perf_counter()
        el(arg)
        delta = time.perf_counter() - start
        if min_time > delta:
            min_time = delta
            res = el
    return res
    # return res.__name__

# Вариант лучше
import time
def get_min_time(fun, val):
    start = time.perf_counter()
    fun(val)
    delta = time.perf_counter() - start
    return delta, fun

def get_the_fastest_func(funcs: list, arg):
    res = [get_min_time(el, arg) for el in funcs]
    res = min(res, key=lambda x: x[0])
    return res[1]
    # return res[1].__name__


#  3.6-03
"""
доступны три реализации функции, которая вычисляет факториал числа n:
- встроенная из модуля math
- рекурсивная
- итеративная
Выясните, какая функция быстрее вычислит факториал числа 900.

Output: factorial()
"""
import time
from math import factorial

num = 900
def calculate_it(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start

def factorial_recurrent(n):  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)

def factorial_classic(n):  # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

a = calculate_it(factorial, num)  # Ответ factorial
print(a)  # 3.770000000000162e-05
b = calculate_it(factorial_recurrent, num)
print(b)  # 0.0012429000000000051
c = calculate_it(factorial_classic, num)
print(c)  # 0.0002560000000000062


#  3.6-04
"""
Вам доступны две реализации функции, которая создает и 
возвращает список из чисел от 1 до 10000000 включительно:
- с использованием цикла for и метода append()
- с использованием списочного выражения
Определить, какая функция быстрее создаст и вернет требуемый список.

Output: list_comprehension()
"""
# import time

import time
def for_and_append():  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result

def list_comprehension():  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]

# инструмент решения
def get_min_time(fun):
    start = time.perf_counter()
    fun()
    delta = time.perf_counter() - start
    return delta, fun

def get_the_fastest_func(funcs: list):
    res = [get_min_time(el) for el in funcs]
    res = min(res, key=lambda x: x[0])
    return res[1].__name__
    # return res[0][1].__name__, res[0][0], res[1][1].__name__, res[1][0]
    # ('for_and_append', 0.8620671, 'list_comprehension', 0.6320116999999998)

lst = [for_and_append, list_comprehension]
print(get_the_fastest_func(lst))  # list_comprehension


#  3.6-05
"""
Доступны три реализации функции, которая принимает в качестве аргумента итерируемый объект 
и возвращает список, элементами которого являются элементы переданного итерируемого объекта::
- с использованием цикла for и метода append()
- с использованием списочного выражения
- с использованием встроенной функции list()
Определить, какая функция быстрее создаст и вернет требуемый список на основе итерируемого объекта range(100_000)

Output: list_function
"""
import time

def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result

def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)

# инструмент решения
def get_min_time(fun, arg):
    start = time.perf_counter()
    fun(arg)
    delta = time.perf_counter() - start
    return delta, fun

def get_the_fastest_func(funcs: list, arg):
    res = [get_min_time(el,arg) for el in funcs]
    res = min(res, key=lambda x: x[0])
    return res[1].__name__
    # return res[0][1].__name__, res[0][0], res[1][1].__name__, res[1][0], res[2][1].__name__, res[2][0]
    # ('for_and_append', 0.00708940000000001, 'list_comprehension', 0.00391190000000001, 'list_function', 0.002072400000000002)

iter = range(100_000)
lst = [for_and_append, list_comprehension, list_function]
print(get_the_fastest_func(lst, iter))  # list_function

