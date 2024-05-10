# 9.5 Вложенные функции, замыкания
""""""
# https://stepik.org/lesson/651459/step/1?unit=648165


"""   *   *   *   Task   *   *   *   """


#  9.5-1
"""
Реализуйте функцию power(), которая принимает один аргумент:
degree — целое число
Функция power() должна возвращать функцию, которая принимает в качестве аргумента целое число x 
и возвращает значение x в степени degree
"""
def power(degree):
    def inner(x):
        return x ** degree
    return inner

square = power(2)
print(square(5))  # 25

print(power(3)(3))  # 27

result = power(4)(2)
print(result)  # 16


#  9.5-2
"""
Функция generator_square_polynom()
семейство функций — квадратных трехчленов:
f(x) = 𝑎𝑥^2 + 𝑏𝑥 + 𝑐

Реализуйте функцию generator_square_polynom(), которая принимает три аргумента в следующем порядке:
a — вещественное число, коэффициент 
b — вещественное число, коэффициент 
c — вещественное число, коэффициент 

Функция generator_square_polynom() должна возвращать функцию, 
которая принимает в качестве аргумента вещественное число x 
и возвращает значение выражения 𝑎𝑥^2 + 𝑏𝑥 + 𝑐
"""
def generator_square_polynom(a, b, c):
    def inner(x):
        return a * x**2 + b * x + c
    return inner

f = generator_square_polynom(1, 2, 1)
print(f(5))  # 36

print(generator_square_polynom(9, 52, 64)(8))  # 1056


#  9.5-3
"""
Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения:
https://beegeek.ru?name=timur&color=green
Реализуйте функцию sourcetemplate(), которая принимает один аргумент:
url — URL адрес
Функция sourcetemplate() должна возвращать функцию, 
которая принимает произвольное количество именованных аргументов и возвращает url адрес, 
объединенный со строкой запроса, сформированной из переданных аргументов. 
При вызове без аргументов она должна возвращать исходный url адрес без изменений.
Параметры в строке запроса должны располагаться в лексикографическом порядке ключей.
"""
def sourcetemplate(url):
    def inner(**kwargs):
        if kwargs:
            res = [f'{k}={v}' for k, v in sorted(kwargs.items())]
            return f"{url}?{'&'.join(res)}"
        return url
    return inner


url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))
# https://stepik.org/lesson/651459/step/14?thread=solutions&unit=648165

url = 'https://beegeek.ru';
load = sourcetemplate(url)
print(load())  # https://beegeek.ru


#  9.5-4
"""
Функция date_formatter()
https://stepik.org/lesson/651459/step/19?unit=648165

Реализуйте функцию date_formatter(), которая принимает один аргумент:
country_code — код страны
Функция date_formatter() должна возвращать функцию, 
которая принимает в качестве аргумента дату (тип date) 
и возвращает строку с данной датой в формате страны с кодом country_code.
"""
from datetime import date

def date_formatter(code: str):
    dt = {'ru': '%d.%m.%Y',
          'us': '%m-%d-%Y',
          'ca': '%Y-%m-%d',
          'br': '%d/%m/%Y',
          'fr': '%d.%m.%Y',
          'pt': '%d-%m-%Y'}

    def inner(data: date):
        return data.strftime(dt[code])

    return inner


date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))  # 25.01.2022


#  9.5-5
"""
Функция sort_priority() 🌶️
https://stepik.org/lesson/651459/step/20?unit=648165
Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:
values — список чисел
group — список, кортеж или множество чисел
Функция должна сортировать по неубыванию список чисел values, 
делая при этом приоритетной группу чисел из group, которая должна следовать первой.
"""
# Хорошее решение
# Сортировка с использованием двух массивов данных
def sort_priority(values, group):
    values.sort(key=lambda el: (el not in group, el))

# Обычное решение
def sort_priority(values: list, group):
    head = sorted(el for el in group if el in values)
    tail = sorted(set(values) - set(head))
    values.clear()
    values.extend(head + tail)


numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])
print(numbers)  # [200, 300, 50, 150, 1000, 20000]

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)
print(numbers)   # [2, 3, 5, 7, 1, 4, 6, 8]

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
