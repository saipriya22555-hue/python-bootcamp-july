num=int(input("Enter number:"))

def factorial(b):
    fact = 1
    for i in range(1,b+1):
       fact= i*fact
    return fact
a=factorial(num)
print(a)
