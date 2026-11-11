from car import Car

car1 = Car("Maserati", 2020, "red", False)
car2 = Car("Mustang", 2012, "yellow", True)
car3 = Car("BMW", 2022, "black", True)


print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car2.stop()
car3.describe()
