# Задача 2
# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

UPPER_LIMIT = 100_000
ZERO = 0
NUMBER_OF_MAX_DELIMIMETERS = 2

number = ZERO

while number > ZERO or number < UPPER_LIMIT:
    number = int(input('Введите число: '))
    delimiter = ZERO
    for i in range(1, number + 1):
        if number % i == ZERO:
            delimiter += 1
    if delimiter == ZERO:
        print(f'Число {number} не является ни простым, ни составным')
    elif delimiter > NUMBER_OF_MAX_DELIMIMETERS:
        print(f'Число {number} является составным')
    else:
        print(f'Число {number} является простым')
