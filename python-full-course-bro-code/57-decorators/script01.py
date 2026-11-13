def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Added fudge")
        func(*args, **kwargs)
    return wrapper

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Added sprinkles")
        func(*args, **kwargs)
          
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavour):
    print(f"{flavour} ice cream")

get_ice_cream("vanilla")