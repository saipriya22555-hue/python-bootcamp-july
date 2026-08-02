def calculator(a,o,b):
    if o=="+":
        return a + b
    elif o=="-":
        return a-b
    elif o=="*":
        return a * b
    elif o == "/":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"
    
       
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
opr=(input("Enter the operator:"))
result=calculator(num1,opr,num2)
print("result:",result)
