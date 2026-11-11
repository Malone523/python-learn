word = "APPLE"

letter = input("Guess a letter: ").upper()

if letter in word:
    print(f"There is a {letter}")
else:
    print(F"{letter} not found")