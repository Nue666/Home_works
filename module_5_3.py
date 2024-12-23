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

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self

    def __mul__(self, value):
        self.number_of_floors *= value.number_of_floors
        return self

    def __sub__(self, value):
        self.number_of_floors -= value
        return self


house_1 = House('ЖК Эльбрус', 30)
house_2 = House('Домик в деревне', 2)
house_3 = House('ЖК Новая Поляна', 10)

print(house_1 == house_2)
print(house_3 == house_3)
print(house_1 < house_3)
print(house_1 > house_3)
print(house_1 >= house_2)
print(house_1 <= house_2)
print(house_1 != house_2)
print(house_1 != house_1)

print()
print(house_1)
house_1 = house_1 + 3
print(house_1)

print()
print(house_2)
house_2 = 5 + house_2
print(house_2)

print()
print(house_3)
house_3 += 10
print(house_3)

print()
print(house_3)
house_3 = house_1 * house_3
print(house_3)

print()
print(house_2)
house_2 = house_2 - 1
print(house_2)

print()
a = 5 + house_1
print(a)
b = house_1 + 10
print(b)