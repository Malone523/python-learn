# Exercise 2 Shopping Cart Program

item = str(input("Item: "))
price = float(input("Price: "))
quantity = int(input("Quantity: "))
total = price * quantity

print(f"You bought {quantity} x {item}/s")
print(f"Total is: ${total}")