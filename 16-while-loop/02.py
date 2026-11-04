age = int(input("Age: "))

while age < 0:
    print("Age can not be negative")
    age = int(input("Age: "))

print(f"You are {age} y/o")