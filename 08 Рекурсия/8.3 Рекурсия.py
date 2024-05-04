# 8.3 Рекурсия
""""""

#  рекурсивный алгоритм вычисления факториала
# Базовый случай не требует рекурсии, и поэтому он останавливает цепочку рекурсивных вызовов.
def factorial(n):
    if n == 0:
        return 1                    # базовый случай
    else:
        return n * factorial(n-1)   # рекурсивный случай


#  сумма чисел от 0 до n включительно
def sum_to(n):
    if n == 0:
        return 0                   # базовый случай
    else:
        return n + sum_to(n - 1)   # рекурсивный случай


# возвратить сумму элементов списка nums
def recursive_sum(nums):
    if not nums:
        return 0                                   # базовый случай
    return nums[0] + recursive_sum(nums[1:])       # рекурсивный случай


"""   *   *   *   Task   *   *   *   """


#  8.3-1
"""
Определить количество цифр в введенном числе
Input:  17488
Output: 5
"""
def get_bit(num: int):
    if num // 10 == 0:  # num < 10
        return 1
    else:
        return get_bit(num // 10) + 1

print(get_bit(int(input())))


# Вариант
get_bit = lambda x: 1 if x < 10 else get_bit(x // 10) + 1
print(get_bit(int(input())))


#  8.3-2
"""
Определить сумму цифр введенного числа 
Input:  25
Output: 7
"""
def get_sum(num: int):
    if num < 10:
        return num
    return get_sum(num // 10) + num % 10

print(get_sum(int(input())))


# Вариант
get_sum = lambda x: x if x < 10 else get_sum(x // 10) + x % 10
print(get_sum(int(input())))


#  8.3-3
"""
number_of_frogs()
https://stepik.org/lesson/594137/step/8?unit=589173
В первый год в пруду живет 77 лягушек. Каждый год из пруда вылавливают 30 лягушек, 
а оставшиеся размножаются, и их становится в три раза больше.
F (k) = 3(F (k−1) − 30)
Input:  print(number_of_frogs(2))
Output: 141
"""
def number_of_frogs(num: int):
    if num == 1:
        return 77
    return 3 * (number_of_frogs(num - 1) - 30)


# Вариант
number_of_frogs = lambda n: 77 if n == 1 else 3 * (number_of_frogs(n - 1) - 30)
# print(number_of_frogs(3))


#  8.3-4
"""
range_sum()
https://stepik.org/lesson/594137/step/9?unit=589173
Реализуйте функцию range_sum() с использованием рекурсии, 
которая принимает три аргумента в следующем порядке:
numbers — список целых чисел
start — целое неотрицательное число
end — целое неотрицательное число
Функция должна суммировать все числа из списка numbers от numbers[start] до numbers[end] включительно 
и возвращать полученный результат.
Input:  print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
Output: 30
"""
def range_sum(numbers: list, start, end):
    if start == end + 1:
        return 0
    return numbers[start] + range_sum(numbers, start + 1, end)

# Вариант
def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    return numbers[start] + range_sum(numbers, start + 1, end)

# Вариант
range_sum = lambda n, s, e: n[s] if s == e else n[s] + range_sum(n, s + 1, e)
# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))


#  8.3-5
"""
Обычное возведение в степень
https://stepik.org/lesson/594137/step/10?unit=589173
Реализуйте функцию get_pow() с использованием рекурсии, которая принимает два аргумента в следующем порядке:
a — положительное целое число
n — неотрицательное целое число
Функция должна вычислять значение a в степени n и возвращать полученный результат.
Для построения рекурсивного алгоритма воспользуйтесь следующим рекуррентным соотношением:
a ^n = a * a ^(n−1)
Input:  print(get_pow(5, 2))
Output: 25
"""
def get_pow(a, n):
    if n == 0:
        return 1
    return a * get_pow(a, n - 1)

# Вариант
get_pow = lambda a, n: 1 if n == 0 else a * get_pow(a, n - 1)
# print(get_pow(5, 2))



#  8.3-6
"""
Быстрое возведение в степень
https://stepik.org/lesson/594137/step/10?unit=589173
Реализуйте функцию get_fast_pow() с использованием рекурсии, которая принимает два аргумента в следующем порядке:
a — положительное целое число
n — неотрицательное целое число
Функция должна вычислять значение a в степени n и возвращать полученный результат.
Для построения рекурсивного алгоритма воспользуйтесь следующим рекуррентным соотношением:
a ^n = (a * a) ^(n / 2)     - при  четном  n
a ^n = a * a ^(n−1)         - при  нечетном  n
Input:  print(get_pow(5, 2))
Output: 25
"""
def get_fast_pow(num, pow):
    if pow == 0:
        return 1
    elif pow % 2:
        return num * get_fast_pow(num, pow - 1)
    return get_fast_pow(num * num, pow // 2)


# Вариант
def get_fast_pow(num, pow):
    if pow == 0:
        return 1
    return num * get_fast_pow(num, pow - 1) if pow % 2 else get_fast_pow(num * num, pow // 2)

# print(get_fast_pow(5, 2))


#  8.3-7
"""
Реализуйте функцию recursive_sum() с использованием рекурсии, которая принимает два аргумента в следующем порядке:
a — неотрицательное целое число
b — неотрицательное целое число
Функция должна возвращать сумму чисел a и b

При вычислении суммы функция:
не должна использовать циклы
из всех арифметических операций должна использовать только +1 и −1

Input:  print(recursive_sum(10, 22))
Output: 32
"""
def recursive_sum(a, b):
    if b == 0:
        return a
    return 1 + recursive_sum(a, b - 1)

# print(recursive_sum(10, 22))


#  8.3-8
"""
Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:
number — натуральное число
Функция должна возвращать значение True, если number является степенью числа 2, 
или False в противном случае.

Input:  print(is_power(512))
Output: True
"""
def is_power(number):
    if number <= 2:
        return True
    elif number % 2:  # отсекаем нечетные числа
        return False
    return is_power(number // 2)


# Через внутреннюю функцию
def is_power(num):
    if num == 1:
        return True

    def inner(n):
        if n < 2:
            return n
        return inner(n / 2)

    return inner(num) == 1

# Короче
def is_power(n):
    if n > 1:
        return is_power(n / 2)
    else:
        return n == 1

# print(is_power(32))


#  8.3-9
"""
Функция tribonacci()
Реализуйте функцию tribonacci() с использованием рекурсии и мемоизации, которая принимает один аргумент:
n — натуральное число
Функция должна возвращать n-й член последовательности Трибоначчи.

Последовательность Трибоначчи – 
последовательность натуральных чисел, где каждое последующее число является суммой трех предыдущих:
1, 1, 1, 3, 5, 9, 17, 31, 57, 105 …

Input:  print(tribonacci(7))
Output: 17
"""
def tribonacci(num):
    cache = {1: 1, 2: 1, 3: 1}

    def trib(n):
        if n not in cache:
            cache[n] = trib(n - 1) + trib(n - 2) + trib(n - 3)
        return cache[n]

    return trib(num)


# Вариант
def tribonacci(num):
    cache = {1: 1, 2: 1, 3: 1}

    def trib(n):
        if n in cache:
            return cache[n]
        res = trib(n - 1) + trib(n - 2) + trib(n - 3)
        cache[n] = res
        return res

    return trib(num)

# print(tribonacci(10))   # 105
# print(tribonacci(100))  # 69087442470169316923566147


#  8.3-10
"""
Реализуйте функцию is_palindrome() с использованием рекурсии, которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать значение True, если переданная строка является палиндромом, 
или False в противном случае.

Input:  print(is_palindrome('level'))
Output: True
"""
def is_palindrome(word: str):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])


#  8.3-11
"""
Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:
number — неотрицательное целое число
Функция должна возвращать строковое представление числа number в двоичной системе счисления.

Input:  print(to_binary(15))
Output: 1111
"""
def to_binary(num):
    if num <= 1:
        return str(num)
    return to_binary(num // 2) + str(num % 2)


#  8.3-12
"""
Без циклов
https://stepik.org/lesson/594137/step/17?unit=589173
Напишите программу с использованием рекурсии, которая принимает на вход число 𝑛
и вычитает из него число 5, пока оно не перестанет быть положительным, 
а затем прибавляет к нему число 5, пока оно снова не станет равным 𝑛

Input:  10
Output: 10
        5
        0
        5
        10
"""
def get_five(num):
    if num > 0:
        print(num)
        get_five(num - 5)
    print(num)

get_five(int(input()))
