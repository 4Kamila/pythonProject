class Adult:
    height = 180
    age = 32
    contry = "Peru"
    food = "pizza"
class Teen(Adult):
    height = 174
    age = 15
    food = "cheese"
class Child(Teen):
    food = "milk"
    def __init__(self):
        print(self.age)
        print(self.height)
        print(self.food)
        print(self.contry)
Ann = Adult()
Micki = Teen()
Tony = Child()

