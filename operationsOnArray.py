from numpy import *

arr1 =array([1,2,3,4,5])
# arr2 =array([6,7,8,4,5])
# ----Add to each element----
# arr3=arr1+arr2
# print(arr3)
# print(sin(arr1))
# print(cos(arr1))
# print(log(arr1))
# print(sqrt(arr1))
# print(min(arr1))
# print(max(arr1))

# print(concatenate([arr1,arr2]))
#  copying an array 
arr3 = arr1
# print(arr3)

# Having same address

# print(id(arr3))


print(arr1)
print(id(arr1))
# shallow copy 

# arr4=arr1.view()
# print(arr4)
# print(id(arr4))

# Deep copy
arr5=arr1.copy()
arr1[1]=7
print(arr5)
print(id(arr5))