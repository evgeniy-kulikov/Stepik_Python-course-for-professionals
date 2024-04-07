# 11.1 Регулярные выражения
""""""


"""   *   *   *   Task   *   *   *   """


# 01
"""
Вам доступно регулярное выражение regex, которому соответствуют строки car, cat и cab. 
Перепишите его с использованием набора символов, чтобы ему соответствовали те же строки.
Input:  Car cAt caB caaaaaat carrrrrr-kar
Output: car
"""
regex = r'ca[rtb]'


# 02
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют все шестнадцатеричные цифры. 
Предполагается, что шестнадцатеричные цифры образуют множество:
0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
Input:  this is digit 10, A in hex 
Output: 1 0 A
"""
regex = r'[0-9A-F]'


# 03
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют последовательности символов формата Xxxxx, 
где X — любая буква латинского алфавита в произвольном регистре, 
а x — произвольная цифра.
Input:  is valid number A123(-), a123(-), B12345(+), b12345(+)
Output: B1234 b1234
"""
regex = r'(?i)[a-z]\d{4}'


# 04
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют последовательности символов длины 5, удовлетворяющие следующим условиям:
* первый символ — строчная латинская буква
* второй символ — произвольная цифра
* третий символ — строчная латинская буква
* четвертый символ — заглавная латинская буква
* пятый символ — заглавная латинская буква
Input:  Stood u1pPP
Output: u1pPP
"""
regex = r'[a-z]\d[a-z][A-Z]{2}'


# 05
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют последовательности символов длины 6, 
удовлетворяющие следующим условиям:
* первый символ — произвольная цифра
* второй символ — строчная латинская гласная буква (a, e, i, o, u, y)
* третий символ — любой символ, кроме b, c, D, F
* четвертый символ — любой не пробельный символ
* пятый символ — любой символ, кроме заглавной латинской гласной буквы (A, E, I, O, U, Y)
* шестой символ — любой символ, кроме точки и запятой
Input:  password do you prefer: 9ython or 4uTUMN?
Output: 9ython 4uTUMN
"""
regex = r'\d[aeiouy][^bcDF]\S[^AEIOUY][^,\.]'


# 06
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют последовательности символов длины 6, удовлетворяющие следующим условиям:
* первый символ — цифра 1, 2 или 3
* второй символ — цифра 0, 1 или 2
* третий символ — цифра 1, 2 или строчная латинская буква x
* четвертый символ — цифра 0, 3 или латинская буква a в любом регистре
* пятый символ — строчная латинская буква x, s или u
* шестой символ — точка или запятая
Input:  _010x. A010x, 4010s. 1010s, 010u. '010u,
Output: 1010s,
"""
regex = r'[1-3][0-2][12x][03aA][xsu][,\.]'


# 07
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют телефонные номера следующих форматов:
+7xxxxxxxxxx
+7(xxx)xxxxxxx
+7(xxx)-xxx-xx-xx
+7 xxx xxx xx xx
где x — произвольная цифра.  Дополнительная проверка телефонного номера на корректность не требуется.
Input:  +7(917) 634 81 19 +7-917-634-81-19 +8(917)-634-81-19 +791768790541 +7 917 687 90 54
Output: +79176879054 +7 917 687 90 54
"""
# regex = r'\+7\d{10}|\+7\(\d{3}\)\d{7}|\+7\(\d{3}\)-\d{3}(-\d{2}){2}|\+7(\s\d{3}){2}(\s\d{2}){2}'
regex = r'\+7\d{10}|\+7\(\d{3}\)\d{7}' \
        r'|\+7\(\d{3}\)-\d{3}(-\d{2}){2}' \
        r'|\+7(\s\d{3}){2}(\s\d{2}){2}'


# 08
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют даты следующих форматов:
DD.MM.YYYY
DD/MM/YYYY
YYYY.MM.DD
YYYY/MM/DD
Input:  first date: 01.12.22, second date: 01/12/22, thirs date 09.07.2003 07/09/2003
Output: 09.07.2003 07/09/2003
"""
# regex = r'(?:\d\d\.){2}\d{4}|(?:\d\d/){2}\d{4}|\d{4}(?:\.\d\d){2}|\d{4}(?:/\d\d){2}'
regex = r'(?:\d\d\.){2}\d{4}' \
        r'|(?:\d\d/){2}\d{4}' \
        r'|\d{4}(?:\.\d\d){2}' \
        r'|\d{4}(?:/\d\d){2}'


# 09
"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, 
которому соответствуют времена формата HH:MM
Input:  00:00, 00:60, 24:00, 50:39, 17/30 - 23:59
Output: 00:00 23:59
"""
regex = r'(?:[0-1]\d|2[0-3]):[0-5]\d'
