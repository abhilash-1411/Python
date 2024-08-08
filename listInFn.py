lst=[1,23,4,5,6,6,7,7,8,9]
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
        
    return even,odd

even,odd=count(lst)

print ("Even:{} and Odd:{}".format(even,odd))