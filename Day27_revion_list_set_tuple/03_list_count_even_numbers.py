numbers = [15, 20, 35, 40, 55, 60]

count = 0

for i in numbers:
    if i % 2 == 0:
        count = count + 1
        print(i)

print("Even count:", count)
