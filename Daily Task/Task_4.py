1) Write python programs , which accept two inputs and perform the following arithmetic operations
	      i)   Addition (+)
        ii)   Subtraction (-)
        iii)  Multiplication (*)
        iv)   Division (/)
         v)    Modulus (%)
        vi)   Exponentiation (**)
        vii)  Floor Division (//)  

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
op=input("Enter any Operator(+,-,*,/,%,**,//): ")
if op=="+":
    add=x+y
    print("Addition:",add)
elif op=="-":
    sub=x-y
    print("Subtraction:",sub)
elif op=="*":
    product=x*y
    print("Multiplication:",product)
elif op=="/":
    division=x/y
    print("Division:",division)
elif op=="%":
    modulus=x%y 
    print("Modulus:",modulus)
elif op=="**":
    exp=x**y
    print("Exponentiation:",exp) 
elif op=="//":
    fd=x//y
    print("Floor Division:",fd)
else:
    print("Invalid Operator")    


2)Python Program to replicate bank transaction: min balance 500, ask user to the amount to withdraw, 
  print the balance amount after withdrawal, if user enters an amount greater than balance: print:: insufficient balance. 
min_balance=500
current_balance = 5000
withdrawal_amount=int(input("Enter the amount to withdraw:"))
if withdrawal_amount>current_balance:
    print("Insufficient Balance")
else:
    current_balance -= withdrawal_amount
    if current_balance<min_balance:
        print("Warning: Your balance is below the minimum required balance.")
    print("Balance after withdrawal:", current_balance) 

   
3)Print the greatest of the 3 numbers taken as input, print equal if all three numbers are the same
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
if n1==n2==n3:
    print("Three numbers are same")
else:
    max_num = max(n1, n2, n3)
    print("Greatest number:", max_num)

4)Python program to check the number taken as an input is even or odd,print invalide input if user enters anything other than integers
n=int(input("Enter a number:"))
if n%2==0:
    print("Even number")
elif n%2!=0:
    print("Odd number")
else:
    print("Invalid Input")     
   

5)Python program to check the score from a student ,print grades as A+ if score >= 90,A if 80 or above, B+ if 70 or above and so on... 
print failed if the score is below 50, if score > 100 print invalid
score=int(input("Enter the score:"))
if score > 100:
    print("Invalid")
elif score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B+")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Failed")
   

6)Python program to print all even/odd numbers in the range given by user
start=int(input("Enter the starting number of range:"))
end=int(input("Enter the ending number of range:"))
op=input("Enter even or odd :")
if op=="even":
    for i in range(start,end):
        if i%2==0:
            print(i,end=" ")
elif op=="odd":
    for i in range(start,end):
        if i!=2:
            print(i,end=" ")
else:
    print("Invalid") 
                          
7)Python program to print the multiplication table of any number(number should be taken as input and user decides the end limit of the table)
n = int(input("Enter a number:"))
limit=int(input("Enter the end limit:"))
for i in range(limit):
    p=n*i
    print(n,"*",i,"=",p)

    
8)Find the factorial of a number taken as input using for loop
n= int(input("Enter a number:"))
f=1
for i in range(1,n+1):
    f*=i
print("Factorial of",n,"is",f)


9)Find the factorial of a number taken as input using while loop
n= int(input("Enter a number:"))
f=1
i=1
while i<=n:
    f*=i
    i+=1
print("Factorial of",n,"is",f)    


10)Find the sum of all even numbers between the range given by user
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
sum=0
for i in range(start,end+1):
    if i%2==0:
        sum+=i
print("Sum of even numbers:",sum)       


11)Find the sum of all odd numbers between the rane given by user using while loop
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
sum=0
num = start
while num <= end:
    if num % 2 != 0:
        sum += num
    num += 1
print("Sum of odd numbers:",sum)       


12)Print first 10 fibonacci numbers using 'for' and 'while' loops
Using For loop
n=int(input("Enter the series range:"))
a,b=0,1
print(a)
print(b)
for i in range(1,n):
    value = a + b
    print(value)
    a,b=b,value

# Using While loop
n=int(input("Enter the series range:"))
a=0
print(a)
b=1
while(b<=n):
    print(b)
    a,b=b,a+b


13.print the following patterns
(a)
	         *
           * *
          * * *
         * * * *
k=2*3
for i in range(1,5):
    for k in range(1,k+1):
        print(end=" ")
    k=k-2
    for j in range(1,i+1):
        print("*",end="   ")
    print()   

(b)	o
		1 2
		3 4 5
		6 7 8 9
n=0
for i in range(1,5):
    for j in range(1,i+1):
        print(n,end="   ")
        n+=1
    print() 


(c)	o
		1 1
		2 2 2
		3 3 3 3
for i in range(0,4):
    for j in range(0,i+1):
        print(i,end="   ")
    print()    


(d)	*
		* *
		* * *
		* * * *   
for i in range(1,5):
    for j in range(1,i+1):
            print("*",end="  ")
    print()
