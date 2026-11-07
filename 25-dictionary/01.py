capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get("USA"))

if capitals.get("Japan"):
    print("Capital exists")
else:
    print("Capital does not exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()

keys = capitals.keys()
values = capitals.values()
items = capitals.items()
print(capitals)
print(keys)

for key in capitals.keys():
    print(key)

for key, value in capitals.items():
    print(f"{key} - {value}")
capitals.clear