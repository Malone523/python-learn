fruits = ["apple", "orange", "banana"]

print(fruits[1])
fruits[1] = "pineapple"
fruits.append("coconut")
fruits.remove("apple")
fruits.insert(0, "ah")
fruits.sort()
fruits.reverse()

print(fruits.index("banana"))
print(fruits.count("banana"))

for fruit in fruits:
    print(fruit)
print(len(fruits))
print("coconut" in fruits)

fruits.clear()
# print(dir(fruits))
# print(help(fruits))

