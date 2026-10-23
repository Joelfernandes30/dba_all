class Car:
    def __init__(self, color, seats, wheels):  #constructor
        self.color = color
        self.seats = seats
        self.wheels = wheels

    def display_info(self):
        return f"this is a {self.color} car with {self.seats} seats and {self.wheels} wheels"

    def fly(self):
        return "this car can fly"

    def run(self):
        return "this car can run"

audi = Car("red", 4, 5)

print(audi.seats)
print(audi.fly())
print(audi.run())
print(audi.display_info())

bmw = Car("blue", 4, 5)
print(bmw.seats)
print(bmw.fly())
print(bmw.run())
print(bmw.display_info())
