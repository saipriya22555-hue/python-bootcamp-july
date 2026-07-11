side = int(input("Enter side of square: "))

length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

area_square = side * side
area_rectangle = length * breadth
area_triangle = (base * height) / 2

print(f"""Area of Square = {area_square}
Area of Rectangle = {area_rectangle}
Area of Triangle = {area_triangle}
""")
