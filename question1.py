# Swap two variables 
# 1.Using third variable
a=5
b=10
# temp=a
# a=b
# b=temp

# 2.Without using third variable
# a=a+b 
# b=a-b
# a=a-b

# -----this take extra bit

# Step 1: a becomes a XOR b
# a = a ^ b  # a now holds 5 ^ 10

# Step 2: b becomes a XOR b (which is (a XOR b) XOR b = a)
# b = a ^ b  # b now holds (5 ^ 10) ^ 10, which simplifies to 5

# Step 3: a becomes a XOR b (which is (a XOR b) XOR a = b)
# a = a ^ b # a now holds (5 ^ 10) ^ 5, which simplifies to 10

# 3 python functions

a,b = b,a

print(a, b)  
