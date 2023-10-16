import datetime


class Person():
    def __init__(self, name, birth_date, death_date, gender, surname=None, second_name=None):
        self.gender = gender
        self.name = name

        if death_date != '':
            for x, y in ('.', '/'), (',', '/'), (' ', '/'), ('-', '/'):
                self.death_date = death_date.replace(x, y)
            self.death_date = datetime.datetime.strptime(self.death_date, '%d/%m/%Y')
        else:
            self.death_date = None

        for x, y in ('.', '/'), (',', '/'), (' ', '/'), ('-', '/'):
            self.birth_date = birth_date.replace(x, y)
        self.birth_date = datetime.datetime.strptime(self.birth_date, '%d/%m/%Y')

    def age(self):
        now = datetime.date.today()

        if self.death_date is None:
            if now.month < self.birth_date.month:
                result = now.year - self.birth_date.year - 1
            elif now.month == self.birth_date.month and now.day < self.birth_date.day:
                result = now.year - self.birth_date.year - 1
            else:
                result = now.year - self.birth_date.year
        else:
            result = self.death_date.year - self.birth_date.year
        return result

person_1 = Person('Ліна', '16-03-1930', '', 'ж', 'Костенко', '')
person_2 = Person('Василь', '06-01-1938', '04-09-1985', 'ч', 'Стус', 'Семенович')

print(person_1.age())
