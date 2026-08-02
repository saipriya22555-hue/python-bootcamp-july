def odd_even(num):
    if num % 2 == 0:
        return "even"
    else :
        return "odd"
a=int(input("Enter the number:"))
result=odd_even(a)
print("The given number is :",result)
