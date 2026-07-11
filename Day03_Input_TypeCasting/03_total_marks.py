python_mark = int(input("Enter Python mark: "))
english_mark = int(input("Enter English mark: "))
maths_mark = int(input("Enter Maths mark: "))
physics_mark = int(input("Enter Physics mark: "))
chemistry_mark = int(input("Enter Chemistry mark: "))
biology_mark = int(input("Enter Biology mark: "))

total = (
    python_mark
    + english_mark
    + maths_mark
    + physics_mark
    + chemistry_mark
    + biology_mark
)

print(f"Total Marks = {total}")
