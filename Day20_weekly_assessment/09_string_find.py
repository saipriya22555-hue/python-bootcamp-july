word = input("Enter the string: ")
ch = input("Enter the character: ")

index = word.find(ch)
if index == -1:
    print("Character not found")
else:
    print("Character found at index:", index)
