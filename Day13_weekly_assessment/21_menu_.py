while True:
    print(f"""====Number Utility Menu =====
1. Multiplication Table
2. Even Numbers
3. Odd Numbers
4. Exit""")
    choice=int(input("Enter your Choice:"))
    if choice==1:
        num=int(input("enter the number:"))
        for i in range(1,11):
            print(num,"*",i,"=",num*i)
    elif choice==2:
        for i in range(2,21,2):
            print(i)
    elif choice==3:
         for i in range(1,21,2):
             print(i)
             
    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice! Please try again.")
