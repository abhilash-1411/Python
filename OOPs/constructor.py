class Computer:
     pass
     def __init__(self):
          self.name ="Abhilash"
          self.age=23
          
     def update(self):
          self.age=25

     def compare(self, other):
          if   self.age==other.age:
               return True
          else:
               return False
c1=Computer()
c2=Computer()

# c1.name="Bablu"
# c1.age=12
c1.update()
if c1.compare(c2):
     print("They are same")
else:
     print("They are different")

print(c1.name,c2.name)
print(c1.age,c2.age)
