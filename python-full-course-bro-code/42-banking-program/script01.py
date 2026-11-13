def show_balance(balance):
    print("***************")
    print(f"Your balance is ${balance}")
    print("***************")

def deposit():
    print("***************")
    ammount = float(input("How much: "))
    print("***************")
    if ammount < 0:
        print("***************")
        print("Invalid ammount")
        print("***************")
        return 0
    else:
        return ammount;

def withdraw(balance):
    print("***************")
    ammount = float(input("How much: "))
    print("***************")
    if ammount < 0:
        print("***************")
        print("Invalid ammount")
        print("***************")
        return 0
    elif ammount > balance:
        print("***************")
        print("Insuficient funds")
        print("***************")
        return 0
    else:
        return ammount;


def main():    
    balance = 0
    is_running = True

    while is_running:
        print("***************")
        print("Banking Program")
        print("***************")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("***************")
        choice = input("Choice (1 - 4): ")
        print("***************")
        
        match choice:
            case "1": 
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print("Invalid input")
        print()
    print("***************")
    print("Have a nice day")
    print("***************")


if __name__ == "__main__":
    main()