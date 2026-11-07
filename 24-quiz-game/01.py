# python quiz game

questions = ("Periodic table has X elements: ",
             "X lays the largest egg: ",
             "Most abundant gas in the atmosphere:",
             "The human body has X bones:",
             "This planet is the hottest in the solar system")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C.Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Guess (A, B, C, D): ").upper()
    guesses.append(guess)
    if (guess == answers[question_num]):
        print("Correct")
        score += 1
    else: 
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("--------------------")
print("       ANSWERS      ")
print("--------------------")

print("answers: ", end ="")
for answer in answers:
    print(answer, end= " ")
print()

print("guesses: ", end ="")
for guess in guesses:
    print(guess, end= " ")
print()

print(f"Your score: {score / len(questions) * 100}%")

