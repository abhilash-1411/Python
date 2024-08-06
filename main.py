# print("Hello world!")
# print(2+3)
# print('c:\docs\navin')  \n converts to new line
# print(r'c:\docs\navin')   we write r means raw data 

# Variables in python
x=2
y=3
# print(x+y)
name='youtube'
# print(name+'rocks')
# print(name[0])
# print(name[0:2]) 2--where to stop exlude 2
# print(name[-1])  start from peeche

# print(name[1:4])
# print(name[1:]) till the end 
# print(name[:4])

# List 
nums=[12,34,2,3,1,2,3]
# print(nums)
names=['ram', 'laxman', 'seeta']
# print(names)

values=[1.5,23,'navin']
# print('The values are ', values)

mil=[nums,names]
# print(mil)

nums.append(7)
# print('THe minimum value is',min(nums))
# print('THe max value is',max(nums))
# print('The sum of nums is',sum(nums))


nums.insert(2,77)
# print(nums)

# nums.remove(77)  remove by number
# print(nums)

nums.pop(3)  
# print(nums)

# del[nums[2:4]]  used to delete multiple values 
# print(nums)


# TUPLES--are immutable

tup=(12,13,134,2,4)
# print(tup[1])

set={1,2,3,6,5,6,7,7}
# print(set)

# DICTIONARY

data={
    1:'John',
    2:"Jon",
    4:'Harsh'
}
# print(data[4])
# print(data.get(3,'Not found'))

keys=['john','jon','harsh']
values=['Python','java','Cpp']

data1=dict(zip(keys,values))
# print(data1)

# Add entry
data1['Nandu']='C sharp'
# print(data1)

# Del entry
del data1['harsh']
# print(data1)

# Now uisng list and dict inside dictionary

prog={
    'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}
}
# print(prog)
# print(prog['Python'][1])
# print(prog['Java']['JEE'])

# More on variables
num=5
# print(id(num))  id gives as address of variable
# a=10
# b=a
# print(a)
# print("Address of a ",id(a))
# print(b)
# print("Address of b ",id(b))
# print("Address of 10 ",id(10))

# Data types
a=5
b=6
c=complex(a,b)
# print(c)

# range 
range(10)
# print(range(10))
# print(list(range(10)))
# print(list(range(4,10,2))) 4 se 10 tk 2 ka difference 
# print(type(range(10)))


# Number System 
# Decimal to binary
print(bin(25))
print(bin(12))
# Binary to decimal
print(0b0101)
# octal
print(oct(25))
# hexadecimal
print(hex(25))
