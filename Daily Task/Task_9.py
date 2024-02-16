# Python Dictionary Questions - Task_9

# 1.Write a Python program to merge two Python dictionaries.
# def merge_dict(d1, d2):
#     return { **d1, **d2}   #Dictionary unpacking

# d1 = {'name': 'parvathy', 'age': 23}
# d2 = {'Maths': 90, 'English': 75}
# merged_dict = merge_dict(d1, d2)
# print("Merged Dictionary:", merged_dict)


# 2.Write a Python program to get dictionary keys as a list
# dict = {'course': 'python', 'batch': 'A', 'tutor': 'Anu'}

# keys_list = [key for key in dict]
# print("Dictionary Keys as a List:", keys_list)


# 3.Write a Python program to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# square_dict = {n: n ** 2 for n in range(1, 16)}

# print("Dictionary with keys as numbers between 1 and 15 and values as their squares:",square_dict)


# 4.Write a Python program to sum all the items in a dictionary.
# dict = {1: 1, 2: 4, 3: 9, 4: 16}
# dict_sum = sum(value for value in dict.values())

# print(f"sum all the items in a dictionary is {dict_sum}")


# 5.Write a Python program to multiply all the items in a dictionary.
# import math
# dict = {'a': 4, 'b': 2, 'c': 8}
# dict_multiply = math.prod(value for value in dict.values())  #Using math.prod() function

# print(f"multiplication all the items in a dictionary : {dict_multiply}")


# 6.Write a Python program to get the maximum and minimum values of a dictionary
# dict = {1: 1, 2: 4, 3: 9, 4: 16}
# max_value = max(value for value in dict.values())
# min_value = min(value for value in dict.values())

# print(f"{max_value} is the maximum value and {min_value} is the minimum value in the given dictionary.")


# 7.Write a Python program to Delete a list of keys from a dictionary
# dict = {'name': 'parvathy', 'age': 23, 'Maths': 90, 'English': 75}
# delete_key = ['Maths', 'English']

# new_dict = {key: dict[key] for key in dict if key not in delete_key}
# print("New Dictionary:",new_dict)

# 8.Create a function that takes a string and returns a dictionary where keys are letters, and values are the number of times each letter appears in the string 
# def create_dict(string):
#     return {x: string.count(x) for x in string if x.isalpha()}


# string = input("Enter a string:")
# dict = create_dict(string)
# print("Dictionary:", dict)


