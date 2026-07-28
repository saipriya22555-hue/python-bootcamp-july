num=int(input("Enter number:"))

def multiplication_table(b):
    for i in range(1,11):
        print(i,"*",b,"=",i*b)

multiplication_table(num)
