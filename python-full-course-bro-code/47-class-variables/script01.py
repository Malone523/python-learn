class Student:

    class_year = 2027
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

    
student1  = Student("Sponge", 22)
student2 = Student("Bob", 32)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

print(Student.class_year)
print(Student.num_students)
