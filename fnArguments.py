# def update(x):
#     print(id(x))
#     x=8
#     print(id(x))
#     print("x",x)
# a=10
# print("a id",id(a))
# update(a)
# print("a",a)


# //Types of arguments
# def person(name,age):
#     print(name)
#     print(age)

# person("navin",28)

# variable parameter
def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
# sum(5,6,7,9)

#keyworded variable length argument

def person(name,**data):
    print(name)
    # print(data)
    for i,j in data.items():
        print(i,j)

person("abhi",age=23,mob=656576,city="Indore")