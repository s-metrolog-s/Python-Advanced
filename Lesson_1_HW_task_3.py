# Задача 3
# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1_000
OUT_OF_BOUND = -1

number = randint(LOWER_LIMIT, UPPER_LIMIT)

user_input = OUT_OF_BOUND
counter = 0

while counter < 5:
    user_input = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}:'))
    # Проверку диапазона вводим для всех попыток
    if number < LOWER_LIMIT or number > UPPER_LIMIT:
        print(f'Число {user_input} за пределами диапазона')
        continue
    else:
        if user_input > number:
            print(f'Введенное число {user_input} больше загаданного числа')
            counter += 1
        elif user_input < number:
            print(f'Введенное число {user_input} меньше загаданного числа')
            counter += 1
        else:
            print(f'Вы угадали загаданное число {number}')
            quit()
else:
    print('К сожалению, вы не угадали,попытки закончились. Попробуйте снова')