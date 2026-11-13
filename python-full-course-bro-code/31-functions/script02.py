def display_invoice(username, ammount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${ammount:.2f} is due: {due_date}")
    print()

display_invoice("Yo", 50.25, "01/01")