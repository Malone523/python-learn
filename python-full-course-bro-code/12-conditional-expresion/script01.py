num = 5
a = 6
b = 7
age = 24
temp = 30
user_role = "Admin"

print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"
print(result)

max_num = a if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

status = "Adult" if age >= 18 else "Child"
print(status)

weather = "Hot" if temp > 20 else "Cold"
print(weather)

access_level = "Full Access" if user_role == "Admin" else "Limited Access"
print(access_level)