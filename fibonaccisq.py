def fibonacci(n):
    a=0
    b=1
    if n==1:
       print(a)
    if n==0:
      print(b)
    else:
     for i in range(2,n):
      c=a+b
      a=b
      b=c
    print(c)


fibonacci(8)