grades = {"Sponge": "A",
          "Bob": "C"}

student = input("Enter student name: ").capitalize()

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not found")