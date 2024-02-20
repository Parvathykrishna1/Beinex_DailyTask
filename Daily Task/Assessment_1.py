# PYTHON INTERNSHIP TASK – ASSESSMENT 1
""" (1) write a single program to handle the following arithmetic operations for addition, subtraction, 
       multiplication , division, floor division,modulus and Exponentiation."""

# x = float(input("Enter the first number: "))
# y = float(input("Enter the second number: "))
# op = input("Enter operator (+, -, *, /, //, %, **): ")

# if op == '+':
#     print("Result:", x + y)
# elif op == '-':
#     print("Result:", x - y)
# elif op == '*':
#     print("Result:", x * y)
# elif op == '/':
#     if y != 0:
#         print("Result:", x / y)
#     else:
#         print("Error: Division by zero")
# elif op == '//':
#     if y != 0:
#         print("Result:", x // y)
#     else:
#         print("Error: Division by zero")
# elif op == '%':
#     if y != 0:
#         print("Result:", x % y)
#     else:
#         print("Error: Division by zero")
# elif op == '**':
#     print("Result:", x ** y)
# else:
#     print("Error: Invalid operator.")


""" (2)Write a program to check the validity of a password. Primary conditions for password validation:
    - minimum 8 charecters
    - The alphabet must be between [a-z]
    - At least one alphabet should be of Upper Case [A-Z]
    - At least 1 number or digit between [0-9].
    - At least 1 character from [ _ or @ or $ ].
    Examples:
    Input : R@m@_f0rtu9e$
    Output : Valid Password
    Input : Rama_fortune$
    Output : Invalid Password
    Explanation: Number is missing
    Input : Rama#fortu9e 
    Output : Invalid Password
    Explanation: Must consist from _ or @ or $.    """

# password = input("Enter the password:")
# if (len(password) >= 8 and any(i.isupper for i in password) and 
#     any(i.islower for i in password) and any(i.isdigit for i in password) and
#     any(i in ['_', '@', '$'] for i in password)):
#     print("Valid Password")
# else:
#     print("Error: Invalid Password!")    


"""(3) print the following patterns:
    a)
    0
    0 0
    0 0 0
    0 0 0 0    """
    
# for i in range(1, 5):
#     print(" 0 " * i)

"""b)
    *
  * * *
 * * * * *
* * * * * * *   """

# num_rows = 4
# for i in range(1,num_rows+1):
#     print(" " * (num_rows - i) + "* " * (2 * i - 1))


'''c)
    0
    1 1
    2 2 2
    3 3 3 3
    4 4 4 4 4
    5 5 5 5 5 5  '''

# for i in range(0,6):
#     print((str(i) + ' ') * (i + 1))

"""d)
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5   """

# for i in range(1, 6):
#     print(' '.join(str(j) for j in range(1, i+1)))

'''e)
    * * * * * *
    * * * * *
    * * * *
    * * * 
    * *
    *        '''

# for i in range(6, 0, -1):
#     print(' * ' * i )

"""f)
    @ @ @ @ @ @ @
    @ @ @ @ @ @ @
    @ @ @ @ @ @ @
    @ @ @ @ @ @ @     """

# for i in range(1, 5):
#     print(' @ ' *7)


#(4) Write a Python program to perform matrix multiplication using lists of lists.

# def matrix_multiplication(mat1, mat2):
#     if len(mat1[0]) != len(mat2):
#         return "Matrix multiplication is not possible."
    
#     result = [[sum(mat1[i][j] * mat2[j][k] for j in range(len(mat2)))
#                for k in range(len(mat2[0]))] for i in range(len(mat1))]
#     return result

# matrix1 = [[1, 0],
#            [0, 1]]

# matrix2 = [[2, 0],
#            [0, 1]]

# result = matrix_multiplication(matrix1, matrix2)
# print("Result of Matrix multiplication:",result)


#(5) Write a Python program to implement a stack using a list.(push and pop)

# stack = []

# def push(item):
#     stack.append(item)
#     print("Pushed:", item)

# def pop():
#     if len(stack) > 0:
#         item = stack.pop()
#         return "Popped:", item
#     else:
#         print("Stack is empty")

# push(6)
# push(1)
# push(3)
# push(10)
# print("stack after push operation:",stack)

# pop()
# print("Stack after pop operation",stack)
  

#(6) Write a Python program to implement a queue using a list.(enqueue and dequeue)

# queue = []

# def enqueue(item):
#     queue.append(item)
#     print(f"Enqueued: {item}")

# def dequeue():
#     if queue:
#         item = queue.pop(0)
#         print(f"Dequeued: {item}")
#     else:
#         print("Queue is empty")

# enqueue(1)
# enqueue(2)
# enqueue(3)
# print("Queue after enqeue operation:",queue)

# dequeue()
# dequeue()
# print("Queue after dequene operation:",queue)



#(7) Write a Python program to implement a binary search on a sorted list.

# sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
# element = int(input("Enter the element:"))

# left, right = 0, len(sorted_list) - 1
# found = False

# while left <= right:
#     middle = left + (right - left) // 2
#     if sorted_list[middle] == element:
#         print(f"Element found at index {middle}")
#         found = True
#         break
#     elif sorted_list[middle] < element:
#         left = middle + 1
#     else:
#         right = middle - 1

# if not found:
#     print("Element not found")


#(8) Write a Python program to reverse a list.

# list1 = [5, 6, 7, 8, 9, 10]
# print("Reversed List:", list1[::-1])

#(9) Write a Python program to count the occurrences of an element in a list.

# list1 = [1, 2, 5, 8, 2, 8, 7, 2]
# element = int(input("Enter an element: "))

# element_count = lambda list1, element: list1.count(element) if element in list1 else "Element not found in the list."

# c = element_count(list1, element)
# print(f"Count of {element} in the given list: {c}")


#(10) Write a Python program to remove duplicates from a list.

# list1 = [1, 2, 5, 8, 2, 8, 7, 2]
# new_list = []

# for i in list1:
#     if i not in new_list:
#         new_list.append(i)
# print("List after removes all the duplicates:", new_list)


#(11) Write a Python program to find the intersection of two lists.

# list1 = [2, 2, 3, 4, 5]
# list2 = [4, 5, 1, 7, 8]

# intersection_list = [x for x in list1 if x in list2]
# print("Intersection List:", intersection_list)


#(12) Write a Python program to flatten a nested list.([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6])

# def flatten_list(list1):
#     for i in list1:
#         if isinstance(i, list):
#             flatten_list(i)
#         else:
#             flat_list.append(i)

# nested_list = [["hello", 2, [10, 4]], [1, 2], [7, [8, 9]]]
# flat_list = []
# flatten_list(nested_list)
# print("Flattened List:", flat_list)


#(13) Write a Python program to check if a string contains only digits.("12345" -->True)

# string = input("Enter a string:")
# print("String contains only digits:",string.isdigit())


#(14) Write a Python program to check if a given year is a leap year.

# year = int(input("Enter the year:"))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a Leap Year")
# else:
#     print("Not a Leap Year")


#(15) Write a Python program to check if a string is an anagram of another string.("listen", "silent")

# string1 = input("Enter the first string:")
# string2 = input("Enter the second string:")

# string1 = string1.lower().replace(" ", "")
# string2 = string2.lower().replace(" ", "")

# if len(string1) != len(string2):
#     print("The strings are not anagrams.")
# else:
#     if sorted(string1) == sorted(string2):
#         print("The strings are anagrams.")
#     else:
#         print("The strings are not anagrams.")


#(16) Write a Python program to merge two sorted lists into a single sorted list.

# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 4, 6, 8, 10]

# merged_list = sorted(list1 + list2)
# print("Merged sorted list:", merged_list)

#(17) Write a Python program to find the sum of all even numbers in a list.

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_sum = sum(n for n in num if n % 2 == 0)
# print("Sum of all even numbers in given list:", even_sum)

#(18) Write a Python program to find the second largest number in a list.

# list1 = [59, 43, 34, 89, 0, 23]

# sec_largest = sorted(list1)[-2]
# print("The second largest number in given list:", sec_largest)

#(19) Write a Python program to count the number of vowels in a string.

# str = input("Enter a string:")

# num_vowels = sum(1 for i in str if i.lower() in 'aeiou')
# print("Number of vowels in the string:", num_vowels)

#(20) Write a Python program to remove all occurrences of a given element from a list.

# list1 = [1, 2, 3, 4, 3, 6]
# element = int(input("Enter the element to be removed: "))

# if element in list1:
#     list1 = [x for x in list1 if x != element]
#     print("Updated list after removing element:", list1)
# else:
#     print("Element not found in the list.")


#(21) Write a Python program to remove all whitespace characters from a string.

# string = input("Enter a string to remove all the whitespace:")
# new_string = ''.join(x for x in string if x != ' ')
# print("New String after removing whitespace:", new_string)

#(22) Write a Python program to check if a given number is a perfect number.

# n = int(input("Enter a number:"))
# temp = sum(i for i in range(1, n) if n % i == 0)

# if temp == n:
#     print("The number is a Perfect number")
# else:
#     print("The number is not a Perfect number")


#(23) Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.(gcd(48, 60)=12)

# a = int(input("Enter a number:"))
# b = int(input("Enter another number:"))

# gcd = lambda a, b: a if b == 0 else gcd(b, a % b)

# print(f"The gcd of {a} and {b} is:", gcd(a, b))

#(24) Write a Python program to calculate the sum of all elements in a list recursively.

# def recursive_sum(list):
#     if len(list) == 0:
#         return 0
#     else:
#         return list[0] + recursive_sum(list[1:])

# l = [1, 2, 3, 4, 5]
# sum = recursive_sum(l)
# print("Sum of all elements in the list:", sum)

#(25) Write a Python program to count the number of occurrences of each element in a tuple.

tup = (1, 2, 3, 4, 3)
element = int(input("Enter an element:"))
element_counts = {element: tup.count(element) for element in tup}

print("Number of occurrences of each element in the given tuple:", element_counts)
    
