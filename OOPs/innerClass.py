class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        # create object inside
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student("abhi",21)
s2=Student("rbhi",22)

# print(s1.name,s1.rollno)
s1.show()
# s2.show()
lap1=s1.lap
lap2=s2.lap

# create object outside
# lap1=Student.Laptop()

print(id(lap1),id(lap2))