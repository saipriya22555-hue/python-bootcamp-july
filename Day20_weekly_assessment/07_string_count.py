word=input("Enter the string:")
count=0
for ch in word:
    if ch in "aeiouAEIOU":
        count=count+1
        print(ch,end="")
print()

print("total numbers of vowels:",count)
        
