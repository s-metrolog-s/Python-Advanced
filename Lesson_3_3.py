my_tuple = (42, 73, 3.14, 'Hello World', None, True, 'Text', 100500.2, False)

result = {}

# for item in my_tuple:
#     key = type(item)
#     if key not in result:
#         value = [x for x in my_tuple if isinstance(x, type(item))]
#         result[key] = value
# print(f'{result = }')

for item in my_tuple:
    key = result.setdefault(type(item), list())
    key.append(item)