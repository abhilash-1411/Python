class Student:
    school="oxford"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self): 
          #1.instance method
        return (self.m1+self.m2+self.m3)/3
    #a.accessor to get the value
    # def get_m1(self):
        # return self.m1
    # b.mutator to modify the value
    # def set_m1(self,value):
    #     self.m1=value

   #2.class method
    @classmethod
    def getSchool(cls):
        return cls.school
    
    # 3.Static method
    @staticmethod
    def info():
        print("This is a static method")
    

s1=Student(35,66,77)
s2=Student(55,88,99)

print(s1.m1,s1.m2,s1.m3,s1.school)
print(s2.m1,s2.m2,s2.m3,s2.school)

print("The avg of s1 is",s1.avg())
print("The avg of s2 is ",s2.avg())
print(Student.getSchool())
Student.info()
