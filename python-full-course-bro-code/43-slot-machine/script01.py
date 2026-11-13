import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    results = [random.choice(symbols) for _ in range(3)]
    return results

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "🍒":
                return bet * 3
            case "🍉":
                return bet * 4
            case "🍋":
                return bet * 5
            case "🔔":
                return bet  * 10
            case "⭐":
                return bet * 20
    return 0



def main():
    balance = 100

    print("*************************")
    print("Welcome to python slots ")
    print("Symbols 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    while balance > 0:
        print(f"Current balance: {balance}")

        bet = input("Bet ammount: ")
        if not bet.isdigit():
            print("Invalid input")
            continue
        bet = int(bet)

        if bet > balance:
            print("Insuficient funds")
            continue
        if bet <= 0:
            print("Invalid ammount")
            continue

        balance -= bet
        
        row = spin_row()
        print("Spinining...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost")

        balance += payout

        play_again = input("Play again (Y/N): ").upper()
        if not play_again == "Y":
            break

    print("*************************")
    print(f"Final balance: {balance}")
    print("*************************")

if __name__ == "__main__":
    main()