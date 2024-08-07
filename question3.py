# check if number is prime or not

x=int(input("Enter the number "))
is_prime=1
if x<=1:
    is_prime=0
for i in range(2,x):
    if x%i==0:
        is_prime=0
        break


if is_prime:
    print("Number is prime")
else:
    print("Number is not prime")