string = input("Enter the string: ")

count = 0

for ch in string:
    if ch in "aeiouAEIOU":
        count = count + 1
        print(ch, end=" ")
print()

print("Number of vowels:", count)
