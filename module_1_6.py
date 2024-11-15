#Словари
my_dict = {'1': 'номер 1', '2': 'номер 2', '3': 'номер 3', 'answer': True, 'год рождения': 2002}
print(my_dict)
print(my_dict['год рождения'])
my_dict['имя'] = 'Константин'
print(my_dict['имя'])
my_dict.update(
    {'номер телефона': 8993939992,
     'почтовый индекс': 423333})
object = my_dict.pop('1')
print(object, my_dict, sep = '\n')

print('')

#Множества
my_set = {1, 2, 3, 4, 4, 4, 'жесть', 'жесть',}
print(my_set)
my_set.add('тридцать три')
my_set.add(33)
my_set.remove(1)
print(my_set)