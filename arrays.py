from array import *

val = array('i',[5,9,8,4,2])

# ------create array from array-----
newArray = array(val.typecode,(a*a for a in val))


# print(val.buffer_info())
# print(val.typecode)
# for i in range(5):
#     print(val[i])

# for i in range(len(val)):
#     print(val[i])

# val = array('u',['a','e','i','o','u'])
# for e in val:
        # print(e)

# print(newArray)


# --Take user input in array-----

arr=array('i',[])

n=int(input("Enter the length of the array "))

for i in range(n):
    x=int(input("Enter the value "))
    arr.append(x)
print(arr)





