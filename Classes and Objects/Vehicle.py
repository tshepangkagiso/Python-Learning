# Design a Vehicle class hierarchy with a base Vehicle class and derived classes for different types of vehicles (e.g., Car, Motorcycle, Truck). Include appropriate attributes and methods for each class.

class Vehicle:
    def __init__(self, wheels = 0, weight = 0, color = "black"):
        self.wheels = wheels
        self.weight = weight
        self.color = color

    def SetWheels(self):
        try:
            self.wheels = int(input("Enter amount of wheels: "))
        except Exception as ex:
            print(ex)

    def SetWeight(self):
        try:
            self.weight = int(input("Enter Vehicle weight: "))
        except Exception as ex:
            print(ex)

    def SetColor(self):
        try:
            self.color = input("Enter Vehicle color: ")
        except Exception as ex:
            print(ex)

class Car(Vehicle):
    def __init__(self, wheels, weight, color):
        super().__init__(wheels, weight, color)


class Motorcycle(Vehicle):
    def __init__(self, wheels, weight, color):
        super().__init__(wheels, weight, color)

class Truck(Vehicle):
    def __init__(self, wheels, weight, color):
        super().__init__(wheels, weight, color)


car = Car(4,1200,"red")
car.SetWheels()
car.SetWeight()
car.SetColor()
print(f"Weight: {car.weight}kg, Wheels: {car.wheels}, Color: {car.color} \n")



bike = Motorcycle(2, 500, "black")
bike.SetWheels()
bike.SetWeight()
bike.SetColor()
print(f"Weight: {bike.weight}kg, Wheels: {bike.wheels}, Color: {bike.color} \n")

truck = Truck(8, 8000, "white")
truck.SetWheels()
truck.SetWeight()
truck.SetColor()
print(f"Weight: {truck.weight}kg, Wheels: {truck.wheels}, Color: {truck.color} \n")