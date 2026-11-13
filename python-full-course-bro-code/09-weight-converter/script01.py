# Weight converter

weight = float(input("Weight: "))
unit = input("Kilograms or pounds (K or L): ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs"
    print(f"New weight: {round(weight, 1)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kgs"
    print(f"New weight: {round(weight, 1)} {unit}")
else:
    print(f"{unit} not valid")
