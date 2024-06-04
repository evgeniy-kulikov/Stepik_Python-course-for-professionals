# 10.12 Модуль itertools
""""""


"""   *   *   *   Task   *   *   *   """


#  10.12-1
"""
Подается произвольная строка из строчных латинских букв, длина которой не превышает 10 символов.
Вывести все перестановки символов данной строки без дубликатов в алфавитном порядке, каждую на отдельной строке.
Input:  aab
Output: aab
        aba
        baa
"""
from itertools import permutations

data = permutations(input())
[print(''.join(el)) for el in sorted(set(data))]


#  10.12-2
"""
https://stepik.org/lesson/680669/step/12?unit=679339
Вывести количество способов, которыми может приобрести товар стоимостью 100 у.е.
wallet - список доступных номиналов у.е.
"""
from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

cnt = 0
for el in range(1, len(wallet) + 1):
    data = set(combinations(wallet, el))
    res = (1 for el in data if sum(el) == 100)
    cnt += sum(res)
print(cnt)  # 16

# Вариант
cnt = 0
for el in range(1, len(wallet) + 1):
    for elem in set(combinations(wallet, el)):
        if sum(elem) == 100:
            cnt += 1
print(cnt)  # 16


#  10.12-3
"""
https://stepik.org/lesson/680669/step/13?unit=679339
Вывести количество способов, которыми может приобрести товар стоимостью 100 у.е.
Можно использовать купюру одного номинала произвольное количество раз
wallet - список доступных номиналов у.е.
"""
from itertools import combinations, permutations, combinations_with_replacement

wallet = [100, 50, 20, 10, 5]

cnt = 0
for el in range(1, 21):  # 20 - макс. кол-во из самых мелких купюр
    data = set(combinations_with_replacement(wallet, el))
    res = (1 for el in data if sum(el) == 100)
    cnt += sum(res)
print(cnt)  # 50

# # Вариант
cnt = 0
for el in range(1, 21):
    for elem in set(combinations_with_replacement(wallet, el)):
        if sum(elem) == 100:
            cnt += 1
print(cnt)  # 50


#  10.12-4
"""
Задача о рюкзаке
https://stepik.org/lesson/680669/step/14?unit=679339
Подается число — грузоподъемность рюкзака (в граммах)
Определить какие предметы из представленного набора следует взять, 
чтобы собрать рюкзак с максимальной ценностью предметов внутри, 
соблюдая при этом весовое ограничение рюкзака, 
и вывести названия полученных предметов в лексикографическом порядке, каждое на отдельной строке. 
Если рюкзак не позволяет взять ни один предмет, программа должна вывести текст:
Рюкзак собрать не удастся

Input:  500
Output: Золотая монета
        Мобильный телефон
        Наушники
        Обручальное кольцо
        Ручка Паркер
"""
from itertools import combinations
from collections import namedtuple

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

weight = int(input())
summ, res = 0, None

for el in range(1, len(items) + 1):
    data = set(combinations(items, el))
    row = (el for el in data if sum(i.mass for i in el) <= weight)
    for kit in row:
        kit_summ = sum(i.price for i in kit)
        if kit_summ > summ:
            summ = kit_summ
            res = kit

if res:
    [print(el.name) for el in sorted(res, key=lambda x: x.name)]
else:
    print('Рюкзак собрать не удастся')


#  10.12-5
"""
Перепишите данную программу с использованием функции product(), чтобы она выполняла ту же задачу.
"""
from string import ascii_lowercase
from itertools import product

letters = ascii_lowercase[:8]
digits = [1, 2, 3, 4, 5, 6, 7, 8]

# for letter in letters:
#     for digit in digits:
#         print(letter, digit, sep='', end=' ')

for el in product(letters, digits):
    print(el[0], el[1], sep='', end=' ')

#  10.12-6
"""
Функция password_gen()
Вам доступна функция password_gen(), которая возвращает генератор, 
порождающий все трехсимвольные строковые пароли в порядке возрастания, 
составленные из цифр от 0 до 9 включительно.
Перепишите данную функцию с использованием функции product(), чтобы она выполняла ту же задачу.
"""
# def password_gen():
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 yield str(i) + str(j) + str(k)

from itertools import product

def password_gen():
    for el in product(range(10), range(10), range(10)):
        yield ''.join(map(str, el))

passwords = password_gen()
print(next(passwords))
print(next(passwords))
print(next(passwords))
# 000
# 001
# 002


#  10.12-7
"""
Системы счисления
На вход программе в первой строке подается 
натуральное число n≤16 — основание системы счисления, 
а затем натуральное число m — длина генерируемых чисел.
Сгенерировать в системе счисления n все числа длины m и вывести их в порядке возрастания через пробел.
В системах счислениях по основанию 11 и выше в качестве цифр 
должны использоваться заглавные латинские буквы: A,B,C,D,...
Input:  2
        3
Output: 000 001 010 011 100 101 110 111
"""
from itertools import product

n = int(input())
m = int(input())
num = '0123456789ABCDEF'

res = product(num[:n], repeat=m)
print(*(''.join(el) for el in res))
