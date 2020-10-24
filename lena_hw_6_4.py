"""
Let's play Cars
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = 0
        self.color = ""
        self.name = ""
        self.is_police = False
        print(f"{name}, color: {color}, speed: {speed}")

    def go(self):
        print("Your car is going")

    def stop(self):
        print("Your car was stopped")

    def turn(self, direction):
        print(f"Your car turns {direction}")

    def show_speed(self, speed):
        print(f"Speed: {speed}")


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        print(f"Speed:{speed}")
        if speed > 60:
            print("Speed exceeded")


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, speed):
        print(f"Speed:{speed}")
        if speed > 40:
            print("Speed exceeded")


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police_car(self, is_police):
        if is_police == True:
            print("POLICE CAR")


tc = TownCar(70, "grey", "my_volvo_car", False)
tc.go()
tc.turn("left")
tc.show_speed(70)
tc.stop()

sc = SportCar(220, "red", "lamborghini", False)
sc.go()
sc.turn("right")
sc.show_speed(250)
sc.stop()

wc = WorkCar(20, "yellow", "ant", False)
wc.show_speed(15)

pc = PoliceCar(90, "multicolor", "logan", True)
pc.police_car(True)
