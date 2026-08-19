file = open("student.txt", "w")
file.write("Name: Sai\nCollege: Sri Meenakshi college Madurai\nCourse: B.Sc Computer Science\n") 
file.close()


file=open("student.txt","a")
file.write("Age:19\nDepartment: Computer Science")
file.close()

with open("student.txt", "r") as file:
    data = file.read()

print(data)
