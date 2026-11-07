dictionary = {"A": 1,
              "B": 2,
              "C": 3}

for key in dictionary.keys():
    print(key, end= " ")
print()
    
for value in dictionary.values():
    print(value, end = " ")
print()
    
for item in dictionary.items():
    print(item, end= " ")
print()

for key, value in dictionary.items():
    print(f"{key} - {value}", end= " ")
