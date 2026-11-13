class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with the radius of {3.14 * self.radius * self.radius}")
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with the area of {self.width * self.width}")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with the area of {self.width * self.height / 2}")
        super().describe()




circle = Circle(color = "red", is_filled = True, radius = 5)
print(circle.color)
print(circle.is_filled)
print(circle.radius)

square = Square(color = "blue", is_filled= False, width = 10)
print(square.color)
print(square.is_filled)
print(square.width)

triangle = Triangle(color = "white", is_filled= True, width = 2, height = 4)
print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)

circle.describe()
square.describe()
triangle.describe()
