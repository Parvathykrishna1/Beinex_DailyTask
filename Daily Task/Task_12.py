"""Task 1
   ======
1) Create a class named Shape. Add an instance method called area. But don't define the method, just raise
NotImplementedError() exception with a suitable message.
2) Make it an abstract base class by inheriting ABC class from the abc module. (To import: from abc import ABC)
Make the area method an abstract method by decorating it with abstractmethod decorator (import this also from 
abc).
3) Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle.
Define constructor for each of them to assign the necessary parameters required for calculating the area.
Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it.
Create an object for each of the subclasses and call the area method on the objects.    """

# from abc import ABC, abstractmethod
# import math


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         raise NotImplementedError(
#             "Oops! Looks like this shape is a mystery! Can't calculate the area until it's defined."
#         )


# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side**2


# class Pentagon(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side**2


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2


# triangle = Triangle(5, 8)
# print("Area of triangle:", triangle.area())

# square = Square(4)
# print("Area of square:", square.area())

# pentagon = Pentagon(6)
# print("Area of pentagon:", pentagon.area())

# circle = Circle(5)
# print("Area of circle:", circle.area())


"""Task 2
   =====
Create a class named Cypher. The purpose of that class is to receive an input string of characters and convert it to
another cypher string. Use a constructor to receive the input. You can also read the input from user. But don’t use
input() inside the constructor.
The class must have a class method to do the string conversion. And an instance method to invoke the classmethod
from within it.
• Use the below conversion logic:
• Iterate over each character in the string, and if the character is a digit increment it by one (0->1, 1-
>2, ... 9 should be replaced with 0)
• if the character is an alphabet then shift the character by 2 positions (use chr() and ord() built-ins for
this) (a->c, b->d, ... y->a, z->b) If the character is in upper case convert it to lower and vice versa
• The returned string must be of same length as the input.
No need to implement the reversing algorithm but will be a plus if available.
1) create an object for the Cypher class with the string.
2) call the instance method, which should internally call the classmethod you prepared for the conversion, pass the
string data to classmethod and do the conversion.
No need to consider special characters for now.
Expected output for the string "ABcD1293Z" is "cdEf2304b"     """


# class Cypher:
#     def __init__(self, input_string):
#         self.input_string = input_string

#     @classmethod
#     def convert(cls, input_string):
#         cypher = ""
#         for char in input_string:
#             if char.isdigit():
#                 cypher += str((int(char) + 1) % 10)
#             elif char.isalpha():
#                 shifted_char = chr((ord(char.lower()) - ord("a") + 2) % 26 + ord("a"))
#                 cypher += (
#                     shifted_char.upper() if char.isupper() else shifted_char.lower()
#                 )
#             else:
#                 cypher += char
#         return cypher

#     def reveal_secret(self):
#         return self.convert(self.input_string)


# input_str = input("Enter the string: ")
# cypher = Cypher(input_str)

# secret_message = cypher.reveal_secret()

# print("Original Message:", input_str)
# print("Secret Cypher:", secret_message)
