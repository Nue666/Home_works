def func(data):
    values = []
    for item in data:
        if isinstance(item, (list, tuple,set)):
            values.extend(func(item))
        elif isinstance(item, dict):
            for key in item.items():
                values.extend(func(key))
        elif isinstance(item, (int,float)):
            values.append(item)

        elif isinstance(item, str):
            values.append(len(item))
    return values



data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

data_structure_2 = [
    {1: ('avc', 3, 4), 2: 4},
    [[{1,2,3,4,'asds'}]],
    [32, 64, ['avc', [12]]]
]

result_1 = func(data_structure)
result_2 = func(data_structure_2)
print(sum(result_1))
print(sum(result_2))