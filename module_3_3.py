def print_params(a = 1 ,b = 'строка',c = True):
    print(a,b,c)

print_params()
print_params(3, 10, 22)
print_params(2,'abc')
print_params(False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'string', False]
values_dict ={'a': 'Python', 'b': True, 'c': 52}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'CSS']

print_params(*values_list_2, 42)
