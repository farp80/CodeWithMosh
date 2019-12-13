# method override ==> super.__init__() --> to extend the method of the base class
# Shift + Alt + down Arrow
from abc import ABC, abstractmethod
from collections import namedtuple

# --> this is done for classes that contain just dats no logic. Unmutuable.
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)  # keyword arguments
p2 = Point(x=1, y=2)
print(p1 == p2)


class Animal:
    def __init__(self):
        print("Animal")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):  # it overrides the base class constructor
        super().__init__()
        print("Mammal")
        self.height = 1

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


class Shark(Fish, Animal):
    pass  # it does not do anything, we cannot have a empty class in Python. It is bad, too many level is bad


fish = Fish()
print(fish.eat())
print(isinstance(fish, Animal))  # object is the base class of everything.

o = object()
print(issubclass(Mammal, Animal))

mammal = Mammal()
print(mammal.age)

# *** GOOD INHERITANCE LEVEL ******


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.open = False

    def open(self):
        if self.open:
            raise InvalidOperationError("Stream is open")
        self.open = True

    def close(self):
        if not self.open:
            raise InvalidOperationError("Stream is already closed")
        self.open = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading form File")


class NetworkStream(Stream):
    def read(self):
        print("Reading form Network")


class MemoryStream(Stream):
    def read(self):
        print("Memory Stream")


#stream = Stream()
# stream.open()

ms = MemoryStream()
ms.read()
