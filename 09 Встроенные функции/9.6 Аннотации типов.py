# 9.6 Аннотации типов
""""""


"""   *   *   *   Task   *   *   *   """


#  9.6-1
"""
Реализуйте функцию get_digits() c использованием аннотаций типов, которая принимает один аргумент:
number — положительное целое или вещественное число
Функция должна возвращать список, состоящий из цифр числа number.

Примечание 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing. 
Также используйте нотацию |, а не тип Union из модуля typing.
Примечание 2. Порядок следования цифр в списке должен совпадать с порядком следования их в исходном числе.
"""
def get_digits(number: int | float) -> list[int]:
    # return [int(el) for el in str(number).replace('.', '')]
    return list(int(el) for el in str(number) if el.isdigit())


print(get_digits(13.909934))  # [1, 3, 9, 0, 9, 9, 3, 4]

annotations = get_digits.__annotations__
print(annotations['return'])  # list[int]


#  9.6-2
"""
Реализуйте функцию top_grade() c использованием аннотаций типов, которая принимает один аргумент:
grades — словарь, содержащий данные об ученике, 
а именно имя по ключу name и список оценок по ключу grades.

Функция должна возвращать словарь, содержащий имя ученика по ключу name 
и его самую высокую оценку по ключу top_grade.
"""
def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}


print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))
# {'name': 'Ruslan', 'top_grade': 86}

annotations = top_grade.__annotations__
print(annotations['grades'])
# dict[str, str | list[int]]

print(*top_grade.__annotations__.values())
# dict[str, str | list[int]] dict[str, str | int]


#  9.6-3
"""
Реализуйте функцию cyclic_shift() с использованием аннотаций типов, 
которая принимает два аргумента в следующем порядке:
numbers — список целых или вещественных чисел
step — целое число
Функция должна изменять переданный список, 
циклически сдвигая элементы списка на step шагов, и возвращать значение None. 
Если step является положительным числом, сдвиг происходит вправо, если отрицательным — влево.
"""
def cyclic_shift(numbers: list[int | float], step: int) -> None:
    if step and len(numbers) > 1:
        numbers[:] = [numbers[(el - step) % len(numbers)] for el in range(len(numbers))]

def cyclic_shift(numbers: list[int | float], step: int) -> None:
    for _ in range(abs(step)):
        if step > 0:
            numbers.insert(0, numbers.pop(-1))
        else:
            numbers.append(numbers.pop(0))


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)
print(numbers)  # [3, 4, 5, 1, 2]

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
print(numbers)  # [5, 1, 2, 3, 4]


#  9.6-4
"""
Реализуйте функцию matrix_to_dict() с использованием аннотаций типов, которая принимает один аргумент:
matrix — матрица произвольной размерности, элементами которой являются целые или вещественные числа.
Функция должна возвращать словарь, 
ключом в котором является номер строки матрицы, а значением — список элементов этой строки.
Примечание:
 1. Используйте встроенные типы (list, tuple, ...), а не типы из модуля typing. 
    Также используйте нотацию |, а не тип Union из модуля typing.
 2. Под матрицей подразумеваются исключительно вложенные списки.
 3. Нумерация строк матрицы в возвращаемом функцией словаре должна начинаться с единицы.
 4. Элементы матрицы в списке должны располагаться в своем исходном порядке.
"""
def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {k: v for k, v in enumerate(matrix, 1)}
    # return {k: v for k, v in zip(range(1, len(matrix) + 1), map(list, matrix))}


matrix = [[5.1, 6, 7.94]]
print(matrix_to_dict(matrix))
# {1: [5.1, 6, 7.94]}

matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
print(matrix_to_dict(matrix))
# {1: [5, 6, 7], 2: [8, 3, 2], 3: [4, 9, 8]}

annotations = matrix_to_dict.__annotations__
print(annotations['return'])
# dict[int, list[int | float]]

print(*matrix_to_dict.__annotations__.values())
# list[list[int | float]] dict[int, list[int | float]]
