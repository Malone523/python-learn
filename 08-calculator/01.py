# Calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    print(f"sum = {round(num1 + num2, 3)}")
elif operator == "-":
    print(f"dif = {round(num1 - num2, 3)}")
elif operator == "/":
    print(f"div = {round(num1 / num2, 3)}")
elif operator == "*":
    print(f"mult = {round(num1 * num2, 3)}")
else:
    print(f"{operator} not included")