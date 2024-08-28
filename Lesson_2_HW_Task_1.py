'''
Задача 1.
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.
'''

DELIMETER = 16
CHAR_SHIFT = 97 - 10 # 97 код первой буквы в UNICODE, 10 первое число заменяемое на букву
MAX_NUM = 9

number_main: int = int(input('Введите целое число: '))

result: str = ''

number = number_main
while number > 0:
    temp = number % DELIMETER
    number //= DELIMETER
    if temp > MAX_NUM:
        num = chr(temp + CHAR_SHIFT)
    else:
        num = str(temp)
    result = num + result
result = '0x' + result
print(f'Число {number_main} в шестнадцатеричной системе: {result}')
print(f'Проверка полученного числа с формулой HEX {result == hex(number_main)}')

# Можно сделать через match
# match temp:
#     case 10: num = 'a'
#     case 11: num = 'b'
#     case 12: num = 'c'
#     case 13: num = 'd'
#     case 14: num = 'e'
#     case 15: num = 'f'
#     case _: num = temp