"""
1. класс TrafficLight
"""

from time import sleep


class TrafficLight:

    __color = ""

    def running(self):

        model = ["red", "yellow", "green"]
        fact_list = []
        while True:
            TrafficLight.__color = "red"
            fact_list.append(TrafficLight.__color)
            print(TrafficLight.__color)
            sleep(7)
            TrafficLight.__color = "yellow"
            fact_list.append(TrafficLight.__color)
            print(TrafficLight.__color)
            sleep(2)
            TrafficLight.__color = "green"
            fact_list.append(TrafficLight.__color)
            print(TrafficLight.__color)
            sleep(7)
            if fact_list != model:
                print("The traffic light has blurred")
                break
            fact_list = []


tl_1 = TrafficLight()
tl_1.running()
