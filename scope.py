a=10
print(id(a))
b=15

def scope():
   a=15
   x=globals()['a']
   print(id(x))
   print("inside",a)
   print("inside x",x)
   globals()['a']=9

scope()
print("outside",a)