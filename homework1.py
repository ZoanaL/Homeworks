
import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 300
    def to_study(self):
        print("Time to study")
        self.progress += 0.1
        self.gladness -= 5
    def to_work(self):
        print("Pora na roboty")
        self.gladness -= 7
        self.money += 40
        self.progress += 0.05
    def to_sleep(self):
        print("Time to go rest")
        self.gladness += 3
    def to_chill(self):
        print("Time to play")
        self.gladness += 10
        self.money -= 45
        self.progress -= 0.1
    def is_alive(self):
        if self.money <= 46:
            self.to_work()
        if self.progress <= 0:
            self.to_study()
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed extern")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 4
            self.to_work()

nick = Student(name = "Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
