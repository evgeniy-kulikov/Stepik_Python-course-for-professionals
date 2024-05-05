# 9.1 Встроенные функции
""""""


"""   *   *   *   Task   *   *   *   """


#  9.1-1
"""
Вывести все строчные латинские буквы от a до z, каждую на отдельной строке.
"""
from string import ascii_lowercase as st

[print(el) for el in st]


#  9.1-2
"""
Реализуйте функцию convert(), которая принимает один аргумент:
number — целое число
Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:
двоичное представление числа number в виде строки без префикса 0b
восьмеричное представление числа number в виде строки без префикса 0o
шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x
"""
def convert(num):
    return f'{num:b}', f'{num:o}', f'{num:X}'
    # return bin(num).replace('0b', ''), oct(num).replace('0o', ''), hex(num).replace('0x', '').upper()

print(convert(15))  # ('1111', '17', 'F')
print(convert(-24))  # ('1111', '17', 'F')


#  9.1-3
"""
https://stepik.org/lesson/640035/step/8?unit=636555
Вывести название фильма с наименьшей средней оценкой.
"""
films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
         'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
         'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
         'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
         'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
         'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
         'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
         'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
         'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
         'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}

# Хорошее решение
res = min(films, key=lambda x: sum(films[x].values()) / 2)
print(res)

# Вариант
res = [(k, sum(v.values()) / 2) for k, v in films.items()]
res.sort(key=lambda x: x[1])
print(res[0][0])

# Короче
res = [(k, sum(v.values()) / 2) for k, v in films.items()]
res = min(res, key=lambda x: x[1])
print(res[0])


#  9.1-4
"""
non_negative_even()
Функция должна возвращать True, 
если все числа в списке numbers являются четными и неотрицательными, 
или False в противном случае.
Input:  print(non_negative_even([0, 2, 4, 8, 16]))
Output: True
"""
def non_negative_even(num: list):
    return all(not el % 2 and el >= 0 for el in num)

print(non_negative_even([0, 2, 4, 8, 16]))  # True
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))  # False


#  9.1-5
"""
Реализуйте функцию is_greater(), которая принимает два аргумента в следующем порядке:
lists — список, элементами которого являются списки целых чисел
number — целое число
Функция должна возвращать True, 
если хотя бы в одном вложенном списке из списка lists сумма всех элементов больше number, 
или False в противном случае.
Input:  data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
        print(is_greater(data, 10))
Output: True
"""
def is_greater(lists: list, num):
    res = any(sum(el) > num for el in lists)
    return res

# data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
# print(is_greater(data, 10))


#  9.1-6
"""
Реализуйте функцию custom_isinstance(), которая принимает два аргумента в следующем порядке:

objects — список произвольных объектов
typeinfo — тип данных или кортеж с типами
Функция должна возвращать единственное число — количество объектов из списка objects, 
которые принадлежат типу typeinfo или одному из типов, если был передан кортеж.
Input:  numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
        print(custom_isinstance(numbers, int))
Output: 2
"""
def custom_isinstance(objects: list, typeinfo):
    res = sum(isinstance(el, typeinfo) for el in objects)
    return res

# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, (int, float)))


#  9.1-7
"""
Вывести индекс максимального элемента в списке.
"""
numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354,
           1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370,
           2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729,
           5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722,
           -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062,
           9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]

print(numbers.index(max(numbers)))

print(max(enumerate(numbers), key=lambda el: el[1])[0])

# Примитивное решение
idx, num = 0, numbers[0]
for el in numbers[1:]:
    if el > num:
        num = el
        idx = numbers.index(el)
print(idx)


#  9.1-8
"""
Функция my_pow()
https://stepik.org/lesson/640035/step/13?unit=636555
Функция должна возвращать сумму, 
состоящую из цифр числа, возведенных в степень их порядкового номера.
139 -> 1^1 + 3^2 + 9^3 = 1 + 9 + 729 = 739
"""
def my_pow(num):
    return sum(pow(int(v), k) for k, v in enumerate(str(num), 1))

# print(my_pow(139))


#  9.1-9
"""
https://stepik.org/lesson/640035/step/14?unit=636555
Дополните приведенный ниже код, чтобы он определил, какую прибыль принес каждый мультфильм, 
и вывел названия мультфильмов, указав для каждого соответствующую прибыль. 
Мультфильмы должны быть расположены в лексикографическом порядке.
Cars: 342216280$
Coco: 627082196$
Finding Nemo: 846335536$
...
"""
names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]

res = [(a, b - c) for a, b, c in zip(names, box_offices, budgets)]
# res = [(v, box_offices[k] - budgets[k]) for k, v in enumerate(names)]

for el in sorted(res):
    print(f'{el[0]}: {el[1]}$')

# Вариант
[print(f'{a}: {c - b}$') for a, b, c in sorted(zip(names, budgets, box_offices))]


#  9.1-10
"""
Функция zip_longest()
https://stepik.org/lesson/640035/step/15?unit=636555

Input:  zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_')
Output: [(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]
"""
def zip_longest(*ls: list, fill=None):
    res = []
    idx = max(map(len, [*ls]))

    for col in range(idx):
        el = []
        for row in ls:
            if len(row) > col:
                el += [row[col]]
            else:
                el += [fill]
        res += [tuple(el)]
    return res


# Короче
def zip_longest(*ls: list, fill=None):
    idx = max(map(len, [*ls]))
    for el in ls:
        el += [fill] * (idx - len(el))
    return list(zip(*ls))


# print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]


#  9.1-11
"""
Необычная сортировка 🌶️
https://stepik.org/lesson/640035/step/16?unit=636555
Дана строка, содержащая латинские буквы и цифры. 
Отсортировать символы в строке согласно следующим правилам:

- все отсортированные строчные буквы стоят перед заглавными буквами
- все отсортированные заглавные буквы стоят перед цифрами
- все отсортированные нечетные цифры стоят перед отсортированными четными

Input:  Sorting1234
Output: ginortS1324
"""

st = input()

low = list(sorted(filter(lambda x: x.islower(), st)))
up = list(sorted(filter(lambda x: x.isupper(), st)))
num = list(sorted(filter(lambda x: x.isnumeric(), st), key=lambda x: (not int(x) % 2, x)))
res = ''.join(low + up + num)

print(res)


# Вариант преподавателя
def get_key(char):
    if char.isalpha():
        return 0, char.isupper(), char
    digit = int(char)
    return 1, digit % 2 == 0, digit

st = input()
print(''.join(sorted(st, key=get_key)))
