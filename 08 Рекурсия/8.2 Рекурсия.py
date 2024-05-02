#  8.2 Рекурсия
""""""


"""   *   *   *   Task   *   *   *   """


#  8.2-1
"""
Подозрительно просто
"""
# def traffic(n):
#     while n > 0:
#         print('Не парковаться')
#         n -= 1

def traffic(n):
    if n > 0:
        traffic(n - 1)
        print('Не парковаться')

# traffic(3)


#  8.2-2
"""
вывести последовательность натуральных чисел от 1 до 100 включительно, 
каждое на отдельной строке.
"""
def one_hundred(n=100):
    if n > 0:
        one_hundred(n - 1)
        print(n)


def one_hundred(n=1):
    if n <= 100:
        print(n)
        one_hundred(n + 1)

one_hundred()



#  8.2-3
"""
доступен список numbers, содержащий ровно 100 целых чисел. 
Дополните приведенный ниже код с использованием рекурсии, 
чтобы он вывел все элементы этого списка от первого до последнего, 
каждый на отдельный строке, в следующем формате:

Элемент <индекс элемента>: <значение элемента>

Output:
Элемент 0: 243
Элемент 1: -279
Элемент 2: 395
...
"""
numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341,
           437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331,
           323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127,
           984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777,
           805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]


def one_hundred(n=0):
    if n < 100:
        print(f'Элемент {n}: {numbers[n]}')
        one_hundred(n + 1)

one_hundred()


#  8.2-4
"""
Обратный порядок
https://stepik.org/lesson/637962/step/8?thread=solutions&unit=634429
Дана последовательность целых чисел. Вывести эту последовательность в обратном порядке (начиная от нуля).

"""
import sys
ls = list(map(int, sys.stdin))

def get_list(ls: list):
    idx = ls.index(0)
    def get_reverse(n):
        if n >= 0:
            print(ls[n])
            get_reverse(n - 1)
    get_reverse(idx)

get_list(ls)


# Без обработки лишнего ввода
def get_reverse(num: str):
    if num != '0':
        get_reverse(input())
    print(num)

get_reverse(input())


#  8.2-5
"""
Функция triangle()
Функция должна выводить звездный треугольник с высотой h в соответствии:
...
***
**
*
"""
def triangle(n):
    if n > 0:
        print('*' * n)
        triangle(n - 1)

# triangle(3)


#  8.2-6
"""
Функция triangle()
Функция должна выводить звездный треугольник с высотой h в соответствии:
*
**
***
...
"""
def triangle(n):
    if n > 0:
        triangle(n - 1)
        print('*' * n)

# triangle(3)


#  8.2-7
"""
Песочные часы
https://stepik.org/lesson/637962/step/11?unit=634429

1111111111111111    # 16 раз
  222222222222      # 12 раз
    33333333        # 8 раз
      4444          # 4 раза
    33333333        # 8 раз
  222222222222      # 12 раз
1111111111111111    # 16 раз
"""
def hourglass(n=1, repeat=16):
    print((str(n) * repeat).center(16))
    if n < 4:
        hourglass(n + 1, repeat - 4)
    if n < 4:
        print((str(n) * repeat).center(16))


# Вариант
def hourglass(n=1, repeat=16):
    print(' ' * (n - 1) * 2 + str(n) * repeat)
    if n < 4:
        hourglass(n + 1, repeat - 4)
    if n < 4:
        print(' ' * (n - 1) * 2 + str(n) * repeat)

hourglass()


#  8.2-8
"""
Функция print_digits()
https://stepik.org/lesson/637962/step/12?unit=634429

Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:
number — натуральное число
Функция должна выводить все цифры числа number, 
начиная с младших разрядов, каждое на отдельной строке.

Input:  print_digits(12345)
Output: 5
        4
        3
        2
        1
"""
def print_digits(number):
    if number > 0:
        print(number % 10)
        print_digits(number // 10)

# print_digits(12345)


#  8.2-9
"""
Функция print_digits()
Функция должна выводить все цифры числа number, 
начиная со старших разрядов, каждое на отдельной строке.
Input:  print_digits(12345)
Output: 1
        2
        3
        4
        5
"""
def print_digits(number):
    if number:
        print_digits(number // 10)
        print(number % 10)

# print_digits(12345)

