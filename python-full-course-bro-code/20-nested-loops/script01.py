rows = int(input("Rows: "))
columns = int(input("Columns: "))
symbol = input("Symbol: ")

for x in range(rows):
    for y in range (columns):
        print(symbol, end = "")
    print()