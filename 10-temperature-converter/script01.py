unit = input("Celcius or Fahrenhite (C/F): ")
temp = float(input("Temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 +32, 1)
    print(f"Temperature in Fahrenheit is: {temp}")
elif unit == "F":
    temp = round((temp-32) * 5 / 9, 1)
    print(f"Temperature in Celcius is: {temp}")
else:
    print(f"{unit} nod valid")