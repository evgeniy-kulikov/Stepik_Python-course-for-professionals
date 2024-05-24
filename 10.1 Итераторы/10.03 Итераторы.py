#  10.3 Итераторы. Часть 3
""""""


"""   *   *   *   Task   *   *   *   """


#  10.3-1
"""
Дополните приведенный ниже код, чтобы в переменной infinite_love содержался итератор, 
бесконечно генерирующий единственное значение — строку i love beegeek!
"""
infinite_love = iter(lambda: 'i love beegeek!', 1)

print(next(infinite_love))


#  10.3-2
"""
Реализуйте функцию is_iterable(), которая принимает один аргумент:
obj — произвольный объект
Функция должна возвращать True, если объект obj является итерируемым объектом, 
или False в противном случае.
"""
def is_iterable(obj):
    return '__iter__' in dir(obj)


print(is_iterable(18731))  # False
print(is_iterable('18731'))  # True


#  10.3-3
"""
Реализуйте функцию is_iterator(), которая принимает один аргумент:
obj — произвольный объект
Функция должна возвращать True, если объект obj является итератором, или False в противном случае. 
"""
def is_iterator(obj):
    return '__next__' in dir(obj)


print(is_iterator([1, 2, 3, 4, 5]))  # False

beegeek = map(str.upper, 'beegeek')
print(is_iterator(beegeek))  # True


#  10.3-4
"""
Реализуйте функцию random_numbers(), которая принимает два аргумента:
left — целое число
right — целое число
Функция должна возвращать итератор, 
генерирующий бесконечную последовательность случайных целых чисел в диапазоне от left до right включительно.
Гарантируется, что left <= right.
"""
from random import randint

def random_numbers(left, right):
    return iter(lambda: randint(left, right), None)

# Короче
# random_numbers = lambda left, right: iter(lambda: randint(left, right), None)

iterator = random_numbers(1, 1)
print(next(iterator))  # 1
print(next(iterator))  # 1
