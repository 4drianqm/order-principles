from food import Food


class Cat:
    def __init__(self, name: str):
        self.name = name
        self.energy = 0

    def eat(self, food: Food):
        self.energy += food.get_nutrition()

    def play(self):
        if self.energy > 0 :
            print('Im playing')
        else:
            print('Im tired')

