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

house_1 = House('ЖК Эльбрус', 30)
house_2 = House('Домик в деревне', 2)
house_3 = House('ЖК Новая Поляна', 10)

print(house_1.name, house_1.number_of_floors)
print(house_3.name, house_3.number_of_floors)

house_1.go_to(10)
house_2.go_to(3)
house_3.go_to(5)