1.Write a Python program to multiples all the items in a list.
list_data = [1,4,9,12]
total = 1
for x in list_data:
	total *= x
print("Given list:",list_data)    
print("Product of all the items in the given list:",total)    

2.Write a Python program to remove duplicates from a list,
list1= [1,4,9,1,2,3,9]
list2=[]
[list2.append(x) for x in list1 if x not in list2]
print("Final list after removes all the duplicates:",list2)

3.Write a Python program to count the number of strings where the string length is 2 or more.
	Sample List : ['abc', 'xyz', 'aba', '1']
	Expected Result : 3
list_data = ['abc', 'xyz', 'aba', '1', 'jkl']
count = sum(1 for string in list_data if len(string) >= 2)
print("Count the number of strings where the string length is 2 or more:", count)

4.Write a Python program to print the numbers of a specified list after removing even numbers from it
	list = [24,34,53,65,78,93,23,42]
list1 = [24,34,53,65,78,93,23,42]
print("Given list:",list1)
list2 =[]
for i in list1:
    if i%2==0:
        list1.remove(i)
    else:
        list2.append(i)  
print("Final list after removing even numbers:",list2)          


5.Use list comprehension to contruct a new list but add 6 to each item.
	list = [24,34,54,45]
original_list = [24,34,54,45]
new_list = [i+6 for i in original_list]
print("Given list:",original_list)
print("New list after adds 6 to each item:",new_list)


6.Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
	lst1=[2, 4, 6, 8, 10, 12, 14]
list1 = [2, 4, 6, 8, 10, 12, 14]
square_list = [i*i for i in list1 if i*i>50]
print(square_list)

7. Write a Python program to find the repeated items of a tuple.
tup = (3, 5, 6, 7, 8, 2, 7, 4, 7)
for i in tup:
    if tup.count(i)>1:
        print(i)       
