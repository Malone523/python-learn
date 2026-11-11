students = {"Sponge", "Bob"}

student = input("Enter student name:").capitalize()

if student not in students:
    print(f"{student} not fount")
else:
    print(f"{student} is a student")