# 7.1 Обработка исключений
""""""


"""   *   *   *   Task   *   *   *   """


#  7.1-1
"""
Найдите и исправьте все ошибки, допущенные в этой программе (их ровно 3).
"""
# total = 0
#
# with open(data.txt, encoding='utf-8') as file:
#     for _ in file.readlines:
#         total == total + 1
#
# print(total)

total = 0

with open('data.txt', encoding='utf-8') as file:
    for _ in file.readlines():
        total += 1

print(total)


#  6.11-1
"""
Найдите и исправьте все ошибки, допущенные в этой программе (их ровно 3)
"""
# def swapcase_vowels(string):
#     vowels = 'aeiouy'
#     swapped_string = ''
#
#     for char in string:
#         if char == vowels:
#             char.upper()
#         swapped_string += char
#
#     return print(swapped_string)

def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''

    for char in string:
        if char.lower() in vowels:
            swapped_string += char.upper()
        else:
            swapped_string += char
    return swapped_string


#  7.1-3
"""
Вывести список всех целых чисел от a до b включительно, которые делятся на 7 без остатка
Найдите и исправьте все ошибки, допущенные в этой программе (их ровно 5)
"""
# a = input()
# b = input()
# numbers = []
#
# for i in range(a, b):
#     if i // 7 == 0:
#         numbers = numbers.append(i)
#
# print(numbers)

a = int(input())
b = int(input())
numbers = []

for i in range(a, b + 1):
    if i % 7 == 0:
        numbers.append(i)

print(numbers)


#  7.1-4
"""
реализовать функцию get_max_index(), 
которая принимает в качестве аргумента список различных целых чисел 
и возвращает индекс наибольшего числа из этого списка (начиная с 0)
Найдите и исправьте все ошибки, допущенные в этой программе (их ровно 4)
"""
# def get_max_index(numbers):
#     max_index = 0
#     max_value = numbers[-1]
#
#     for index, value in enumerate(numbers, 1):
#         if index > max_index:
#             max_index = index
#             max_value = value
#
#     return max_value

def get_max_index(numbers: list):
    max_index = 0
    max_value = numbers[0]

    for index, value in enumerate(numbers):
        if value > max_value:
            max_index = index
            max_value = value

    return max_index

