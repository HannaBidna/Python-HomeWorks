import time


class Auto:
    cоlor = 'Blue'
    weight = 2

    def __init__(self, brand, mark, age):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('Move')

    def stop(self):
        print('Stop')

    def birthday(self, age):
        self.age = int(age)
        self.age += 1

class Car(Auto):
    def __init__(self, brand, mark, age,  max_speed):
           super().__init__(brand, mark, age)
           self.max_speed = max_speed

    def move(self, max_speed):
          super().move()
          print(f'Max speed = {max_speed}')

class Truck(Auto):
    def __init__(self, brand, mark, age, max_load):
           super().__init__(brand, mark, age)
           self.max_load = max_load

    def move(self):
           print('Attention!')
           super().move()


    def load(self):
           time.sleep(1)
           print('load...')
           time.sleep(1)



car_1 = Car('audi', 'a6', 8, 160)
car_2 = Car ('BMW','M140', 5, 180)
car_2.weight = 3
car_1.color = 'white'

print(f'Brand Car1: {car_1.brand}')
print(f'Mark Car1: {car_1.mark}')
print(f'Max speed Car1: {car_1.max_speed}')
print(f'Age Car1: {car_1.age}')
print(f'Color Car1: {car_1.color}')
print()

print(f'Brand Car2: {car_2.brand}')
print(f'Mark Car2: {car_2.mark}')
print(f'Max speed Car2: {car_2.max_speed}')
print(f'Age Car2: {car_2.age}')
print(f'Weight Car2: {car_2.weight}')
print()

car_1.move(160)
car_1.stop()
car_1.birthday(8)
print(f'New Age: {car_1.age}')
print()


car_2.move(160)
car_2.stop()
car_2.birthday(8)
print(f'New Age: {car_2.age}')
print()

truck_1 = Truck('Kraz', '6322', 3, 10)
truck_2 = Truck('Mercedes', 'Srinter', 6, 4)
truck_1.weight = 7
truck_2.color = 'red'

print(f'Brand Truck1: {truck_1.brand}')
print(f'Mark Truck1: {truck_1.mark}')
print(f'Max load Truck1: {truck_1.max_load}')
print(f'Age Truck1: {truck_1.age}')
print(f'Weight Truck2: {truck_1.weight}')
print()

print(f'Brand Truck2: {truck_1.brand}')
print(f'Mark Truck2: {truck_1.mark}')
print(f'Max load Truck2: {truck_1.max_load}')
print(f'Age Truck2: {truck_1.age}')
print(f'Color Truck2: {truck_2.color}')
print()

truck_1.load()
truck_1.move()
truck_1.stop()
truck_1.birthday(3)
print(f'Age: {truck_1.age}')
print()

truck_2.load()
truck_2.move()
truck_2.stop()
truck_2.birthday(3)
print(f'New Age: {truck_2.age}')
print()