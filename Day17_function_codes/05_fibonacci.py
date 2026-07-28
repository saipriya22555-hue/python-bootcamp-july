num = int(input("Enter number of terms: "))

def fibonacci(n):
    first = 0
    second = 1

    for i in range(n):
        print(first, end=" ")

        next_num = first + second
        first = second
        second = next_num

fibonacci(num)
