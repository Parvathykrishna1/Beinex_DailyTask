# 1.Write a Python program to calculate the length of a string.
# s=input("Enter a string:")
# l=len(s)
# print("Given string:",s)
# print("Length of the given string:",l)
# 2.Print even length words in a string.
# Sample String : ''I love coding"
# Expected Result : “love, coding”

# s="I love coding"
# str = s.split(" ")
# l=list(filter(lambda x: (len(x)%2==0),str))
# print(" ".join(l))

# 3.Write a Python code to remove all characters except a           
# Sample String : 'exercises'
# Expected Result : 'eee' (Removed all characters except special character : e)
def remove_characters(str,n):
  return ''.join([x for x in str if x == n])
s = "exercises"

print("Given string:",s)
except_char = "e"
print(f"Remove all characters except {except_char} in the given string:")
print(remove_characters(s,except_char))

