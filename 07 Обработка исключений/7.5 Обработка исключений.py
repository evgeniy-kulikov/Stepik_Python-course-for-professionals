#  7.5 Обработка исключений
""""""

"""
В Python можно создавать собственные типы исключений. 
Для создания собственного типа исключения необходимо создать класс, 
являющийся потомком (наследником) одного из уже существующего типа исключения. 
Самым верным вариантом является класс Exception.
"""
class MyError(Exception):
    pass

try:
    num = int(input())
    if num < 0:
        raise MyError('Число не должно быть отрицательным')
    else:
        print(num + 10)
except ValueError:
    print('Введите число')
except MyError as er:
    print(er)


"""
Методики LBYL и EAFP
При написании программного кода, который может потенциально возбуждать исключения, 
существуют два основных подхода:

LBYL (Look Before You Leap) — посмотри перед прыжком
EAFP (Easier to Ask Forgiveness than Permission) — проще извиниться, чем спрашивать разрешение
"""


""" Оператор assert """

"""
Синтаксис использования оператора assert следующий:
assert <утверждение>, <сообщение>

примерно эквивалентна записи: 
if not <утверждение>:
    raise AssertionError(<сообщение>)
"""
age = 29                # возраст человека
assert age > 0, 'Возраст должен быть положительным числом'


num1, num2 = 20, 0
assert num2 != 0, 'Делитель равен нулю.'
print('Частное равно:', num1 / num2)


"""
оператор assert — это средство отладки, которое проверяет утверждение, 
выступающее в качестве внутренней самопроверки вашей программы

оператор assert должен применяться только для того чтобы помогать разработчикам идентифицировать ошибки. 
Он не является механизмом обработки ошибок времени выполнения программы (исключений)

оператор assert может быть глобально отключен в настройках интерпретатора
"""



"""   *   *   *   Task   *   *   *   """


#  7.5-1
"""
Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:
string — произвольная строка
Функция должна возвращать True, если:
- его длина равна 9 или более символам
- в нем присутствуют большие и маленькие буквы любого алфавита
- в нем имеется хотя бы одна цифра
"""
def is_good_password(word: str)-> bool:
    if len(word) >= 9:
        if sum(el.isdigit() for el in word) > 0:
            if sum(el.islower() for el in word) > 0:
                if sum(el.isupper() for el in word) > 0:
                    return True
    return False


# Короче
def is_good_password(word: str) -> bool:
    return all([len(word) >= 9,
                any(map(str.isdigit, word)),
                any(map(str.islower, word)),
                any(map(str.isupper, word))])


# regrex (для двух языков)
import re
def is_good_password(word: str) -> bool:
    reg = r'(?=.*[a-z,а-я,ё])(?=.*[A-Z,А-Я,Ё])(?=.*\d).{9,}'
    return bool(re.findall(reg, word))

# print(is_good_password('МойПарольСамыйЛучший111'))  # True



#  7.5-2
"""
Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:
string — произвольная строка
Функция должна возвращать True, если:
- его длина равна 9 или более символам
- в нем присутствуют большие и маленькие буквы любого алфавита
- в нем имеется хотя бы одна цифра

или возбуждать исключение:
- LengthError, если его длина меньше 9 символов
- LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
- DigitError, если в нем нет ни одной цифры
"""
class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass


def is_good_password(word: str) -> bool:
    if len(word) < 9:
        raise LengthError
    if word.upper() == word or word.lower() == word:
        raise LetterError
    if word.isalpha():
        raise DigitError
    return True


#  7.5-3
"""
https://stepik.org/lesson/640052/step/9?thread=solutions&unit=636572
Воспользуйтесь функцией is_good_password() из предыдущей задачи.
На вход программе подается произвольное количество паролей, каждый на отдельной строке.
После ввода хорошего пароля все последующие пароли должны игнорироваться.
"""
import sys
data = list(map(str.strip, sys.stdin))


def is_good_password(word: str) -> str:
    if len(word) < 9:
        return 'LengthError'
    if word.upper() == word or word.lower() == word:
        return 'LetterError'
    if word.isalpha():
        return 'DigitError'
    return 'Success!'

for el in data:
    print(is_good_password(el))
    if is_good_password(el) == 'Success!':
        break


# Решение по теме
import sys

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string: str) -> bool:
    if len(string) < 9:
        raise LengthError('LengthError')
    if string == string.upper() or string == string.lower():
        raise LetterError('LetterError')
    if string.isalpha():
        raise DigitError('DigitError')
    return True

for el in sys.stdin:
    try:
        if is_good_password(el.strip()):
            print('Success!')
            break
    except PasswordError as err:
        print(err)
