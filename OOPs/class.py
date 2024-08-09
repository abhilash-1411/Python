class Computer:
    #  for every object it is called automatically
     def __init__(self,cpu,ram):
         self.cpu = cpu
         self.ram = ram
        
     def config(self):
        print("config is ",self.cpu,self.ram)


com1=Computer('i5',16)
com2=Computer('Ryzen',8)


com1.config()
com2.config()
# Computer.config(com1)
# Computer.config(com2)



# x=9
# print(type(x))       
# a='8'
# print(type(a))
# print(type(comp1))