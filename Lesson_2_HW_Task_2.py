'''
Задача 2
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
'''

import fractions

ERROR_INPUT = 'Введены не вырные данные: '
check_input = True
sum = []
multiply = []

while True:
    check_input = True
    num_1 =  input('Введите первую дробь в формате x/y: ')
    num_2 =  input('Введите вторую дробь в формате x/y: ')

    number_1 = list(num_1.split('/'))
    number_2 = list(num_2.split('/'))

    # Проверка на знак деления в пользовательском вводе
    if '/' not in num_1 or '/' not in num_2:
        print(f'{ERROR_INPUT}необходим знак деления')
        check_input = False
    else:
        # Проверка на наличие только цифр в аргументах дроби
        for i in (number_1, number_2):
            for j in i:
                if not j.isdigit():
                    print(f'{ERROR_INPUT}в аргументах дробей должны быть цифры. Попробуйте снова')
                    check_input = False

    if not check_input:
        continue
    else:
        # Переводим значения в списках в числа
        number_1 = list(map(int, number_1))
        number_2 = list(map(int, number_2))

        # Находим сумму
        if number_1[1] != number_2[1]:
            temp = list(map(lambda x: x * number_2[1], number_1))
            number_2 = list(map(lambda x: x * number_1[1], number_2))
            number_1 = temp
        sum.append(number_1[0] + number_2[0])
        sum.append(number_1[1])

        # Находим произведение для числителя и знаменателя
        for i in range(2):
            multiply.append(number_1[i] * number_2[i])

        print(f'До сокращения множителей\nСумма дробей: {sum[0]}/{sum[1]} Произведение: {multiply[0]}/{multiply[1]}')

        # Сокращаем множители
        for i in (sum, multiply):
            common_delimiter = i[0] if i[0] < i[1] else i[1]
            while common_delimiter > 0:
                if i[0] % common_delimiter == 0 and i[1] % common_delimiter == 0:
                    i[0] = i[0] // common_delimiter
                    i[1] = i[1] // common_delimiter
                common_delimiter -= 1

        print(f'После сокращения множителей\nСумма дробей: {sum[0]}/{sum[1]} Произведение: {multiply[0]}/{multiply[1]}')

    frac_number = fractions.Fraction(number_1[0], number_1[1])
    frac_number_2 = fractions.Fraction(number_2[0], number_2[1])
    print('Проверка модулем fractions:')
    print(frac_number + frac_number_2, end=' ')
    print(frac_number * frac_number_2)

    quit()