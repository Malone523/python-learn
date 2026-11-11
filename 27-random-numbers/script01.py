import random

# print(help(random))

low = 1
heigh = 100
options = ("rock", "paper", "scissor")
cards = ["2", "3", "4", "5" "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, heigh)
# number = random.random()
# option = random.choice(options)
random.shuffle(cards)

print(cards)