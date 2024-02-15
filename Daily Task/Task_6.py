FUNCTIONS – Task-6 
1.Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
add = lambda a: a+15
n=int(input("Enter a number:"))
result = add(n)
print("Given numner:",n)
print("Given number after adding 15:",result)


mult = lambda x,y: x*y
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
multiply = mult(n1,n2)
print("Multiplication of",n1,"and",n2,"is",multiply)


2.Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def multiply(x):
    unknown_num = 4
    return lambda x: x * unknown_num

n = int(input("Enter a number: "))
mult = multiply(n)
result = mult(n)
print("Given number:", n)
print("Final result after multiplied with an unknown number:", result)

3.Write a Python program to find if a given string starts with a given character using Lambda.
starts_with = lambda s: True if s.startswith('A') else False 
print(starts_with('Amazon'))
print(starts_with('Hello'))
print(starts_with('python'))

4.Write a Python program to extract year, month, date and time using Lambda.
Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178

import datetime
now = datetime.datetime.now()
print(now)

year = lambda x: x.year
month = lambda x:x.month
day = lambda x:x.day
tm = lambda x:x.time()

print("Year:",year(now))
print("Month:"month(now))
print("Day:"day(now))
print("Time:"tm(now))


5.Write a Python program to check whether a given string is a number or not using Lambda.
check_number = lambda s: s.isdigit()

s = input("Enter a string: ")
if check_number(s):
    print("The given string is a number.")
else:
    print("The given string is not a number.")

6.Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
 
fibonacci_series = lambda n: [0, 1] if n == 2 else fibonacci_series(n - 1) + [fibonacci_series(n - 1)[-1] + fibonacci_series(n - 1)[-2]]

n = int(input("Enter the range: "))
print("Fibonacci series upto", n, ":")
print(fibonacci_series(n))


7.Write a Python program to find palindromes in a given list of strings using Lambda.
is_palindrome = lambda s: s == s[::-1]

s = ["python", "php", "java", "malayalam", "hello"]

p = list(filter(is_palindrome, s))
print("Palindromes in the given list:", p)


8.Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
Original list: [2, 4, 6, 9, 11]
Given number: 2
Result:
4 8 12 18 22
 
multiply = lambda x: x * given_number

l = [1, 2, 3, 4, 5]        
given_number = int(input("Enter a number that multiplied with each number in a list:"))            
result = list(map(multiply, l))
print("Original list:", l)
print("Given number:", given_number)
print("Result:", result)


9.Write a Python program to find the maximum value in a given heterogeneous list using lambda.Original list:
def max_val(l):
    max_val = max(l, key=lambda i: (isinstance(i, int), i))
    return max_val

l = ['Python', 3, 2, 4, 5, 'version']
print("Original list:",l)
print("Maximum values in the  list using lambda:",max_val(l))


10.Create a Python module (a separate .py file) that contains a function to calculate the area of a rectangle. Then, in another Python script, import the module and use the function to calculate the area of a rectangle with specific dimensions.
#area.py module is used in this code
import area
length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
A = area.calculate_area(length, width)
print("Area of the rectangle:", A)

