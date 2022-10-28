import random
class Student:
    group = "B2910"
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.cash = 500

    def to_study(self):
        print("Personal life, NOT GOING TO ALLOW THAT! Study now.")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I want to sleep :C pls no hard hw :C")
        self.gladness += 3

    def to_chill(self):
        print("I CAN REST WOOOOO")
        self.progress -= 0.1
        self.gladness += 5
        self.cash -= 50

    def to_work(self):
        print("Time to get some cash.")
        self.cash += 40
        self.gladness -= 2

    def is_alive(self):
        if self.progress < -0.5:
            print("Get outta here")
        elif self.gladness <= 0:
            print("Oh. Look at that. Your old buddy D E P R E S S I O N is back!")
            self.alive = False
        elif self.progress > 5:
            print("You have passed the course, through all the hardships and barriers... Good job...")
            self.alive = False
        elif self.cash <= 0:
            print("You are broke now good job.")
            self.alive = False



    def end_of_the_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Cash = {round(self.cash)} $")

    def days_of_life(self, day):
        day = "Day " + str(day) + "of" + self.name + "live"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_work()
        elif live_cube == 4:
            self.to_sleep()
        self.end_of_the_day()
        self.is_alive()



nick = Student(name = "Nick")
for day in range (365):
    if nick.alive == False:
        break
    nick.days_of_life(day)




