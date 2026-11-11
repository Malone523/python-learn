foods = []
prices = []
total = 0

while True:
    food = input("Food (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Price of {food}: $"))
        foods.append(food)
        total += price

print("---- YOUR CART ----")
for food in foods:
    print(food, end=" ")


print()
print(f"Total is ${total}")