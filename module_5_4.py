class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

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

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


house_1 = House('ЖК Эльбрус', 30)
print(House.houses_history)
house_2 = House('Домик в деревне', 2)
print(House.houses_history)
house_3 = House('ЖК Новая Поляна', 10)
print(House.houses_history)

del house_2
del house_3

print(House.houses_history)