num=int(input("Enter number:"))

def odd_or_even(b):
   
    if b % 2 == 0:
        return "even"
    else:
        return "odd"
a=odd_or_even(num)
print(a)
