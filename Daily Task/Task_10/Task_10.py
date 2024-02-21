File handling in Python – task
(1) Write a Python program to read an entire text file.

file1 = open("a.txt", "r")
print(file1.read())
file1.close()  

(2) Write a Python program to read first n lines of a file.

file1 = open("a.txt", "r")
lines = int(input("Enter how many lines to be read:")) 
for i in range(lines):
    read_lines = file1.readline()
    print(read_lines)

(3) Write a Python program to append text to a file and display the text.

with open("a.txt", 'a') as file:
    file.write("Python is a high level programming language.")

with open("a.txt", 'r') as file:
    print(file.read())

(3)Write a Python program to read a file line by line store it into a variable.

file_content = ""
with open('a.txt', 'r') as file:
    for line in file:
        file_content += line

print("File contents stored in a variable:")
print(file_content)


(4)Write a Python program to copy the contents of a file to another file.

with open('a.txt','r') as firstfile, open('b.txt','a') as secondfile: 
	
	for line in firstfile: 
			secondfile.write(line)
			
with open("b.txt", 'r') as secondfile:
	print("Contents of Second file:")
	print(secondfile.read())		

(5)Write a Python program to read a random line from a file.

import random

with open("a.txt", 'r') as file:
    lines = file.readlines()

random_line = random.choice(lines)
print("Random line from", "a.txt", ":", random_line)

(6)Write a Python program to assess if a file is closed or not.

file = open('a.txt', 'r')  
if file.closed:
    print("File is closed.")
else:
    print("File is open.")

file.close()  


(7)Write a Python program to write a list to a file.

list1 = ["python", "java", "html", "css"]

with open('c.txt', 'w') as file:
    for i in list1:
        file.write("%s\n" % i)

with open("c.txt", 'r') as file:
	print(file.read())
file.close() 


(8)Write a Python program that takes a text file as input and returns the number of words of a given text file.
Note: Some words can be separated by a comma with no space.

with open('d.txt', 'r') as file:
    content = file.read()
    word_count = len(content.split())
    print("Number of words:", word_count)

(9)Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line.

import string

n = int(input("Enter the number of letters per line:"))
with open('e.txt', 'w') as file:
    for i in range(0, len(string.ascii_uppercase), n):
        line = string.ascii_uppercase[i: i + n]
        file.write(line + '\n')

print("Alphabet file created successfully:", "e.txt")



