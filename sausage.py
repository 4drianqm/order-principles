from datetime import date
from food import Food


class Sausage(Food):
    def __init__(self, energy: float, due_date: date):
        self.energy = energy
        self.date_date = due_date

    def get_nutrition(self):
        if self.date_date > date.today():
            return -10
        else:
            return self.energy

