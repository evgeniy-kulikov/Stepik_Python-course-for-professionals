# 7.4 Обработка исключений
""""""

"""
Тип Exception – базовый класс для большинства встроенных в Python исключений. 
Именно его, а не BaseException, необходимо наследовать при создании пользовательского класса исключения.
"""

try:
    nums = [10, 5, 20, 25]
    print(nums[100])
except (KeyError, IndexError) as err:    # записываем сгенерированное исключение в переменную err
    print(err)  # list index out of range


"""   *   *   *   Task   *   *   *   """


#  7.4-1
"""
Реализуйте функцию get_weekday(), которая принимает один аргумент:

number — целое число (от 1 до 7 включительно)
Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:

если number не является целым числом, функция должна возбуждать исключение: 
TypeError('Аргумент не является целым числом')
если number является целым числом, но не принадлежит отрезку [1;7], 
функция должна возбуждать исключение: 
ValueError('Аргумент не принадлежит требуемому диапазону')
"""
import locale
from calendar import day_name

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def get_weekday(number):
    if not type(number) == int:
        raise TypeError('Аргумент не является целым числом')
    if number < 1 or number > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return day_name[number - 1]


#  7.4-2
"""
Реализуйте функцию get_id(), которая принимает два аргумента:
names — список имен учеников, обучающихся в школе
name — имя поступающего ученика

Функция должна возвращать идентификационный номер, который получит поступающий в школу ученик, 
при этом если имя ученика name не является строкой (тип str), 
функция должна возбуждать исключение:
TypeError('Имя не является строкой')
если имя ученика name является строкой (тип str), но не представляет собой корректное имя, 
функция должна возбуждать исключение:
ValueError('Имя не является корректным')
"""

def get_id(names: list, name: str):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    if not all([name.isascii(), name.istitle(), name.isalpha()]):
        raise ValueError('Имя не является корректным')
    return len(names) + 1

# names = ['Timur', 'Anri', 'Dima', 'Arthur']
# name = 'Ruэфы'

# try:
#     print(get_id(names, name))
# except ValueError as e:
#     print(e)


#  7.4-3
"""
Напишите программу, которая принимает на вход название JSON файла, 
десериализует содержащийся в этом файле объект и выводит его.

если файла с данным названием нет в папке с программой, программа должна вывести текст:
Файл не найден
если файл с данным названием содержит некорректные данные (то есть не удовлетворяющие формату JSON), 
программа должна вывести текст:
Ошибка при десериализации
"""
import json

try:
    with open(input(), encoding='u8') as file:
        print(json.load(file))
except FileNotFoundError:
    print('Файл не найден')
except json.decoder.JSONDecodeError:
    print('Ошибка при десериализации')


# Вариант
try:
    with open(input(), encoding='utf-8') as file:
        try:
            data = json.load(file)
            print(data)
        except json.JSONDecodeError:
            print("Ошибка при десериализации")
except FileNotFoundError:
    print("Файл не найден")
