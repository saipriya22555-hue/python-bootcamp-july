file=open("students.txt","r")

data=file.readlines()
count=len(data)
print("Number of students:",count)
file.close()
