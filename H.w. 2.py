import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
    def to_work(self):
        print("Work time")
        self.gladness -= 4
        self.progress += 0.15
        self.money += 50
    def is_alive(self):
        if self.progress < -0.5:
            print("cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally")
            self.alive = False
        elif self.money <= 0:
            print("Bankrupt…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if self.progress <= 0.5:
            progress_cube = random.randint(1, 2)
            if progress_cube == 1:
                self.to_work()
            elif progress_cube == 2:
                self.to_study()
        if self.money <= 25:
            print("I need work")
            self.to_work()
        else:
            self.to_chill()
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)