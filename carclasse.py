class Car:
    def __init__(self, make, type, color):
        self.make = make
        self.type = type
        self.color = color
        self.mileage = 0
    
    def info(self):
        return f"This is a {self.make}, {self.type} with color {self.color} and mileage of {self.mileage}"

    def drive(self, distance):
        if distance < 0:
            raise 'You can not drive a negative distance...'
        else:
            self.mileage += distance
    


car1 = Car('Fiat', 'Panda', 'Rood')
car2 = Car('Fiat', 'Panda', 'Blauw')

print(car1.info())
car1.drive(10)
print(car1.info())
print(car2.info())
car2.drive(-10)


