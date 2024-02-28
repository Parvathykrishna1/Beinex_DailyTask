1.Write a Python program that prompts the user to enter an integer and handles the ValueError exception if the user enters a non-integer value.

while True:
    try:
        n = input("Enter an integer: ")
        num = int(n)
        print("Entered number:", num)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

2.Create a program that opens a file and reads its contents. Use a try-except block to handle the FileNotFoundError exception and display a custom error message if the file does not exist.

try:
    with open(input("Enter file name: "), 'r') as file:
        print("File contents:\n", file.read())
except FileNotFoundError as e:
    print(f"Error: {e.filename} not found.")


3.Write a program that calculates the division of two numbers entered by the user. Use a try-except block to handle the ZeroDivisionError exception and display an appropriate error message if the user tries to divide by zero.

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    print("Result:", numerator / denominator)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numeric values.")


4.Create a program that attempts to connect to a website and prints the HTML content if successful. Use a try-except-else block to handle the requests.exceptions.RequestException exception and display an error message if the connection fails.

import requests

url = input("Enter the URL of the website: ")
try:
    html_content = requests.get(url).text
except requests.exceptions.RequestException as e:
    print(f"Error: Failed to connect to the website: {e}")
else:
    print(f"Connection successful.\nHTML content:\n{html_content}")


5.Write a program that opens a file, reads its contents, and writes the contents to a new file. Use a try-except-finally block to ensure that the file is closed even if an exception occurs during the file operations.

try:
    with open("input_file.txt", 'r') as input_file:
        inputfile_contents = input_file.read()

    with open("output_file.txt", 'w') as output_file:
        output_file.write(inputfile_contents)

    print("File contents successfully copied.")
except FileNotFoundError:
    print("Error: Input file not found.")
except IOError as e:
    print(f"Error: {e}")
finally:
    print("File operations complete.")


6.Write a Python program that reads email details (sender, recipient, subject, and body) from user input and sends the email using Mailtrap as the SMTP server.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Enter sender email: ")
recipient_email = input("Enter recipient email: ")
subject = input("Enter email subject: ")
body = input("Enter email body: ")

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

smtp_server = 'smtp.mailtrap.io'
smtp_username = 'username'
smtp_password = 'password'
smtp_port = '1234'

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server.quit()


7.write a python program to send an email with multiple recipients using the smtplib library.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Enter your email address: ")
password = input("Enter your email password: ")

subject = input("Enter the subject of the email: ")
body = input("Enter the body of the email: ")

recipients = []
while True:
    recipient = input("Enter recipient's email address (leave blank to finish): ")
    if not recipient:
        break
    recipients.append(recipient)

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = ", ".join(recipients)
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

smtp_server = "smtp.mailtrap.io"
smtp_username = "username"
smtp_password = "password"
smtp_port = "1234"

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    server.sendmail(sender_email, recipients, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server.quit()


8.write a python program to handle exceptions when sending emails using Python's smtplib library.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
    sender_email = input("Enter your email address: ")
    password = input("Enter your email password: ")
    subject = input("Enter the subject of the email: ")
    body = input("Enter the body of the email: ")
    recipient = input("Enter recipient's email address: ")

    smtp_server = input("Enter SMTP server address: ")
    smtp_username = input("Enter SMTP username: ")
    smtp_password = input("Enter SMTP password: ")
    smtp_port = input("Enter SMTP port: ")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient, message.as_string())
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Authentication error: Please check your email address and password.")
except smtplib.SMTPException as e:
    print(f"SMTP error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


9.Write a Python program that prompts the user to enter their age. Define a custom exception called InvalidAgeError that is raised when the entered age is less than 0 or greater than 150. Handle the InvalidAgeError exception and display an appropriate error message.

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if not 0 <= age <= 150:
        raise InvalidAgeError("Age must be between 0 and 150.")
    print("Your age is:", age)
except ValueError:
    print("Error: Please enter a valid integer for age.")
except InvalidAgeError as e:
    print("Error:", e)


10.Write a Python program that simulates a banking system.
Implement a class called BankAccount with methods to initialize an account with a starting balance, withdraw funds, and handle a custom exception called NegativeBalanceError when the account balance goes below zero.

class NegativeBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, owner_name, initial_balance):
        self.owner_name = owner_name
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Negative amount cannot be withdrawn.")

        if amount > self.balance:
            raise NegativeBalanceError("Insufficient funds.")

        self.balance -= amount
        print("Withdrawal successful. Remaining balance: {}.".format(self.balance))

try:
    account = BankAccount("Parvathy", 1000)
    account.withdraw(500)
    account.withdraw(1000)
except NegativeBalanceError as e:
    print("Error:", e)
except ValueError as e:
    print("Error:", e)
