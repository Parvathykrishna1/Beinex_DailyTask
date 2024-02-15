1.Write a Python program to calculate the length of a string.
s=input("Enter a string:")
l=len(s)
print("Given string:",s)
print("Length of the given string:",l)


2.Print even length words in a string.
Sample String : ''I love coding"
Expected Result : “love, coding”

s = input("Enter a string: ")
words = s.split()

for i in words:
    if len(i)%2==0:
        print("Even length words in the string:",i)

3.Write a Python code to remove all characters except a           
Sample String : 'exercises'
Expected Result : 'eee' (Removed all characters except special character : e)

s = input("Enter a string:")
except_char = "a"

print("Given string:", s)
print(f"Remove all characters except {except_char} in the given string:")
str = ''.join([i for i in s if i == except_char])
print(str)

