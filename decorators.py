import time

# def div(a,b):
#     return a/b


# decorater
# def smart(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
    
#     return inner

# div=smart(div)

# result=div(2,4)
# print(result)

def timer(function):
     def wrapper(*args, **kwargs):
          start=time.time()
          result=function(*args, **kwargs)
          end=time.time()
          print(f"{function.__name__} ran in {end-start} seconds")
          return result
     return wrapper



@timer
def example_function(n):
     time.sleep(n)

example_function(2)