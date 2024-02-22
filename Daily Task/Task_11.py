#                                   OOPS -   TASK
# 1)Write a program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object.

# class Students:
#     def __init__(self, name, age, grade):
#         self.name = name 
#         self.age = age
#         self.grade = grade

# s1 = Students("Anu", "25", "5th")
# s2 = Students("Sonu", "24", "7th")
# s3 = Students("Vinu", "24", "5th")   

# print("Student 1:")
# print("Name:", s1.name)
# print("Age:", s1.age)
# print("Grade:", s1.grade)

# print("\nStudent 2:")
# print("Name:", s2.name)
# print("Age:", s2.age)
# print("Grade:", s2.grade)

# print("\nStudent 3:")
# print("Name:", s3.name)
# print("Age:", s3.age)
# print("Grade:", s3.grade)
        

# 2)Write a program that prints the class name using its object.

# class Employee:
#     pass

# obj = Employee()
# print(obj.__class__.__name__)


# 3)Write a Python class, Square, and define two methods that return the square area and perimeter.

# class Square:
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side
    
#     def perimeter(self):
#         return 4 * self.side
    
# square = Square(6)

# print(f"Area: {square.area()}") 
# print(f"Perimeter: {square.perimeter()}") 


# 4) Write a program to create a child class Teacher that will inherit the properties from the parent class Staff.
#     attributes need for staff : role,department, salary
#     attributes need for teacher: name,age
#     method in  staff : def print_details()

#     output expected -
#         Name:  Raj
#         Age:  28
#         Role: Teacher
#         Department: Science

# class Staff:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def print_details(self):
#         print("Role: ",self.role)
#         print("Department: ",self.department)
#         print("Salary: ",self.salary)
        
# class Teacher(Staff):
#     def __init__(self, name, age, role, department, salary):
#         super().__init__(role, department, salary)
#         self.name = name
#         self.age = age

#     def print_details(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         super().print_details() 

# teacher = Teacher("Parvathy", 24, "Teacher", "Civil", "200000")
# teacher.print_details()
    

# #5,6,7 related Questions
# 5) Create a class named Student with name, score as instance attributes. Assign values to both of these attributes using a constructor.
# Create 2 Student objects. And also define a method called 'display' in the Student class - which, when called should print the name and score of the student.
 
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def display(self):
#         print(f"Name: {self.name}\nScore: {self.score}")

# s1 = Student("Ami", 85)
# s2 = Student("Alice", 40)


# print("Student 1 Details:")
# s1.display()
# print("\nStudent 2 Details:")
# s2.display()


# 6) Extend the above solution and add another instance attribute called grade (should be string). Assign value to grade from within the constructor.
# The value should not be taken from user input.
# Instead use the following conditions and assign values to grade by using the value of score.
# grade = A+ if score >=90
# grade = A if score >=80 and <90
# grade = B+ if score >=70 and <80
# and so on.
# if score is below 40 then grade should be "FAILED"

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         self.grade = self.calculate_grade()

#     def calculate_grade(self):
#         grades = {90: "A+", 80: "A", 70: "B+", 60: "B", 50: "C", 40: "D"}
#         for mini_score, grade in grades.items():
#             if self.score >= mini_score:
#                 return grade
#         return "FAILED"

#     def display(self):
#         print("Name:", self.name)
#         print("Score:", self.score)
#         print("Grade:", self.grade)

# s1 = Student("Ami", 85)
# s2 = Student("Alice", 40)

# print("Student 1 Details:")
# s1.display()
# print("\nStudent 2 Details:")
# s2.display()


# 7) Extend the above solution again and add another instance method called 'as_dict'. 
# The method should return a dictionary with the data of the student. It should contain
#  'name', 'score', 'grade', keys and their respective values.

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         self.grade = self.calculate_grade()

#     def calculate_grade(self):
#         grades = {90: "A+", 80: "A", 70: "B+", 60: "B", 50: "C", 40: "D"}
#         for mini_score, grade in grades.items():
#             if self.score >= mini_score:
#                 return grade
#         return "FAILED"

#     def display(self):
#         print("Name:", self.name)
#         print("Score:", self.score)
#         print("Grade:", self.grade)

#     def as_dict(self):
#         return {"Name": self.name, "Score": self.score, "Grade": self.grade}

# s1 = Student("Anju", 85)
# s2 = Student("Alan", 40)

# print("Student 1 Details:")
# s1.display()
# print("\nStudent 2 Details:")
# s2.display()

# print("\nStudent 1:", s1.as_dict())
# print("\nStudent 2:", s2.as_dict())

# 8) show class method, static method and instance method with simple example.

# class MathOperation:
#     @staticmethod
#     def add(x, y):
#         return x + y
    
#     @classmethod
#     def multiply(cls, x, y):
#         return cls.add(x, y) * cls.add(x, y)
    
#     def substract(self, x, y):
#         return x - y
    
# print("Addition using static method:", MathOperation.add(4, 3))
# print("Multiplication using class method:", MathOperation.multiply(2, 1))

# obj = MathOperation()
# print("Subtraction using instance method:", obj.substract(7, 3))


