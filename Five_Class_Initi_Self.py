class Car():
    def __init__(self,speed,color):
        print(speed)
        print(color)
        self.speed = speed
        self.color = color
        print("Init is called")

ford = Car(40,"Red")
honda = Car(50,"Black")

# ford.speed = 200
# ford.color = "Red"
#
# honda.speed = 300
# honda.color = "Black"
#
print(ford.speed,"",ford.color)
# print(honda.speed,"",honda.color)
#
# ford.speed = 400
# ford.color = "Orange"
#
# print(ford.speed,"",ford.color)