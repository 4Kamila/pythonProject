# class Adult:
#     height = 180
#     age = 32
#     contry = "Peru"
#     food = "pizza"
# class Teen(Adult):
#     height = 174
#     age = 15
#     food = "cheese"
# class Child(Teen):
#     food = "milk"
#     def __init__(self):
#         print(self.age)
#         print(self.height)
#         print(self.food)
#         print(self.contry)
# Ann = Adult()
# Micki = Teen()
# Tony = Child()

import random
class Math:

    def __number(self):
        a = int(input("a = "))
        b = int(input("b = "))
        dice = random.randint(1, 4)
        if dice == 1:
            print(a + b)
        elif dice == 2:
            print(a - b)
        elif dice == 3:
            print(a * b)
        elif dice == 4:
            print(a / b)

some_obj=Math()
some_obj._Math__number()

