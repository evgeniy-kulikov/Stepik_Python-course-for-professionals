#  11.3 Регулярные выражения
""""""


"""   *   *   *   Task   *   *   *   """


# 01
"""
PAN (Permanent Account Number) 
<letter><letter><letter><letter><letter><digit><digit><digit><digit><letter>
Input:  first number is ABCD EZZPA1234ZaPMQ0000O, check thusEZZPA1234ZAPMQ0000O, 
Output: EZZPA1234Z EZZPA1234Z
"""
regex = r'[A-Z]{5}\d{4}[A-Z]'


# 02
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют комментарии HTML.
Комментарии в страницах HTML помещаются между тегами <!-- и -->
Input:  <!-- header of page --> <-- incorrect header of page !-->
Output: <!-- header of page -->
"""
regex = r'<!--.*?-->'


# 03
"""
идентификационный номер, который имеет следующий формат:
* номер начинается с 0 - 3 строчных латинских букв включительно
* далее следует последовательность цифр, длина которой должна быть от 2 до 8 включительно
* после цифр указываются 3 или более заглавные латинские буквы
Input:  Dear citizen! Your old ID: tba44891AHH, your new ID: 781AHHGYT
Output: tba44891AHH 781AHHGYT
"""
regex = r'[a-z]{,3}\d{2,8}[A-Z]{3,}'


# 04
"""
почтовый индекс начинается с одной или двух заглавных латинских букв, за которыми следует одна цифра. 
После цифры может следовать один необязательный символ — цифра или заглавная латинская буква
далее через пробел указываются одна цифра и любые две заглавные латинские буквы, кроме C, I, K, M, O, V
Input:  Arthur: NW11 8AB, Timur: P01 3AX, Anri: H7Z9T4 Dima: N16 6PS
Output: NW11 8AB P01 3AX N16 6PS
"""
regex = r'[A-Z]{1,2}\d(?:\d|[A-Z])?\s\d[ABD-HJLNP-UW-Z]{2}'
