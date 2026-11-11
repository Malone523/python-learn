principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Principle: "))
    if principle < 0:
        print("Principle can not be < 0")
    else:
        break

while True:
    rate = float(input("Rate: "))
    if rate < 0:
        print("Rate can not be < 0")
    else:
        break

while True:
    time = float(input("Time (Years): "))
    if time < 0:
        print("Time can not be < 0")
    else:
        break

total = principle * pow((1 + rate / 100),time)

print(f"Balance after {time} year/s: ${total:.2f}")