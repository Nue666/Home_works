immutable_var = (1 , 3 , 'привет', True, [1, 3, 'Hello', False])
print(f'Неизменяемый тип данных(кортеж): {immutable_var}')
mutable_list = [1, 2, 3, 'Hola!', True]
mutable_list[0] = 10
mutable_list[4] = False
mutable_list[3] = 'Adios'
print(f'Изменяемый тип данных(список): {mutable_list}')