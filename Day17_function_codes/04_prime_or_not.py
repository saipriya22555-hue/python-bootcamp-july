num = int(input("Enter number: "))

def fibo(b):
    a=b-1
    print(a)
    c=a+b
    a=temp
    b=a
    temp=b
    return c
    

ans = fibo(num)
print(ans)
