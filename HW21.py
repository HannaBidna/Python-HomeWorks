class Auto:
    cоlor = blue
    weight = 2

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('Mowe')

    def stop(self):
        print('Stop')

    def birthday(self):
        self.age += 1