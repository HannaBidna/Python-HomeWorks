
from datetime import datetime


class Person:
    def __init__(self, first_name, last_name=None, middle_name=None, birth_date=None, death_date=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.gender = gender

    def calculate_age(self):
        if self.death_date:
            end_date = datetime.strptime(self.death_date, '%d/%m/%Y')
        else:
            end_date = datetime.now()

        birth_date = datetime.strptime(self.birth_date, '%d/%m/%Y')
        delta = end_date - birth_date
        return int(delta.days // 365.25)

