# from order import Order
# from item import Item
#
#
#
# order = Order('GT')
# order.add_item(Item('Pokemon', 4, 20))
# order.add_item(Item('Halo', 2, 4.4))
#
# total = order.get_total()
# print(total)
from datetime import date
from cat import Cat
from sausage import Sausage
from salmon import Salmon


cat1 = Cat('Garfield')
sausage = Sausage(20, date(2023, 9, 15))
salmon = Salmon(100, date(2023, 5, 25))

cat1.eat(sausage)
cat1.eat(salmon)

