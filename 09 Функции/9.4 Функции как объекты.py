# 9.4 Функции как объекты
""""""
# https://stepik.org/lesson/647292/step/1?unit=643926
# https://stepik.org/lesson/647292/step/13?unit=643926


"""   *   *   *   Task   *   *   *   """

#  9.4-1
"""
Реализуйте функцию numbers_sum(), которая принимает один аргумент:
elems — список произвольных объектов
Функция должна возвращать сумму чисел (типы int и float), 
находящихся в списке elems, игнорируя все нечисловые объекты. 
Если в списке elems нет чисел, функция должна вернуть число 0.
Также функция должна иметь строку документации.
"""
def numbers_sum(elems):
    '''
    Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    '''
    res = 0
    if isinstance(elems, list):
        for el in elems:
            if type(el) in (int, float):
                res += el
    return res


#  9.4-2
"""
Напишите программу, которая переопределяет встроенную функцию print() так, 
чтобы она печатала все переданные строковые аргументы в верхнем регистре.
Значения sep и end также должны переводиться в верхний регистр.
"""
# Через начальную замену имени print()
origin_print = print

def print(*args, sep=' ', end='\n'):
    # args = (str(el).upper() for el in args)
    args = (el.upper() if isinstance(el, str) else el for el in args)
    origin_print(*args, sep=sep.upper(), end=end.upper())


# Сразу переписываем функцию print()
import sys

def print(*args, sep=' ', end='\n'):
    words = map(lambda x: x.upper() if type(x) == str else x, args)
    new_str = list(map(str, words))
    sys.stdout.write(f'{sep.upper().join(new_str)}{end.upper()}')


print('bee', 'geek', 'any', sep=' & ')  # BEE & GEEK & ANY
print('bee', 'geek', 'any', end=' окончание\n')  # BEE GEEK ANY ОКОНЧАНИЕ



#  9.4-3
"""
Реализуйте функцию polynom(), которая принимает один аргумент:
x — вещественное число
Функция должна возвращать значение выражения 𝑥^2 + 1
Также функция должна иметь атрибут values, 
представляющий собой множество (тип set) всех значений функции, которые уже были вычислены.
"""
def polynom(x):
    res = int(x)**2 + 1
    polynom.__dict__.setdefault('values', set())
    polynom.values.add(res)
    return res


# Вариант
def polynom(x):
    res = int(x)**2 + 1
    if 'values' not in polynom.__dict__:
        polynom.__dict__['values'] = set()
    polynom.__dict__['values'].update({res})
    return res

polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))  # 2 5 10


#  9.4-4
"""
Функция remove_marks()
Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:
text — произвольная строка
marks — набор символов
Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в строке marks.
Также функция remove_marks() должна иметь атрибут count, представляющий собой количество вызовов данной функции.
"""
def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1
    # remove_marks.__dict__['count'] += 1

    for el in marks:
        text = text.replace(el, '')
    return text


# Короче
def remove_marks(text, marks):
    remove_marks.__dict__['count'] = remove_marks.__dict__.get('count', 0) + 1

    for el in marks:
        text = text.replace(el, '')
    return text


text = 'Hi! By?'
print(remove_marks(text, '!?'))  # Hi By
print(remove_marks.count)  # 1

