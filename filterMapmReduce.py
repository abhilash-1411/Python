from functools import reduce
nums=[1,2,3,4,5,6,78,5,4,4]

#-------filter 
evens =list(filter(lambda n:n%2==0,nums))
print(evens)

#-------Map 
doubles=list(map(lambda n:2*n,evens))
print(doubles)

# ---------Reduce 
sum=reduce(lambda a,b:a+b,doubles)
print(sum)
