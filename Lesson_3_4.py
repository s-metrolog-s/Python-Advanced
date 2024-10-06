# список с порядковыми номера нечетных значений

my_list = [1, 1, 2, 33, 3, 3, 4, 4, 5, 6, 7]

result = []

for i in range(len(my_list)):
    if my_list[i] % 2:
        result.append(i + 1)
print(f'{result = }')

my_list = [1, 1, 2, 33, 3, 3, 4, 4, 5, 6, 7]
result_2 = []
for i, item in enumerate(my_list, 1):
    if item % 2:
        result_2.append(i)
print(f'{result_2 = }')