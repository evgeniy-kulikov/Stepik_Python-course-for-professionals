# 9.8 Декораторы
""""""

import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Что-то выполняется до вызова декорируемой функции
        value = func(*args, **kwargs)
        # декорируется возвращаемое значение функции
        # или что-то выполняется после вызова декорируемой функции
        return value
    return wrapper



import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper



"""   *   *   *   Task   *   *   *   """


#  9.8-1
"""
Реализуйте декоратор square, который возводит возвращаемое значение декорируемой функции во вторую степень. 
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Гарантируется, что возвращаемым значением декорируемой функции является объект типа int или float.
"""
import functools

def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper


@square
def add(a, b):
    '''прекрасная функция'''
    return a + b

print(add(1, 1))
print(add.__name__)
print(add.__doc__)
# 4
# add
# прекрасная функция


#  9.8-2
"""
Декоратор returns_string
Реализуйте декоратор returns_string, который проверяет, 
что возвращаемое значение декорируемой функции принадлежит типу str. 
Если возвращаемое значение принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""
import functools

def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if not isinstance(res, str):
            raise TypeError
        return res
    return wrapper


@returns_string
def add(a, b):
    return a + b

try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))
# <class 'TypeError'>


#  9.8-3
"""
Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время ее выполнения, 
а именно: имя функции, переданные аргументы и возвращаемое значение в следующем формате:
TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""
import functools

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}\n"
              f"TRACE: возвращаемое значение {func.__name__}(): {repr(res)}")

        return res
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'

say('Jane', 'Hello, World')
# TRACE: вызов say() с аргументами: ('Jane', 'Hello, World'), {}
# TRACE: возвращаемое значение say(): 'Jane: Hello, World'

@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c


print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)
# sub
# прекрасная функция
# TRACE: вызов sub() с аргументами: (20, 5), {'c': 10}
# TRACE: возвращаемое значение sub(): 25


#  9.8-4
"""
Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:
- string — произвольная строка
- to_the_end — булево значение, по умолчанию равное False
Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции. 
Если to_the_end имеет значение True, строка string добавляется в конец, если False — в начало.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Гарантируется, что возвращаемым значением декорируемой функции является объект типа str
"""
import functools

def prefix(string: str, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if to_the_end:
                return res + string
            return string + res
        return wrapper
    return decorator


@prefix('online-school ')
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


print(beegeek.__name__)  # beegeek
print(beegeek.__doc__)   # beegeek docs
print(beegeek())        # online-school beegeek


#  9.8-5
"""
Реализуйте декоратор make_html(), который принимает один аргумент:
tag — HTML-тег, например, del
Декоратор должен обрамлять возвращаемое значение декорируемой функции в HTML-тег tag.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Гарантируется, что возвращаемым значением декорируемой функции является объект типа str
"""
import functools

def make_html(tag: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return f'<{tag}>{res}</{tag}>'
        return wrapper
    return decorator


@make_html('del')
def get_text(text):
    return text

print(get_text('Python'))  # <del>Python</del>


#  9.8-6
"""
Реализуйте декоратор repeat, который принимает один аргумент:
times — натуральное число
Декоратор должен вызывать декорируемую функцию times раз.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""
import functools

def repeat(repeat=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(repeat):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator


@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')

say_beegeek()
# beegeek
# beegeek
# beegeek


@repeat(10)
def add(a, b):
    '''sum of two numbers'''
    return a + b
print(add(10, b=20))  # 30


#  9.8-7
"""
Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:
- start — неотрицательное целое число
- end — неотрицательное целое число
- char — одиночный символ, по умолчанию равный точке .
Декоратор должен изменять возвращаемое значение декорируемой функции, 
заменяя все символы в диапазоне индексов от start (включительно) до end (не включительно) на символ char.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
2. Гарантируется, что start < end.
"""
import functools

def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res[:start] + char * len(res[start:end]) + res[end:]

            # if len(res) - start >= end - start:
            #     return res[:start] + char * (end - start) + res[end:]
            # return res[:start] + char * (len(res) - start)

            # return res[:start] + char * min([(end - start), len(res) - start]) + res[end:]

        return wrapper
    return decorator


@strip_range(3, 7)
def beegeek():
    return 'beegeek'
print(beegeek())  # bee..ek


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'
print(beegeek())  # bee____


#  9.8-8
"""
Реализуйте декоратор returns, который принимает один аргумент:
datatype — тип данных
Декоратор должен проверять, что возвращаемое значение декорируемой функции принадлежит типу datatype. 
Если возвращаемое значение принадлежит какому-либо другому типу, 
декоратор должен возбуждать исключение TypeError.
"""
import functools

def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, datatype):
                return res
            raise TypeError
        return wrapper
    return decorator


@returns(int)
def add(a, b):
    return a + b
print(add(10, 5))  # 15

@returns(int)
def add(a, b):
    return a + b
try:
    print(add('199', '1'))
except TypeError as e:
    print(type(e))  # <class 'TypeError'>


#  9.8-9
"""
Реализуйте декоратор takes, который принимает произвольное количество позиционных аргументов, 
каждый из которых является типом данных.

Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, 
принадлежат одному из этих типов. 
Если хотя бы один аргумент не принадлежит одному из данных типов, 
декоратор должен возбуждать исключение TypeError.
"""
import functools


def takes(*param):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            arg = [type(el) for el in args] + [type(el) for el in kwargs.values()]
            if all(el in param for el in arg):
                return func(*args, **kwargs)
            raise TypeError

        return wrapper

    return decorator


@takes(int, str)
def repeat_string(string, times):
    return string * times


print(repeat_string('bee', 3))  # beebeebee


@takes(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]


print(append_this.__name__)
print(append_this.__doc__)

try:
    print(append_this([1, 2], 3))
except TypeError as e:
    print(type(e))


#  9.8-10
"""
Реализуйте декоратор add_attrs, который принимает произвольное количество именованных аргументов 
и устанавливает их в качестве атрибутов декорируемой функции. 
Названием атрибута должно являться имя аргумента, значением атрибута — значение аргумента.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""
import functools

def add_attrs(**params):
    def decorator(func):
        func.__dict__.update(params)
        # for key, val in params.items():
        #     func.__dict__[key] = val

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'

print(beegeek.attr1)  # bee
print(beegeek.attr2)  # geek


#  9.8-11
"""
Реализуйте декоратор ignore_exception, 
который принимает произвольное количество позиционных аргументов — типов исключений, и выводит текст:
- Исключение <тип исключения> обработано
  если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов.
- Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""
from functools import wraps

def ignore_exception(*params):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except params as err:
                print(f"Исключение {type(err).__name__} обработано")
                # print(f"Исключение {err.__class__.__name__} обработано")
        return wrapper
    return decorator


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x

f(0)
# Исключение ZeroDivisionError обработано


#  9.8-12
"""
Реализуйте декоратор retry, который принимает один аргумент:
times — натуральное число

Декоратор должен выполнять повторную попытку вызова декорируемой функции, 
если во время ее выполнения возникает ошибка. 
Декоратор должен вызывать ее до тех пор, пока не исчерпает количество попыток times, 
после чего должен возбуждать исключение MaxRetriesException.
"""
from functools import wraps

class MaxRetriesException(Exception):
    pass

def retry(times=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    continue
            raise MaxRetriesException
        return wrapper
    return decorator


@retry(3)
def no_way():
    raise ValueError

try:
    no_way()
except Exception as e:
    print(type(e))  # <class '__main__.MaxRetriesException'>


