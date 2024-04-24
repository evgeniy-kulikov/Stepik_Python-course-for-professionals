#  6.8 Тип данных Counter
""""""

"""
Помимо доступных для всех словарей методов, словарь Counter поддерживает еще четыре дополнительных:

most_common()
elements()
total() (начиная с Python 3.10)
subtract()
"""

# Метод most_common()
"""
Метод most_common() возвращает список наиболее повторяемых элементов и количество каждого из них. 
Метод возвращает список кортежей вида (ключ, число повторений)

Если методу most_common() передать целочисленный аргумент n, 
то он вернет n самых часто повторяющихся элементов.
"""
from collections import Counter

letters = Counter('mississippi')
numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])

print(letters.most_common())   # [('i', 4), ('s', 4), ('p', 2), ('m', 1)]
print(letters.most_common(3))  # [('i', 4), ('s', 4), ('p', 2)]

print(numbers.most_common())   # [(5, 3), (7, 3), (9, 3), (1, 2), (6, 1), (3, 1), (2, 1)]
print(numbers.most_common(4))  # [(5, 3), (7, 3), (9, 3), (1, 2)]


# Метод elements()
"""
Метод elements() возвращает итератор по элементам, 
в котором каждый элемент повторяется столько раз, во сколько установлено его значение. 
Элементы возвращаются в порядке их появления.
!!! Метод elements() возвращает итератор. 
"""
from collections import Counter

letters = Counter('mississippi')
numbers = Counter([5, 6, 7, 1, 3, 9, 9, 1, 2, 5, 5, 7, 7, 9])

print(list(letters.elements()))  # ['m', 'i', 'i', 'i', 'i', 's', 's', 's', 's', 'p', 'p']
print(list(numbers.elements()))  # [5, 5, 5, 6, 7, 7, 7, 1, 1, 3, 9, 9, 9, 2]

# Если количество элементов по некоторому ключу меньше единицы, то метод elements() проигнорирует его.
from collections import Counter

letters = Counter(i=4, s=4, a=0, p=2, b=-98, m=1)
print(list(letters.elements()))
# ['i', 'i', 'i', 'i', 's', 's', 's', 's', 'p', 'p', 'm']


# Метод total()
"""
В Python 3.10 появился метод total(), 
который вычисляет сумму всех значений Counter словаря, включая отрицательные.
"""
from collections import Counter

letters = Counter(i=4, s=4, a=0, p=2, b=-98, m=1)
print(letters.total())  # -87


# Метод subtract()
"""
Метод subtract() вычитает из значений элементов одного словаря Counter значения элементов другого словаря. 
Метод subtract() подобен методу update(), но вычитает количества, а не складывает их. 
При этом у результирующего словаря значения ключей могут быть нулевыми или отрицательными.
"""
from collections import Counter

counter1 = Counter(i=4, s=40, a=1, p=20, b=98, z=69)
counter2 = Counter(i=2, s=20, a=6, p=12, m=1, z=69)

counter1.subtract(counter2)       # обновляем значения в counter1

print(counter1)
# Counter({'b': 98, 's': 20, 'p': 8, 'i': 2, 'z': 0, 'm': -1, 'a': -5})


"""   *   *   *   Task   *   *   *   """


#  6.8-1
"""
На вход подается последовательность слов, разделенных пробелом.
определить наиболее часто встречаемое слово в введенной последовательности (игнорировать регистр) 
и вывести его в нижнем регистре.
"""
from collections import Counter

s = input().lower().split()
res = Counter(s).most_common()
print(res[0][0])


#  6.8-2
"""
подается последовательность слов, разделенных пробелом.
определить наименее часто встречаемое слово в введенной последовательности 
и вывести его в нижнем регистре. 
Если таких слов несколько, программа должна вывести их все в лексикографическом порядке, 
в нижнем регистре, разделяя запятой и пробелом.
"""
from collections import Counter

s = input().lower().split()
res = Counter(s).most_common()
val = res[-1][1]
res = filter(lambda x: x[1] == val, res)
print(*[k for k, v in sorted(res)], sep=', ')


#  6.8-3
"""
Подается последовательность слов, разделенных пробелом.

Определить наиболее часто встречаемое слово в введенной строке 
и вывести его в нижнем регистре. 
Если таких слов несколько, программа должна вывести то, 
которое больше в лексикографическом сравнении (в нижнем регистре).
"""
from collections import Counter

s = input().lower().split()
res = Counter(s).most_common()
val = res[0][1]
res = filter(lambda x: x[1] == val, res)
print(sorted(res)[-1][0])


#  6.8-4
"""
Подается последовательность слов, разделенных пробелом.
Напишите программу, которая группирует слова из этой последовательности по их длине 
и определяет количество слов в каждой полученной группе.
Input:  Не сможет больше мальчик дотронуться до солнца
Output: Слов длины 8: 1
        Слов длины 2: 1
        Слов длины 7: 2
        Слов длины 5: 2
        Слов длины 4: 3
"""
from collections import Counter

ls = map(len, input().lower().split())
# ls = [len(el) for el in input().lower().split()]
res = Counter(ls).most_common()
for k, v in sorted(res, key=lambda x: x[1]):
    print(f"Слов длины {k}: {v}")


#  6.8-5
"""
На вход программе подается произвольное количество строк, 
в каждой из которых записаны имя очередного ученика 
и его оценка, разделенные пробелом.

Определить второго по счету ученика, который имеет самую низкую оценку, 
и вывести его имя.
"""
from collections import Counter

import sys

ls = [(int(num), name) for name, num in map(str.split, sys.stdin)]
print(sorted(ls)[1][1])


#  6.8-6
"""
https://stepik.org/lesson/635441/step/17?thread=solutions&unit=631831
"""
from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

# data.__dict__['min_values'] = lambda: list(filter(lambda x: x[1] == data.most_common()[-1][1], data.items()))
data.__dict__['min_values'] = lambda: [(k, v) for k, v in data.items() if v == min(data.values())]

# data.__dict__['max_values'] = lambda: list(filter(lambda x: x[1] == data.most_common()[0][1], data.items()))
data.__dict__['max_values'] = lambda: [(k, v) for k, v in data.items() if v == max(data.values())]

# print(data.min_values())
# print(data.max_values())


#  6.8-8
"""
Here we go again
https://stepik.org/lesson/635441/step/18?unit=631831
Input:  *
Output: *
"""
import csv
from collections import Counter

with open('name_log.csv', encoding='utf-8') as file:
    headers, *rows = csv.reader(file)
    for k, v in sorted(Counter(map(lambda x: x[1], rows)).items()):
        print(f'{k}: {v}')

# Вариант
with open('name_log.csv', encoding='utf-8') as file:
    data = csv.reader(file)
    next(data)
    emails = sorted(Counter(map(lambda e: e[1], data)).items())
    print(*[f"{k}: {v}" for k, v in emails], sep="\n")


#  6.8-9
"""
https://stepik.org/lesson/635441/step/19?unit=631831
Функция scrabble()
Функция должна возвращать True, 
если из набора символов symbols можно составить слово word, 
или False в противном случае.

"""
from collections import Counter

def scrabble(symbols: str, word: str):
    letters = Counter(symbols.lower())
    core = Counter(word.lower())
    s = letters | core
    # return letters & core == core  # Вариант 1
    # return letters | core == letters  # Вариант 2
    # return core <= letters  # Вариант 3
    # return not len(core - letters)  # Вариант 4
    return not bool(core - letters)


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))  # True
print(scrabble('begk', 'beegeek'))  # False


#  6.8-10
"""
https://stepik.org/lesson/635441/step/20?unit=631831
Функция print_bar_chart()
Функция должна определять:
- сколько раз встречается каждый символ в строке, если data является строкой
- сколько раз встречается каждая строка в списке, если data является списком
Input:  print_bar_chart('beegeek', '+')
Output: e |++++
        b |+
        g |+
        k |+
"""
from collections import Counter

def print_bar_chart(data: (str, list), mark: str):
    cnt = Counter(data)
    # length = len(max(data, key=len))
    length = max(map(len, data))
    print(*[f"{k.ljust(length)} |{mark * v}" for k, v in
            sorted(cnt.items(), key=lambda x: -x[1])], sep="\n")


# Вариант
def print_bar_chart(data: (str, list), mark: str):
    cnt = Counter(data).most_common()
    length = max(map(len, data))
    print(*[f"{k.ljust(length)} |{mark * v}" for k, v in
            sorted(cnt, key=lambda x: -x[1])], sep="\n")

print_bar_chart('beegeek', '+')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
print_bar_chart(languages, '#')


#  6.8-12
"""
Бесплатные курсы берут свое
https://stepik.org/lesson/635441/step/21?unit=631831

Input:  quarter1.csv, quarter2.csv, quarter3.csv, quarter4.csv, prices.json
Output: 924593
"""
# через defaultdict
import csv
import json
from collections import defaultdict

dt = defaultdict(int)

for n in '1234':
    with open(f'quarter{n}.csv', encoding='utf-8') as file:
        data = csv.reader(file)
        next(data)
        for el in data:
            dt[el[0]] += sum(map(int, el[1:]))

with open('prices.json', encoding='utf-8') as file:
    price = json.load(file)

print(sum(dt[k] * v for k, v in price.items()))


# через Counter
import csv
import json
from collections import Counter

ls = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']
cnt = Counter()

for el in ls:
    with open(el, encoding='utf-8') as file:
        data = csv.reader(file)
        next(data)
        cnt += Counter({el[0]: sum(map(int, el[1:])) for el in data})

with open('prices.json', encoding='utf-8') as file:
    price = json.load(file)

print(sum(cnt[k] * v for k, v in price.items()))


#  6.8-13
"""
Бесплатные курсы берут свое
https://stepik.org/lesson/635441/step/22?unit=631831

Есть список, в котором указаны учебники (с 1 по 11 класс), имеющиеся в наличии. 
Приходят n покупателей, называют номер класса, за который они хотят приобрести книгу, 
и сумму, которую они готовы заплатить, и если книга есть в наличии, этот учебник продается.

Вычислить общую сумму денег, которая будет заработана на продаже учебников.

Input:  1 1 11 9 5 5 7 9 9
        7
        1 300
        1 250
        11 400
        1 300
        7 200
        9 400
        7 250
Output: 1550
"""
from collections import Counter

books = Counter(map(int, input().split()))
total = 0

for _ in range(int(input())):
    book, price = map(int, input().split())
    total += bool(books[book]) * price
    books -= Counter({book: 1})

print(total)


# Вариант через sys.stdin
from collections import Counter
import sys

data = [tuple(line.split()) for line in sys.stdin]
books = Counter(data[0])
customer = int(data[1][0])
total = 0
for k, v in data[2:]:
    if k in books:
        total += int(v)
        books -= Counter({k: 1})
print(total)
