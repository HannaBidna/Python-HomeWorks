class Auto:
    def __init__(self, brand, age, mark, cоlor='blue', weight=2):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('Move')

    def stop(self):
        print('Stop')

    def birthday(self):
        self.age += 1

