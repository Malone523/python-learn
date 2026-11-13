class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)

dog.speak()
cat.sleep()
mouse.eat()