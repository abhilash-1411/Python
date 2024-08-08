def div(a,b):
    return a/b


# decorater
def smart(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    
    return inner

div=smart(div)

result=div(2,4)
print(result)