# validate input
# 1. < 12 characters
# 2. no space
# 3. no digits


username = input("Username: ")

if len(username) > 12:
    print("Username too long")
elif not username.find(" ") == -1:
    print("Username can not have spaces")
elif not username.isalpha():
    print("Username can only have letters")
else:
    print(f"Welcome {username}")