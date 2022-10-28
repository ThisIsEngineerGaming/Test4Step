import random
class Cat:
    group = "B2910"
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.toilet = 0
        self.alive = True
        self.hunger = 30
        self.shkoda = 30

    def to_go_to_the_toilet(self):
        print("Toilet break.")
        self.toilet =- 5
        self.gladness -= 3

    def to_sleep(self):
        print("Sleeping is good ain`t that right?")
        self.gladness += 3
        self.hunger =+ 1

    def to_chill(self):
        print("Playing time!")
        self.toilet += 2
        self.gladness += 5
        self.hunger += 1

    def to_eat(self):
        print("Time to eat!")
        self.toilet += 2
        self.hunger -= 1
        self.gladness -= 2
    def to_shkoda(self):
        self.gladness += 5
        self.shkoda += 5

    def is_alive(self):
        if self.toilet >= 20:
            print("You pissed yourself.")
            self.alive = False
        elif self.gladness <= 0:
            print("Oh. Look at that. Your old buddy D E P R E S S I O N is back!")
            self.alive = False
        elif self.hunger > 60:
            print("You died of hunger.")
            self.alive = False
        elif self.hunger < 0:
            print("Wait how did you. What. How did you manage to invert your stomach tissues inside out? Well anyways you died from that.")
            self.alive = False
        elif self.shkoda > 60:
            print("Bad kitty, shoo,shoo. You got kicked out of the house.")
            self.alive = False



    def end_of_the_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Toilet = {round(self.toilet)} needing to pee level.")
        print(f"Hunger = {round(self.hunger)} needing to eat level")
        print(f"Owner`s temper {self.shkoda}")

    def days_of_life(self, day):
        day = "Day " + str(day) + "of" + self.name + "live"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_go_to_the_toilet()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_eat()
        elif live_cube == 4:
            self.to_shkoda()
        elif live_cube == 5:
            self.to_sleep()
        self.end_of_the_day()
        self.is_alive()



cat = Cat(name = "cat")
for day in range (366):
    if cat.alive == False:
        break
    cat.days_of_life(day)


