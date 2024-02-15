FUNCTIONS – Task-5
1.Write a Python function that calculates the factorial of a given integer. Demonstrate how to call this function with an example.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number:"))
fact = factorial(n)
print("The factorial of ",n," is ",fact,)
  
    
2.Create a function that takes two arguments, a name and an age, and prints a message like "Hello,   [Name]! You are [Age] years old." Call this function with your name and age as arguments.
def f(n,a):
    print("Hello,",n,"! You are",a,"years old.")

name=input("Enter your name:")
age=int(input("Enter your age:"))
f(name,age)

3.Write a Python function to find the maximum of three numbers.
def greatestnum(a,b,c):
    return max(a,b,c)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
maxnum=greatestnum(a,b,c)
print("Maximum of three numbers is",maxnum)


4.Write a Python program to reverse a string
def reverse_string(s):
       return s[::-1]

s=input("Enter the string:")
rev=reverse_string(s)
print("Reverse of",s,"is",rev)


5.Write a Python function that accepts a string and counts the number of upper and lower case letters.
def letters_count(s):
    upper_count = 0
    lower_count = 0
    for i in s:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1    
    print(f"{s} has {upper_count} upper case letters and {lower_count} lower case letters.")

s = input("Enter a string: ")
letters_count(s)


6.Write a Python function that takes a number as a parameter and checks whether the number is prime or not. 
def primenumber(n):
    "Prime number or not"
    for i in range(2,n):
         if(n%i==0):
              print("Given Number is not a prime number")
              break
    else:
        print("Given number is a prime number")
    return

a=int(input("Enter a number"))
primenumber(a)


7.Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
def str_sort(s):
  s1 = s.split('-')
  s1.sort()
  s2 = '-'.join(s1)
  return s2

str = input('Enter a hyphen-separated sequence of words: ')
final_sequence = str_sort(str)
print("Sorted sequence:", final_sequence)


 8.Define a function that accepts 2 values and return its sum, subtraction and multiplication. Using 4 types of functions based on arguments and return type.
def calculator(a, b):
    return a + b, a - b, a * b

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

add, sub, mult = calculator(n1, n2)
print("Sum:", add)
print("Subtraction:", sub)
print("Multiplication:", mult)


9.Define a function that accepts roll number and returns whether the student is present or absent.
def student_attend(roll_no):
    present_list = [22,23,24,55,60,72]
    if roll_no in present_list:
     print("Present")
    else:
     print("Absent")

roll_no = int(input("Enter your roll number:"))
student_attend(roll_no)


10.Define a function that accepts lowercase words and returns uppercase words.
def to_uppercase(str):
 if str.islower():
  return str.upper()
 
s = input("Enter a string in lowercase:")
print(to_uppercase(s))
