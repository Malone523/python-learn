def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get("street")} {kwargs.get("apt")}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get("street")} {kwargs.get("pobox")}")
    else:
        print(f"{kwargs.get("street")}")
    
    print(f"{kwargs.get("city")} {kwargs.get("state")} {kwargs.get("zip")}")


shipping_label("Dr.", "Sponge", "Bob",
               street = "Fake St.",
               pobox = "PO box #1010",
               apt = 23,
               city = "Detroit",
               state = "MI",
               zip = "921312")