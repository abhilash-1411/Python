class Computer:
     def config(self):
        print("i5,16gb,1TB")


com1=Computer()
com2=Computer()


# com1.config()
Computer.config(com1)
Computer.config(com2)



# x=9
# print(type(x))       
# a='8'
# print(type(a))
# print(type(comp1))