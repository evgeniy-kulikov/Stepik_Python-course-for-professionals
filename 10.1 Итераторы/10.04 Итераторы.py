# 10.4 Итераторы. Часть 4
""""""


"""   *   *   *   Task   *   *   *   """


#  10.4-1
"""
Реализуйте класс Repeater, порождающий итераторы, конструктор которого принимает один аргумент:
obj — произвольный объект
Итератор класса Repeater должен бесконечно генерировать единственное значение — obj
"""
# class Repeater:
#     def __init__(self, ____):
#         pass
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         pass
class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        # if len(self.obj) == 0:
        #     raise StopIteration
        return self.obj


geek = Repeater('geek')
print(next(geek))
print(next(geek))
print(next(geek))
# geek
# geek
# geek


#  10.4-2
"""
Реализуйте класс BoundedRepeater, порождающий итераторы, 
конструктор которого принимает два аргумента в следующем порядке:
obj — произвольный объект
times — натуральное число
Итератор класса BoundedRepeater должен генерировать значение obj times раз, 
а затем возбуждать исключение StopIteration.
"""
# class BoundedRepeater:
#     def __init__(self, ____, ____):
#         pass
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         pass

class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cnt += 1
        if self.cnt > self.times:
            raise StopIteration
        return self.obj


# Вариант без cnt
class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.times == 0:
            raise StopIteration
        self.times -= 1
        return self.obj


geek = BoundedRepeater('geek', 3)
print(next(geek))
print(next(geek))
print(next(geek))

try:
    print(next(geek))
except StopIteration:
    print('Error')
# geek
# geek
# geek
# Error


#  10.4-3
"""
Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:
n — натуральное число,
Итератор класса Square должен генерировать последовательность из n чисел, 
каждое из которых является квадратом очередного натурального числа, 
а затем возбуждать исключение StopIteration.
* Последовательность квадратов натуральных чисел начинается с квадрата числа 1
"""
class Square:
    def __init__(self, num):
        self.num = num
        self.cnt = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.cnt += 1
        if self.cnt > self.num:
            raise StopIteration
        return self.cnt ** 2


squares = Square(2)

print(next(squares))
print(next(squares))
# 1
# 4

squares = Square(10)
print(list(squares))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#  10.4-4
"""
Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких аргументов.
Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел Фибоначчи, начиная с 1.
Последовательность Фибоначчи – последовательность натуральных чисел, 
где каждое последующее число является суммой двух предыдущих:
1, 1, 2, 3, 5, 8, 13, 21, 34 ...
"""
class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


fibonacci = Fibonacci()

for _ in range(10):
    print(next(fibonacci), end=' ')
# 1 1 2 3 5 8 13 21 34 55


#  10.4-5
"""
Реализуйте класс PowerOf, порождающий итераторы, конструктор которого принимает один аргумент:
number — ненулевое число
Итератор класса PowerOf должен генерировать бесконечную последовательность 
целых неотрицательных степеней числа number в порядке возрастания, начиная с нулевой степени.
"""
class PowerOf:
    def __init__(self, number):
        self.number = number
        self.degree = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.degree += 1
        return self.number ** self.degree


power_of_two = PowerOf(2)
for _ in range(10):
    print(next(power_of_two), end=' ')
# 1 2 4 8 16 32 64 128 256 512


#  10.4-6
"""
Реализуйте класс DictItemsIterator, порождающий итераторы, конструктор которого принимает один аргумент:
data — словарь
Итератор класса DictItemsIterator должен генерировать последовательность кортежей, 
представляющих собой пары ключ-значение словаря data, а затем возбуждать исключение StopIteration.
* При решении задачи не используйте словарные методы keys(), values() и items().
* Пары ключ-значение в возвращаемом функцией итераторе должны располагаться в своем изначальном порядке
"""
class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.idx = -1
        self.key = list(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx >= len(self.key):
            raise StopIteration
        return self.key[self.idx], self.data[self.key[self.idx]]


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
print(*pairs)
# (1, 'A') (2, 'B') (3, 'C')


#  10.4-7
"""
Реализуйте класс CardDeck, порождающий итераторы, конструктор которого не принимает никаких аргументов.
Итератор класса CardDeck должен генерировать последовательность из 52 игральных карт, 
а после возбуждать исключение StopIteration. 
Каждая карта должна представлять собой строку в следующем формате:
<номинал> <масть>
(7 пик, валет треф, дама бубен, король червей, туз пик)
* Карты, генерируемые итератором, должны располагаться сначала по величине номинала, затем масти.
* Старшинство мастей по возрастанию: пики, трефы, бубны, червы. 
  Старшинство карт в масти по возрастанию: двойка, тройка, ..., девятка, десятка, валет, дама, король, туз.
* Масти не требуют склонения: пик, треф, бубен, червей.
# self.card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
"""


class CardDeck:
    def __init__(self):
        self.card = [i for i in range(2, 11)] + ['валет', 'дама', 'король', 'туз']
        self.suit = ['пик', 'треф', 'бубен', 'червей']
        self.cnt = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.cnt += 1
        if self.cnt > 51:
            raise StopIteration
        return f'{self.card[self.cnt % 13]} {self.suit[self.cnt // 13]}'


class CardDeck:
    def __init__(self):
        self.cards = [f'{j} {i}' for i in ('пик', 'треф', 'бубен', 'червей') for j in
                      ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')]
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        if self.idx > 51:
            raise StopIteration
        return self.cards[self.idx]


cards = CardDeck()
print(next(cards))  # 2 пик
print(next(cards))  # 3 пик

# for _ in range(52):
#     print(next(cards))


#  10.4-8
"""
Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:
iterable — итерируемый объект
Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого объекта iterable.
* Гарантируется, что итерируемый объект, передаваемый в конструктор класса, не является множеством и итератором.
* Элементы итерируемого объекта, генерируемые итератором, должны располагаться в своем изначальном порядке.
"""
class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        return self.iterable[self.idx % len(self.iterable)]


cycle = Cycle('be')
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
# b
# e
# b
# e


#  10.4-9
"""
Итератор RandomNumbers
Реализуйте класс RandomNumbers, порождающий итераторы, 
конструктор которого принимает три аргумента в следующем порядке:
left — целое число
right — целое число
n — натуральное число
Итератор класса RandomNumbers должен генерировать последовательность 
из n случайных чисел от left до right включительно, 
а затем возбуждать исключение StopIteration.
Примечание 1. Гарантируется, что left <= right.
"""
from random import randint

class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.n -= 1
        if self.n < 0:
            raise StopIteration
        return randint(self.left, self.right)


iterator = RandomNumbers(1, 1, 3)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# 1
# 1
# 1


#  10.4-10
"""
Итератор Alphabet 🌶️
Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:
language — код языка: ru — русский, en — английский
Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:
русского алфавита, если language имеет значение ru
английского алфавита, если language имеет значение en
* Буква ё в русском алфавите не учитывается.
"""
class Alphabet:
    def __init__(self, language):
        self.language = language
        self.idx = -1
        self.alphabet = {'en': [26, 'abcdefghijklmnopqrstuvwxyz'],
                         'ru': [32, 'абвгдежзийклмнопрстуфхцчшщъыьэюя']}

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        return self.alphabet[self.language][1] \
            [self.idx % self.alphabet[self.language][0]]


# Вариант
class Alphabet:
    def __init__(self, language: str):
        if language == "ru":
            self.alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        elif language == "en":
            self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        self.idx %= len(self.alphabet)
        return self.alphabet[self.idx]


ru_alpha = Alphabet('ru')
print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))

en_alpha = Alphabet('en')
letters = [next(en_alpha) for _ in range(28)]
print(*letters)
# a b c d e f g h i j k l m n o p q r s t u v w x y z a b


#  10.4-11
"""
Итератор Xrange 🌶️
Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента в следующем порядке:
start — целое или вещественное число
end — целое или вещественное число
step — целое или вещественное число, по умолчанию имеет значение 1
Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии от start до end, 
включая start и не включая end, с шагом step, а затем возбуждать исключение StopIteration
"""
class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start - step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step

        if self.step > 0 and self.current >= self.end:
            raise StopIteration
        if self.step < 0 and self.current <= self.end:
            raise StopIteration

        return self.current


# Вариант
class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start - step
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.start - self.end) <= abs(self.step):
            raise StopIteration

        self.start += self.step
        return self.start


evens = Xrange(0, 10, 2)
print(*evens)
# 0 2 4 6 8

xrange = Xrange(0, 3, 0.5)
print(*xrange, sep='; ')
# 0.0; 0.5; 1.0; 1.5; 2.0; 2.5

xrange = Xrange(10, 1, -1)
print(*xrange)
# 10 9 8 7 6 5 4 3 2

xrange = Xrange(-50, -49)
print(*xrange)  # -50

