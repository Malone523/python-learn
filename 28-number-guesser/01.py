import random

low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True

print("Python guessing game")
while is_running:
    guess = input(f"Guess {low} and {high}: ")

    if guess.isdigit():
        guess = int(guess)    
        guesses += 1
        
        if guess == answer:
            print("Correct")
            print(f"Number of guesses: {guesses}")
            is_running = False
        elif guess < low or guess > high:
            print("Outside of range")
        elif guess > answer:
            print("Lower")
        else: 
            print("Heigher") 

    
    else: 
        print("Only use numbers")