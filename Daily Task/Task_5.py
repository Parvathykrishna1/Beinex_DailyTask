# FUNCTIONS – Task
# 1.	Write a Python function that calculates the factorial of a given integer. Demonstrate how to call this function with an example.
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# n = int(input("Enter a number:"))
# fact = factorial(n)
# print(f"The factorial of {n} is {fact}")
  
    
# 2.	Create a function that takes two arguments, a name and an age, and prints a message like "Hello,   [Name]! You are [Age] years old." Call this function with your name and age as arguments.
# def f(name,age):
#     print(f"Hello, {name}! You are {age} years old.")

# name=input("Enter name:")
# age=int(input("Enter age:"))
# f(name,age)

# 3.	Write a Python function to find the maximum of three numbers.
# def greatestnum(a,b,c):
#     return max(a,b,c)

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# max=greatestnum(a,b,c)
# print(f"Maximum of three numbers is {max}")



# 4.	Write a Python program to reverse a string
# def reverse_string(s):
#        return s[::-1]

# s=input("Enter the string:")
# rev=reverse_string(s)
# print(f"Reverse of {s} is {rev}")

# 5.	Write a Python function that accepts a string and counts the number of upper and lower case letters.
# def letters_count(s):
#     upper_count = 0
#     lower_count = 0
#     for i in s:
#         if i.isupper():
#             upper_count += 1
#         elif i.islower():
#             lower_count += 1    
#     print(f"{s} has {upper_count} upper case letters and {lower_count} lower case letters.")

# s = input("Enter a string: ")
# letters_count(s)



# 6.	Write a Python function that takes a number as a parameter and checks whether the number is prime or not. 
# def primenumber(n):
#     "Prime number or not"
#     for i in range(2,n):
#          if(n%i==0):
#               print("Given Number is not a prime number")
#               break
#     else:
#         print("prime number")
#     return
# 
# a=int(input("Enter a number"))
# primenumber(a)
           
# 7.	Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
# def str_sort(string):
#   b = string.split('-')
#   b.sort()
#   c = '-'.join(b)
#   return c

# s = input('Enter a sequence of colors separated with hyphen: ')
# result = str_sort(s)
# print("Sorted sequence:", result)

# 8.	Define a function that accepts 2 values and return its sum, subtraction and multiplication. Using 4 types of functions based on arguments and return type.
def calculator(a, b):
    return a + b, a - b, a * b

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_result, subtraction_result, multiplication_result = calculator(num1, num2)
print("Sum:", sum_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)


#  9.	Define a function that accepts roll number and returns whether the student is present or absent.
# def student_attnd(roll_no):
#     roll_list = [26,24,55,72,36]
#     if roll_no in roll_list:
#      print("Present")
#     else:
#      print("Absent")

# roll_no = int(input("Enter your roll number:"))
# student_attnd(roll_no)


#  10.	Define a function that accepts lowercase words and returns uppercase words.
# def to_uppercase(str):
#  if str.islower():
#   return str.upper()
 
# s = input("Enter a string in lowercase:")
# print(to_uppercase(s))
