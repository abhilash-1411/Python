from numpy import *

arr=array([
    [1,2,3,5,7,9],
    [4,5,6,2,4,9]
])

# print(arr)
# print(arr.dtype)    # gives data type
# print(arr.ndim)   #give dimension or bole to degree
# print(arr.shape)  # give shape bole toh no of row and cols
# print(arr.size)  # give size total elements

# ---convert 2d to 1d
arr1 =arr.flatten()
# print(arr1)

# convert 1d to 3d
arr2=arr1.reshape(3,4)
# print(arr2)

arr3=arr1.reshape(2,2,3)
# print(arr3)

arr4=array([
    [1,2,3,4],
    [5,6,7,8]
])
# convert to matrix 
# m=matrix(arr4)
# print(m)

# another way to create matrix
m1=matrix('1,2,3;4,5,6;7,8,9')
m2=matrix('1,4,3;4,3,6;7,8,7')
# print(m)
# print(diagonal(m))
# print(m.min())
# print(m.max())

# add two matrices
m3=m1+m2
print(m3)

# multiplication
m4=m1*m2
print(m4)
