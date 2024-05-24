# 10.5 Генераторы. Часть 1


"""   *   *   *   Task   *   *   *   """


#  10.5-1
"""
Реализуйте генераторную функцию simple_sequence(), которая не принимает никаких аргументов.
Функция должна возвращать генератор, порождающий бесконечную возрастающую последовательность натуральных чисел, 
в которой каждое число встречается столько раз, каково оно:
1,2,2,3,3,3,4,4,4,4,..
"""
def simple_sequence():
    n = 1
    while True:
        for _ in range(n):
            yield n
        n += 1


generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]
print(*numbers)
# 1 2 2 3 3 3 4 4 4 4


#  10.5-2
"""
Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:
count — натуральное число, по умолчанию имеет значение None
Если count имеет значение None, функция должна возвращать генератор, 
порождающий бесконечный знакочередующийся ряд натуральных чисел.
1, −2, 3, −4, 5, −6, 7, −8, 9, −10,...
Если count имеет в качестве значения натуральное число, 
функция должна возвращать генератор, порождающий первые count чисел знакочередующегося ряда натуральных чисел, 
а затем возбуждающий исключение StopIteration
"""
def alternating_sequence(count=None):
    n = 0
    sign = -1
    while n != count:
        n += 1
        sign *= -1
        yield n * sign

generator = alternating_sequence(10)
print(*generator)
# 1 -2 3 -4 5 -6 7 -8 9 -10


generator = alternating_sequence()
numbers = [next(generator) for _ in range(20)]
print(*numbers)
# 1 -2 3 -4 5 -6 7 -8 9 -10 11 -12 13 -14 15 -16 17 -18 19 -20


#  10.5-3
"""
Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:
left — натуральное число
right — натуральное число
Функция должна возвращать генератор, порождающий последовательность простых чисел от left до right включительно, 
а затем возбуждающий исключение StopIteration.
* Гарантируется, что left <= right
* Простое число — натуральное число, которое делиться только на единицу и самого себя.
"""
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False

    for i in range(3, (n // 2) + 1):
        if n % i == 0:
            return False
    return True


def primes(left, right):
    for n in range(left, right + 1):
        if is_prime(n):
            yield n


# Хорошее решение (нужна установка пакета sympy)
# https://www.sympy.org/ru/features.html
from sympy import isprime

def primes(left, right):
    for n in range(left, right + 1):
        if isprime(n):
            yield n


generator = primes(1, 15)
print(*generator)
# 2 3 5 7 11 13


#  10.5-4
"""
Реализуйте генераторную функцию reverse(), которая принимает один аргумент:
sequence — последовательность
Функция должна возвращать генератор, порождающий элементы последовательности sequence в обратном порядке, 
а затем возбуждающий исключение StopIteration.
* Последовательностью является коллекция, поддерживающая индексацию и имеющая длину. 
Например, объекты типа list, str, tuple
"""
def reverse(sequence):
    cnt = len(sequence) - 1
    while cnt >= 0:
        yield sequence[cnt]
        cnt -= 1

# Вариант
def reverse(sequence):
    for el in range(len(sequence) - 1, -1, -1):
        yield sequence[el]

# Короче
def reverse(sequence):
    for el in sequence[::-1]:
        yield el

print(*reverse([1, 2, 3, 4, 5]))
#  5 4 3 2 1


#  10.5-5
"""
Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:
start — дата, тип date
count — натуральное число, по умолчанию имеет значение None
Если count имеет значение None, функция должна возвращать генератор, 
порождающий последовательность из максимально допустимого количества дат (тип date), начиная с даты start.
Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, 
порождающий последовательность из count дат (тип date), начиная с даты start, 
а затем возбуждающий исключение StopIteration
"""
from datetime import date, timedelta

def dates(start: date, count=None):
    if count is None:
        count = (date.max - start).days + 1

    for el in range(count):
        yield start
        if start != date.max:
            start += timedelta(days=1)

# Короче
def dates(start, count=None):
    # count = count or (date.max - start).days + 1
    count = count if count else (date.max - start).days + 1
    for el in range(count):
        yield start + timedelta(days=el)

generator = dates(date(2022, 3, 8))
print(next(generator))
print(next(generator))
print(next(generator))
# 2022-03-08
# 2022-03-09
# 2022-03-10

generator = dates(date(2022, 3, 28), 5)
print(*generator)
# 2022-03-28 2022-03-29 2022-03-30 2022-03-31 2022-04-01

generator = dates(date(9999, 12, 29))
print(next(generator))
print(next(generator))
print(next(generator))
try:
    print(next(generator))
except StopIteration:
    print('Error')
# 9999-12-29
# 9999-12-30
# 9999-12-31
# Error


#  10.5-6
"""
Реализуйте генераторную функцию card_deck(), которая принимает один аргумент:
suit — одна из четырех карточных мастей: пик, треф, бубен, червей
Функция должна возвращать генератор, циклично порождающий колоду игральных карт без масти suit. 
Каждая карта должна представлять собой строку в следующем формате:
<номинал> <масть>
Например, 7 пик, валет треф, дама бубен, король червей, туз пик.
* Карты, генерируемые итератором, должны располагаться сначала по величине масти, затем номинала.
* Старшинство мастей по возрастанию: пики, трефы, бубны, червы. 
  Старшинство карт в масти по возрастанию: двойка, тройка, четверка, пятерка, шестерка, семерка, восьмерка, 
  девятка, десятка, валет, дама, король, туз.
"""
def card_deck(suit):
    card = [str(i) for i in range(2, 11)] + ['валет', 'дама', 'король', 'туз']
    cut_suit = ['пик', 'треф', 'бубен', 'червей']
    cut_suit.remove(suit)
    # cut_suit = [i for i in ['пик', 'треф', 'бубен', 'червей'] if i != suit]
    idx = -1

    while True:
        idx += 1
        res = f'{card[idx % 13]} {cut_suit[idx // 13]}'
        yield res
        if idx == 38:
            idx = -1


generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]
print(*cards)
# 2 пик 3 пик 4 пик 5 пик ... дама червей король червей туз червей 2 пик


#  10.5-7
"""
Доступна генераторная функция matrix_by_elem(), 
которая принимает в качестве аргумента матрицу произвольной размерности 
и возвращает генератор, порождающий последовательность элементов переданной матрицы.
Перепишете данную функцию с использованием конструкции yield from, чтобы она выполняла ту же задачу.
* Под матрицей подразумеваются исключительно вложенные списки.
"""
# def matrix_by_elem(matrix):
#     for row in matrix:
#         for elem in row:
#             yield elem

def matrix_by_elem(matrix):
    for row in matrix:
        yield from row


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(*matrix_by_elem(matrix))
# 1 2 3 4 5 6 7 8 9


#  10.5-8
"""
Реализуйте генераторную функцию palindromes(), которая не принимает никаких аргументов.
Функция должна возвращать генератор, порождающий бесконечную последовательность натуральных чисел-палиндромов.
* Число-палиндром — число, которое читается одинаково как справа налево, так и слева направо.
"""
def palindromes():
    num = 1
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1

# # Срабатывает ограничение по глубине рекурсии в тестах 3 и 4
# def palindromes(num=1):
#     if str(num) == str(num)[::-1]:
#         yield num
#     yield from palindromes(num + 1)


generator = palindromes()
numbers = [next(generator) for _ in range(30)]
print(*numbers)
# 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212

# TEST_3:
generator = palindromes()
for _ in range(10_000):
    next(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# 9002009
# 9003009
# 9004009
# 9005009
# 9006009
# 9007009


#  10.5-9
"""
Реализуйте генераторную функцию flatten(), которая принимает один аргумент:
nested_list — список, элементами которого являются целые числа или списки, 
элементами которых, в свою очередь, также являются либо целые числа, либо списки; 
вложенность может быть произвольной
Функция должна возвращать генератор, порождающий все числа, содержащиеся в nested_list, 
включая все числа из всех вложенных списков, а затем возбуждает исключение StopIteration.
"""
def flatten(ls: list):
    for el in ls:
        if isinstance(el, int):
            yield el
        else:
            yield from flatten(el)

generator = flatten([[1, 2], [[3]], [[4], 5]])
print(*generator)
# 1 2 3 4 5
