class CustomErrors(Exception):
    def __init__(self):
        super().__init__()


class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        try:
            result = self.a + self.b
            print(f' Сума = {result}')
        except NameError:
            return None

    def __sub__(self):
        result = self.a - self.b
        print(f' Різниця = {result}')

    def __mul__(self):
        result = self.a * self.b
        print(f' Добуток = {result}')

    def __truediv__(self):
        try:
            result = self.a/self.b
            print(f' Частка = {result}')
        except ZeroDivisionError:
           print('Ділення на нуль!')
           return None

    def root(self):
        try:
            if self.a < 0:
                raise CustomErrors
            result = self.a ** 1/self.b
            print(f' Корінь {numbers.b } ступіня з  числа {numbers.a} = {float(result)}')
        except ZeroDivisionError:
            print('Ділення на нуль!')
            return None

        except CustomErrors:
            print('Корінь неможливо обчислити!')
            return None

    def power(self):
        try:
            if self.b < 0:
                raise CustomErrors
            result = self.a ** self.b
            print(f' {numbers.b} cтупінь  числа {numbers.a} = {float(result)}')
        except CustomErrors:
            print('Негативний ступінь, виняток')
            return None
try:
    a = float(input())
    b = float(input())
except ValueError:
    print('Це не число!')
try:
    numbers = Calc(a, b)
    print(f' Числа {numbers.a}, {numbers.b}')
except NameError:
    print('Введіть число')
else:
    numbers.__add__()
    numbers.__sub__()
    numbers.__mul__()
    numbers.__truediv__()
    numbers.root()
    numbers.power()





