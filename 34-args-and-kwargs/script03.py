def print_adress(**kwargs):
    for key, value in kwargs.items():
        print (f"{key}: {value}")

print_adress(street = "Spongebob St.", 
             city = "Detroit", 
             state = "MI", 
             zip = "54321",
             apt = 100)