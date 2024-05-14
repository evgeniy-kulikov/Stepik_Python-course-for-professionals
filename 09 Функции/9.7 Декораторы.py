# 9.7 Декораторы
""""""

def say():                      # функция
    print('Привет Мир!')

def null_decorator(func):       # определяем декоратор
    return func

say = null_decorator(say)      # декорируем функцию

say()                          # вызов декорируемой функции


# Вариант реализации
def make_decor(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper

@make_decor
def say():
    print('Привет Мир!')


"""   *   *   *   Task   *   *   *   """


#  9.7-1
"""
Реализуйте декоратор sandwich, который выводит тексты:
---- Верхний ломтик хлеба ----
---- Нижний ломтик хлеба ----
до и после вызова декорируемой функции соответственно.
"""
def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        res = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return res
    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))

add_ingredients(['томат', 'салат', 'сыр', 'бекон'])

@sandwich
def beegeek():
    return 'beegeek'

print(beegeek())


#  9.7-2
"""
Напишите программу с использованием декоратора, которая переопределяет функцию print() так, 
чтобы она печатала весь текст в верхнем регистре.
"""
def print_upper(func):
    def wrapper(*args, **kwargs):
        args = map(str, map(lambda x: x.upper() if isinstance(x, str) else x, args))
        kwargs = {k: v.upper() if isinstance(v, str) else v
                  for k, v in kwargs.items()}
        func(*args, **kwargs)
    return wrapper

print = print_upper(print)

print('are', 'you', 'in', 'trouble')
# ARE YOU IN TROUBLE

print('are', 'you', 'in', 'trouble', sep='x', end='finish')
# AREXYOUXINXTROUBLEFINISH


#  9.7-3
"""
Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.
"""
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        res = func(*args, **kwargs)
        return res
    return wrapper

@do_twice
def beegeek():
    print('beegeek')

beegeek()
# beegeek
# beegeek


@do_twice
def beegeek():
    print('beegeek')

print(beegeek())
# beegeek
# beegeek
# None


#  9.7-4
"""
Реализуйте декоратор reverse_args, 
который передает все позиционные аргументы в декорируемую функцию func в обратном порядке.
"""
def reverse_args(func):
    def wrapper(*args, **kwargs):
        inverse = reversed(args)
        res = func(*inverse, **kwargs)
        return res
    return wrapper


@reverse_args
def concat(a, b, c):
    return a + b + c

print(concat('apple', 'cherry', 'melon'))
# meloncherryapple


#  9.7-5
"""
Реализуйте декоратор exception_decorator, который возвращает
* кортеж (value, 'Функция выполнилась без ошибок'), 
  если декорируемая функция завершила свою работу без ошибок, 
  где value — возвращаемое значение декорируемой функции
* кортеж (None, 'При вызове функции произошла ошибка'), 
  если при выполнении декорируемой функции возникла ошибка
"""
def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), 'Функция выполнилась без ошибок'
        except:
            return None, 'При вызове функции произошла ошибка'
    return wrapper


@exception_decorator
def f(x):
    return x ** 2 + 2 * x + 1

print(f(7))
# (64, 'Функция выполнилась без ошибок')

sum = exception_decorator(sum)
print(sum(['199', '1', 187]))
# (None, 'При вызове функции произошла ошибка')


#  9.7-6
"""
Реализуйте декоратор takes_positive, который проверяет, 
что все аргументы, передаваемые в декорируемую функцию, являются положительными целыми числами.
Если хотя бы один аргумент не удовлетворяет данному условию, 
декоратор должен возбуждать исключение:
TypeError, если аргумент не является целым числом
ValueError, если аргумент является целым числом, но отрицательным или равным нулю
"""
def takes_positive(func):
    def wrapper(*args, **kwargs):
        num = {*args, *kwargs.values()}
        if not all(type(x) == int for x in num):
            raise TypeError
        if not all(x > 0 for x in num):
            raise ValueError
        return func(*args, **kwargs)
    return wrapper




@takes_positive
def positive_sum(*args):
    return sum(args)

print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# 55


@takes_positive
def positive_sum(*args):
    return sum(args)

try:
    print(positive_sum(10, 20, 16, 18, '10'))
except Exception as err:
    print(type(err))
# <class 'TypeError'>


@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))
# 60
