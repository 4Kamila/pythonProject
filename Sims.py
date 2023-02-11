import random
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet

    def get_pet(self):
        self.pet = Pet(pet_list)
        self.pet = Pet(pet_breed)
    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)


    def get_job(self):
        if self.pet.health >= 10:
            pass
        else:
            self.vet()
            return
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.pet.food <= 0:
            self.shopping("pet.food")
        else:
            if self.pet_satiety >= 100:
                self.pet_satiety = 100
                return
            elif self.pet_satiety <= 20:
                self.feed_pet()
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
        self.pet_gladness -= 2

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15
        elif manage == "pet_food":
            print("I bought food for pet")
            self.pet_gladness += 5
            self.pet_satiety += 2
            self.money -= 30
            self.pet.food += 30

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        self.pet_gladness += 2

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def clean_pet_toilet(self):
        self.gladness -= 10
        self.pet_gladness += 5
        self.pet_toilet = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
    def vet(self):
        self.pet.health = 100
        self.money -= 50
        self.pet_gladness -= 5
    def play_w_pet(self):
        self.gladness += 5
        self.pet_gladness += 10
    def feed_pet(self):
        self.pet_satiety += 5
        self.pet.food -= 5



    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
        pet_indexes = f"{self.pet.breed} pet indexes"
        print(f"{pet_indexes:^50}", "\n")
        print(f"Health – {self.pet.health}")
        print(f"Satiety – {self.pet_satiety}")
        print(f"Gladness – {self.pet_gladness}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car{self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
        if self.pet is None:
            self.get_pet()
            print(f"I don't have a pet, I'm gonna choose a job "
                  f"I have a {self.pet_list} , breeds {self.pet_breed}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…")
                print("So I will clean the house")
                self.clean_home()
            elif self.pet_toilet > 10:
                print("Gooosh, it is so horrible smell !")
                print("So I will clean the pet toilet")
                self.clean_pet_toilet()
            else:
                print("Let`s chill!")
                self.chill()
        elif self.pet_gladness < 10:
            print("My pet is sad (")
            self.play_w_pet()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")

pet_list = {
    "Cat":{"health": 50, "gladness": 60, "satiety": 80},
    "Dog":{"health": 40, "gladness": 80, "satiety": 100},
    "Parot":{"health": 100, "gladness": 90, "satiety": 60},
}
pet_breed = {

}

class Pet:
    def __init__(self, pet_list):
        self.pet = random.choice(list(pet_list))
        self.pet_health = pet_list[self.pet]["health"]
        self.pet_gladness = pet_list[self.pet]["gladness"]
        self.pet_satiety = pet_list[self.pet]["satiety"]

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}}
class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list (brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption=brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.pet.food = 0

job_list = {
 "Java developer":
                {"salary":50, "gladness_less": 10 },
 "Python developer":
                {"salary":40, "gladness_less": 3 },
 "C++ developer":
                {"salary":45, "gladness_less": 25 },
 "Rust developer":
                {"salary":70, "gladness_less": 1 },
 }

class Job:
    def __init__(self, job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]

nick = Human(name="Nick")
for day in range(1,800):
    if nick.live(day) == False:
        break
