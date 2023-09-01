# 2.1 Повторяем основные конструкции языка Python. Часть 1
""""""

# 01
"""
Реализуйте функцию hide_card(), которая принимает один аргумент:
card_number — строка, представляющая собой корректный номер банковской карты из 1616 цифр,
между которыми могут присутствовать символы пробела
Функция должна заменять первые 1212 цифр в строке card_number на символ * и возвращать полученный результат.
Если между цифрами в номере имелись символы пробела, их следует удалить.

Sample Input :
card = '1234567890123456'
print(hide_card(card))
Sample Output:
************3456
"""
def hide_card(card_number):
    s = card_number.replace(' ', '')[-4:]
    new_s = '*' * 12 + s
    return new_s


# 02
"""
Реализуйте функцию same_parity(), которая принимает один аргумент:
numbers — список целых чисел
Функция должна возвращать новый список, элементами которого являются числа из списка numbers, имеющие ту же четность, 
что и первый элемент этого списка.
Примечание: Числа в возвращаемом функцией списке должны располагаться в своем исходном порядке.

Sample Input :
print(same_parity([6, 0, 67, -7, 10, -20]))
Sample Output:
[6, 0, 10, -20]
"""
def same_parity(numbers):
    lst = []
    if len(numbers) == 0:
        lst = []
    elif numbers[0] % 2 == 0:
        for el in numbers:
            if el % 2 == 0:
                lst.append(el)
    else:
        for el in numbers:
            if el % 2 != 0:
                lst.append(el)
    return lst


# переделанное решение
def same_parity1(numbers):
    lst = []
    if numbers:  # если список не пустой
        first = numbers[0] % 2  # "0" или "1" (четное / нечетное  первое число)
        for el in numbers:
            if el % 2 == first:  # "0" или "1"
                lst.append(el)
    return lst


# Одно из возможных решений задачи
def same_parity2(numbers):
    return [i for i in numbers if i % 2 == numbers[0] % 2]


# 03
"""
Функция is_valid()
Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:
    состоит из 4, 5 или 6 символов
    состоит только из цифр (0 - 9
    не содержит пробелов
Реализуйте функцию is_valid(), которая принимает один аргумент:
string — произвольная строка
Функция должна возвращать значение True, если строка string представляет собой корректный PIN-код, 
или False в противном случае.
Примечание 1. Если в функцию передается пустая строка, функция должна возвращать значение False.
"""
def is_valid(string):
    if (3 < len(string) < 7) and string.isdigit():
        return True
    else:
        return False


# 04
"""
Реализуйте функцию print_given(), которая принимает произвольное количество позиционных и именованных аргументов 
и выводит все переданные аргументы, указывая тип каждого. 
Пары аргумент-тип должны выводиться каждая на отдельной строке, в следующем формате:
для позиционных аргументов:     <значение аргумента> <тип аргумента>
для именованных аргументов:     <имя переменной> <значение аргумента> <тип аргумента>
"""
def print_given(*arg, **kwargs):
    for el in arg:
        print(el, type(el))
    for el in dict(sorted(kwargs.items())):  # лучше так не делать!!!
        print(el, kwargs[el], type(kwargs[el]))


#  более верное решение
def print_given1(*args, **kwargs):
    for el in args:
        print(el, type(el))
    for key, value in sorted(kwargs.items()):  # sorted(kwargs.items()) отсортированный по ключу список кортежей
        print(key, value, type(value))


# 05
"""
Реализуйте функцию convert(), которая принимает один аргумент: string — произвольная строка
Функция должна возвращать строку string:
* полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
* полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
* полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
Примечание: Символы строки, не являющиеся буквами, следует игнорировать.
"""
def convert(string):
    cnt_low, cnt_up = 0, 0
    for el in string:
        if el.islower():
            cnt_low += 1
        elif el.isupper():
            cnt_up += 1
    if cnt_up > cnt_low:
        return string.upper()
    return string.lower()


# 06
"""
Анаграммы — это слова, которые состоят из одинаковых букв.
    Например: адаптер — петарда
Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:
    word — слово в нижнем регистре
    words — список слов в нижнем регистре
Функция должна возвращать список, элементами которого являются слова из списка words,
которые представляют анаграмму слова word. Если список words пуст или не содержит анаграмм,
функция должна вернуть пустой список.
Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке.
Примечание 2. Считайте, что слово является анаграммой самого себя.
Sample Input  1:
word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
Sample Output 1:
['aabb', 'bbaa']
"""
def filter_anagrams(word, words):
    w = ''.join(sorted(word))  # 'aabb'
    lst = []
    for _ in range(len(words)):
        if ''.join(sorted(words[_])) == w:
            lst.append(words[_])
    return lst

def filter_anagrams(word, words):
    w = sorted(word)  # ['a', 'a', 'b', 'b']
    lst = []
    for _ in range(len(words)):
        if sorted(words[_]) == w:
            lst.append(words[_])
    return lst

# решение автора
def filter_anagrams(word, anagrams):
    return [_ for _ in anagrams if sorted(_) == sorted(word)]


# 07
"""
Реализуйте функцию likes(), которая принимает один аргумент: names — список имён
Функция должна возвращать строку в соответствии с примерами ниже, 
содержание которой зависит от количества имён в списке names.

Приведенный ниже код:

print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))

должен выводить:

Никто не оценил данную запись
Тимур оценил(а) данную запись
Тимур и Артур оценили данную запись
Тимур, Артур и Руслан оценили данную запись
Тимур, Артур и 2 других оценили данную запись
Тимур, Артур и 3 других оценили данную запись

Примечание 1. Имена в формируемой и возвращаемой функцией строке должны располагаться в своем исходном порядке.
Примечание 2. Обратите внимание, что если в передаваемом в функцию списке более трех имен, 
то явно указываются лишь первые два из них. 
"""
def likes(lst):
    if len(lst) == 0:
        return 'Никто не оценил данную запись'
    elif len(lst) < 2:
        return f'{lst[0]} оценил(а) данную запись'
    elif len(lst) < 3:
        return f'{lst[0]} и {lst[1]} оценили данную запись'
    elif len(lst) < 4:
        return f'{lst[0]}, {lst[1]} и {lst[2]} оценили данную запись'
    else:
        return f'{lst[0]}, {lst[1]} и {len(lst) - 2} других оценили данную запись'

# Используя словарь
def likes(lst):
    dict_out = {0: "Никто не оценил данную запись",
                1: "f'{lst[0]} оценил(а) данную запись'",
                2: "f'{lst[0]} и {lst[1]} оценили данную запись'",
                3: "f'{lst[0]}, {lst[1]} и {lst[2]} оценили данную запись'",
                4: "f'{lst[0]}, {lst[1]} и {len(lst) - 2} других оценили данную запись'"}

    if len(lst) == 0:
        return dict_out[0]
    elif len(lst) == 1:
        return eval(dict_out[1])
    elif len(lst) == 2:
        return eval(dict_out[2])
    elif len(lst) == 3:
        return eval(dict_out[3])
    else:
        return eval(dict_out[4])


# 08
"""
Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
numbers — список целых чисел
number — целое число
Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс. 
Если список numbers пуст, функция должна вернуть число -1.
Примечание 1. Если в функцию передается список, содержащий несколько чисел, 
одновременно являющихся ближайшими к искомому числу, функция должна возвращать наименьший из индексов ближайших чисел.

Input 1:    print(index_of_nearest([], 17))
Output 1:   -1

Input 2:    print(index_of_nearest([7, 13, 3, 5, 18], 0))
Output 2:   2

Input 3:    print(index_of_nearest([7, 5, 4, 4, 3], 4))
Output 3:   2
"""
def index_of_nearest(numbers, number):
    if numbers:  # если список не пустой, то ...
        if len(numbers) == 1:
            return 0
        else:
            idx = 0  # индекс (для первого элемента списка)
            min_diff = abs(number - numbers[0])  # фиксируем минимальную абсолютную разницу (для первого элемента списка)
            for el in range(1, len(numbers)):
                if abs(number - numbers[el]) < min_diff:  # ищем еще меньшие значения абсолютной разницы
                    idx = el
                    min_diff = abs(number - numbers[el])
            return idx
    return -1  # если список пустой


# Решение преподавателя
def index_of_nearest(numbers, number):
    if numbers:
        minimum = min(numbers, key=lambda x: abs(x - number))
        return numbers.index(minimum)
    return -1

# пояснение:
numbers = [10, 16, -12, -17, -15, -17]
number = -16
def index_of_nearest(numbers, number):
    if numbers:
        minimum = min(numbers, key=lambda x: abs(x - number))  # min([-17, -17, -15, -12, 10, 16])
        return numbers.index(minimum)  # index() находит первое вхождение в списке [10, 16, -12, -17, -15, -17]
    return -1


# 09
"""
Реализуйте функцию spell(), 
которая принимает произвольное количество позиционных аргументов-слов и возвращает словарь, 
ключи которого — первые буквы слов, а значения — максимальные длины слов на эту букву.
Примечание 1. Если в функцию не передается ни одного аргумента, функция должна возвращать пустой словарь.
Примечание 2. Функция должна игнорировать регистр слов, 
            при этом в результирующий словарь должны попасть именно буквы в нижнем регистре.
Input:  words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
Output: {'р': 7, 'а': 9, 'у': 10, 'к': 5}
"""
def spell(*words):
    ls = sorted(words, key=len)
    d = {el[0].lower(): len(el) for el in ls}
    return d

# words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
# print(spell(*words))

# Вариант преподавателя
def spell(*args):
    result = {}
    for word in args:
        if result.get(word[0].lower(), 0) < len(word):
            result[word[0].lower()] = len(word)
    return result


# 10
"""
Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:
amount — натуральное число, количество
declensions — кортеж из трех вариантов склонения существительного

Функция должна возвращать строку, 
полученную путем объединения подходящего существительного из кортежа declensions и количества amount, 
в следующем формате:
<количество> <существительное>

Примечание 1. Передаваемый в функцию кортеж легко составить по мнемоническому правилу: один, два, пять. Например:
для слова «арбуз»: арбуз, арбуза, арбузов
для слова «рубль»: рубль, рубля, рублей

Input:  print(choose_plural(21, ('пример', 'примера', 'примеров')))
Output: 21 пример

Input:  print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
Output: 92 гвоздя
"""


def choose_plural(amount: int, declensions: tuple) -> str:
    one, dual = amount % 10, amount % 100
    if one == 1 and dual != 11:
        return f'{amount} {declensions[0]}'
    elif one in (2, 3, 4) and dual not in (12, 13, 14):
        return f'{amount} {declensions[1]}'
    return f'{amount} {declensions[2]}'

# print(choose_plural(2, ('пример', 'примера', 'примеров')))  # 2 примера
# print(choose_plural(21, ('пример', 'примера', 'примеров')))  # 21 пример
# print(choose_plural(111, ('пример', 'примера', 'примеров')))  # 111 примеров


# 11
"""
Функция get_biggest()
Реализуйте функцию get_biggest(), которая принимает один аргумент:
numbers — список целых неотрицательных чисел
Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers. 
Если список numbers пуст, функция должна вернуть число −1.

Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3], из которых можно составить следующие числа:
123, 132, 213, 231, 312, 321
Наибольшим из представленных является  321.

[1, 2, 3, 4] -> 1234, 1243, 1324, 1342
"""
from functools import cmp_to_key
# cmp_to_key - превращает функцию сравнения в key-функцию

def compare_numbers(a: str, b: str) -> int:
    # Функция сравнения для сортировки чисел посимвольно
    return int(b + a) - int(a + b)


def get_biggest(numbers: list) -> int:
    if numbers:
        num_lst = list(map(str, numbers))
        num_lst.sort(key=cmp_to_key(compare_numbers))
        return int(''.join(num_lst))
    return -1

print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))
print(get_biggest([]))
print(get_biggest([0, 0, 0]))


# Вариант
def get_biggest(numbers):
    if numbers:
        num_lst = list(map(str, numbers))
        sort_lst = sorted(num_lst, key=lambda x: x * len(max(num_lst)), reverse=True)
        return int(''.join(sort_lst))
    return -1
