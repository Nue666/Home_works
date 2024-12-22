class House():
    def __init__(self,name,number):
        self.name = name
        self.number_of_floors = number

    def go_to(self,new_floor):
        if (new_floor > self.number_of_floors) or (new_floor < 1):
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.'

    def __len__(self):
        return self.number_of_floors

house_1 = House('ЖК Эльбрус', 30)
house_2 = House('Домик в деревне', 2)
house_3 = House('ЖК Новая Поляна', 10)

print(house_1)
print(house_2)
print(house_3)

print(len(house_1))
print(len(house_2))
print(len(house_3))

