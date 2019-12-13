# class: blueprint for creating ne wobjects
# object: instance of a class


class Point:
    # class level attrbutes, and it is shared accross all the objects (instance) of that class.
    default_color = "red"

    # self: reference to the current Point object
    # x, y --> instanced attributes
    # instance methods. We need an object to call it.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def draw(self):
        print(f"Draw: {self.x}, {self.y}")

    # class method
    @classmethod  # decorator
    def zero(cls):
        return cls(0, 0)


point = Point(1, 2)
print(point)
point.draw()
print(type(point))
print(isinstance(point, Point))

Point.default_color = "orange"  # class attribute

# instance attributes. Attributes are dynamic
point.z = 4

print(point.default_color)
print(Point.default_color)

new_point = Point.zero()
print(new_point.draw())

point2 = Point(1, 2)
print(point == point2)
