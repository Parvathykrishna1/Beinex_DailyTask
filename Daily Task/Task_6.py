# FUNCTIONS – Task-6 
# 1.Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
# add = lambda a: a+15
# print(add(3))
# 
# mult = lambda x,y: x*y
# print(mult(2,6))


# 2.Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# def multiply(n):
#     return lambda x:x*n

# r=multiply(3)
# print(r(5))

# r=multiply(4)
# print(r(5))

# r=multiply(5)
# print(r(5))

# 3.Write a Python program to find if a given string starts with a given character using Lambda.
# starts_with = lambda s: True if s.startswith('A') else False 
# print(starts_with('Amazon'))
# print(starts_with('Hello'))

# 4.Write a Python program to extract year, month, date and time using Lambda.
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178

# import datetime
# now = datetime.datetime.now()
# print(now)

# year = lambda x: x.year
# month = lambda x:x.month
# day = lambda x:x.day
# t = lambda x:x.time()

# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))


# 5.Write a Python program to check whether a given string is a number or not using Lambda.
# check_number = lambda s: s.isdigit()

# s = input("Enter a string: ")
# if check_number(s):
#     print("The given string is a number.")
# else:
#     print("The given string is not a number.")

# 6.Write a Python program to create Fibonacci series up to n using Lambda.
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Lambda function to generate Fibonacci series up to n
# Lambda function to generate Fibonacci series up to n
# fibonacci = lambda n: [0, 1] if n == 2 else fibonacci(n - 1) + [fibonacci(n - 1)[-1] + fibonacci(n - 1)[-2]]

# n = int(input("Enter the range: "))
# print("Fibonacci series upto", n, ":")
# print(fibonacci(n))


# 7.Write a Python program to find palindromes in a given list of strings using Lambda.
# is_palindrome = lambda s: s == s[::-1]

# s = ["python", "php", "java", "malayalam", "hello"]

# p = list(filter(is_palindrome, s))
# print("Palindromes in the given list:", p)


# 8.Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
# Original list: [2, 4, 6, 9, 11]
# Given number: 2
# Result:
# 4	8 12 18 22
# 
# l = [1, 2, 3, 4, 5]
# given_number = 2
# multiply = lambda x: x * given_number

# result = list(map(multiply, l))

# print("Original list:", l)
# print("Given number:", given_number)
# print("Result:", result)


# 9.Write a Python program to find the maximum value in a given heterogeneous list using lambda.Original list:
def max_val(l):
    max_val = max(l, key=lambda i: (isinstance(i, int), i))
    return max_val

l = ['Python', 3, 2, 4, 5, 'version']
print("Original list:",l)
print("Maximum values in the  list using lambda:",max_val(l))


# 10.Create a Python module (a separate .py file) that contains a function to calculate the area of a rectangle. Then, in another Python script, import the module and use the function to calculate the area of a rectangle with specific dimensions.
# import area
# length = 5
# width = 6
# A = area.calculate_area(length, width)
# print("Area of the rectangle:", A)

