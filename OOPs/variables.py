class Car:
    # //class static var and namespace
    wheels=4
    def __init__(self):
        self.mileage=14
        self.com="BMW"
        # //instance var and instance namespace 
c1=Car()
c2=Car()
c1.mileage=7   #it only change c1 mileage
Car.wheels=5   #it change the value at every place
print(c1.com,c1.mileage,c1.wheels)
print(c2.com,c2.mileage,c2.wheels)