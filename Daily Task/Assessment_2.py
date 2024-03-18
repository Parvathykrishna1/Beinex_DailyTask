PYTHON CHALLENGE 2
1. Read and Print the Contents of a Text File

try:
    with open("x.txt", "w+") as f:
        f.write(
            "Python is a general-purpose, dynamically typed, high-level,\n"
            "compiled and interpreted, garbage-collected, and purely object-oriented\n"
            "programming language that supports procedural, object-oriented,\n"
            "and functional programming."
        )
        f.seek(0)
        file_contents = f.read()

    print(f"Contents in the 'x.txt' file: \n{file_contents}")

except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


2. Count the Number of Lines, Words, and Characters in a Text File

try:
    with open("x.txt", "r") as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_char = sum(len(line) for line in lines)

    print("Number of lines:", num_lines)
    print("Number of words:", num_words)
    print("Number of characters:", num_char)

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)


3. Search for a String in a Text File

string = input("Enter the string to search for: ")
try:
    count = 0
    with open("x.txt", "r") as f:
        for line in f:
            if string in line:
                count += line.count(string)

    if count > 0:
        print(f"'{string}' is present {count} time(s) in the file")
    else:
        print(f"'{string}' is not present in the file")


except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)


4. Merge Multiple Text Files into One

input_files = ["a.txt", "b.txt", "c.txt"]
output_file = "mergedfile.txt"

try:
    with open(output_file, "w") as outfile:
        for fname in input_files:
            try:
                with open(fname, "r") as infile:
                    content = infile.read()
                    if content:
                        outfile.write(content)
            except FileNotFoundError:
                print(f"Input file '{fname}' not found.")

    print("Files merged successfully.")

except Exception as e:
    print("An error occurred:", e)


5. Implement a program that reads a text file and counts the occurrences of each word, ignoring case sensitivity.

from collections import Counter

try:
    with open("x.txt", "r") as file:
        words = file.read().lower().split()

        word_counts = Counter(words)

    for word, count in word_counts.items():
        print(f"'The word {word}' occurs {count} times.")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)


6. Write a Python function that takes a list of strings as input and returns a
new list with the strings sorted in descending order of their lengths.

list1 = ['a', 'bb', 'ccc', 'dddd', 'eeeee']

new_list = sorted(list1, key=len, reverse=True)

print(f"List after sorted in descending order:{new_list}")


7. Write a function that takes a list of numbers as input and returns the second-largest number.


def second_largest(list1):
    max_number = max(list1)
    second_largest = max(num for num in list1 if num != max_number)
    return second_largest


list1 = [10, 30, 4, 45, 99, 78]
print("Second largest number:", second_largest(list1))


8. Write a Python program that takes a list of integers as input and returns a
new list with only the numbers that are prime.


def prime_integers(input_list):
    prime_list = []
    for integer in input_list:
        if integer > 1:
            for i in range(2, integer):
                if (integer % i) == 0:
                    break
            else:
                prime_list.append(integer)
    return prime_list


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_list = prime_integers(input_list)
print("Prime integers List:",prime_list)

9. Write a Python function that takes a list of integers as input and returns a
new list with only the numbers that are perfect squares.


def perfect_squares(input_list):
    perfect_square_list = []
    for integer in input_list:
        if integer > 0 and (integer**0.5).is_integer():
            perfect_square_list.append(integer)
    return perfect_square_list


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perfect_square_list = perfect_squares(input_list)
print("Perfect square integers List:", perfect_square_list)


10.Write a Python function that takes a list of numbers as input and returns
the sum of all the numbers divisible by 3 or 5.


def sum_divisible_by_3_or_5(numbers):
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_divisible_by_3_or_5(list)
print("Sum of numbers divisible by 3 or 5:", result)


11. Write a Python function called calculate_discounted_price that takes the original price of an item
and a discount percentage as input. The function should return the discounted price after applying the
discount. Ensure that the function handles the case where the discount percentage is negative
and raises a custom exception called InvalidDiscountError with an appropriate error message.

  
def calculate_discounted_price(original_price, discount_percentage):
    if discount_percentage < 0:
        raise ValueError("Discount percentage cannot be negative.")

    discount_amount = original_price * (discount_percentage / 100)
    discounted_price = original_price - discount_amount
    return discounted_price


try:
    original_price = 999
    discount_percentage = 10
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    print("Discounted price:", discounted_price)
except ValueError as e:
    print("Error:", e)


12.Write a function that takes a sentence as input and returns a new sentence
with the words reversed, while keeping the order of the words in the sentence.


def reverse_words(sentence):
    if not sentence:
        raise ValueError("Input sentence cannot be empty.")
    return " ".join(word[::-1] for word in sentence.split())


try:
    input_sentence = input("Enter a sentence: ")
    reversed_sentence = reverse_words(input_sentence)
    print("Reversed sentence:", reversed_sentence)
except ValueError as e:
    print("Error:", e)


13. Implement a program that simulates a basic calculator, allowing users to perform
arithmetic operations (addition, subtraction, multiplication, division) on two numbers.


def calculator():
    try:
        n1 = float(input("Enter the First Number: "))
        n2 = float(input("Enter the Second Number: "))
        print("Select Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter any choice of operation (1/2/3/4): ")

        if operation == "1":
            result = n1 + n2
        elif operation == "2":
            result = n1 - n2
        elif operation == "3":
            result = n1 * n2
        elif operation == "4":
            if n2 == 0:
                return "Cannot divide by zero"
            result = n1 / n2
        else:
            return "Invalid Input"

        return result

    except ValueError:
        return "Invalid input. Please enter valid numbers."
    except ZeroDivisionError:
        return "Cannot divide by zero."


print("Result:", calculator())


14. Create a class named Notes for handling text-based file operations. Class should contain methods "write", "read"
and then "append" as instance methods or class methods. (Can contain any other methods if you wish)Use a single file
for saving the notes. You can set the file name as a constant somewhere in the program (Or as a class variable).
write method should create the if it doesn't exist, Then it should overwrite the older contents with the user input if
the user plans to overwrite the file. read method should read the whole file contents and return it. If the file doesn't
 exist, then it should return "No notes found" append method should take the user input value and it must add the value
to the end of the file. It must not overwrite the file. Now create a program to utilize this class.
The program should repeatedly ask the user for these 4 choices :
1 - Write Note (Overwrite existing).
2 - Add more Notes (Append).
3 - Read Notes.
4 – Exit


class Notes:
    file_name = "x.txt"

    def __init__(self):
        self.content = ""

    def write(self):
        self.content = input("Enter your note: ")
        with open(self.file_name, 'w') as file:
            file.write(self.content)
        print("Note written successfully.")

    def read(self):
        try:
            with open(self.file_name, 'r') as file:
                self.content = file.read()
            return self.content if self.content else "No notes found."
        except FileNotFoundError:
            print("No notes found.")

    def append(self):
        additional_note = input("Enter additional note: ")
        with open(self.file_name, 'a') as file:
            file.write(additional_note + "\n")
        print("Additional note added successfully.")

    def clear(self):
        self.content = ""
        with open(self.file_name, 'w') as file:
            file.write("")
        print("Notes cleared successfully.")

    def search(self, keyword):
        if self.content:
            notes_list = self.content.split("\n")
            matching_notes = [note for note in notes_list if keyword.lower() in note.lower()]
            if matching_notes:
                print("\n".join(matching_notes))
            else:
                print("No matching notes found.")
        else:
            print("No notes found.")

    @classmethod
    def delete(cls):
        try:
            with open(cls.file_name, 'r') as file:
                content = file.read()
            if content:
                with open(cls.file_name, 'w') as file:
                    file.write("")
                print("All notes deleted successfully.")
            else:
                print("No notes found to delete.")
        except FileNotFoundError:
            print("No notes found to delete.")

    @staticmethod
    def welcome_message():
        print("Welcome to the Notes App!")


def main():
    Notes.welcome_message()
    notes = Notes()

    while True:
        print("\nMenu:")
        print("1 - Write Note (Overwrite existing)")
        print("2 - Add more Notes (Append)")
        print("3 - Read Notes")
        print("4 - Clear Notes")
        print("5 - Search Notes")
        print("6 - Delete all Notes")
        print("7 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            notes.write()
        elif choice == '2':
            notes.append()
        elif choice == '3':
            notes.read()
        elif choice == '4':
            notes.clear()
        elif choice == '5':
            keyword = input("Enter keyword to search: ")
            notes.search(keyword)
        elif choice == '6':
            Notes.delete()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


15. Copy odd lines of one file to another file in Python

try:
    with open('x.txt', 'r') as infile:
        with open('output.txt', 'w') as outfile:
            line_number = 1

            for line in infile:
                if line_number % 2 != 0:
                    outfile.write(line)

                line_number += 1

    print("Odd lines copied successfully.")

except FileNotFoundError:
    print("Input file not found.")
except Exception as e:
    print("An error occurred:", e)


16. Count the total number of uppercase characters in a file in Python

try:
    with open('x.txt') as f:
        count = sum(character.isupper() for character in f.read())
        print(f"total number of uppercase characters in a file: {count}")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)

17. Python program to delay printing of line from a file using sleep function

import time

try:
    with open('x.txt', 'r') as file:
        for line in file:
            print(line.strip())
            time.sleep(1)

except FileNotFoundError:
    print("The file does not exist.")

except Exception as e:
    print("An error occurred:", e)


18. Python program to for student height record for a school using Class and Objects.

class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, height):
        self.students.append({"name": name, "height": height})

    def display_students(self):
        for student in self.students:
            print(f"{student['name']}: {student['height']} cm")


school = School()

school.add_student("Aby", 160)
school.add_student("Bob", 155)
school.add_student("Clary", 170)

school.display_students()


19. Write program for building restaurant menu using class in Python.


class MenuItem:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name}: ${self.price} - {self.description}"

    def __repr__(self):
        return f"MenuItem('{self.name}', {self.price}, '{self.description}')"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"{name} removed from the menu.")
                return
        print(f"{name} is not in the menu.")

    def display_menu(self):
        print("Menu:")
        for item in self.items:
            print(item)


burger = MenuItem("Burger", 199.99, "A classic beef burger with cheese and lettuce")
pizza = MenuItem(
    "Pizza", 250, "Thin crust pizza with tomato sauce and mozzarella cheese"
)
salad = MenuItem(
    "Salad", 0.20, "Fresh mixed greens with tomatoes, cucumbers, and dressing"
)

menu = Menu()

menu.add_item(burger)
menu.add_item(pizza)
menu.add_item(salad)

menu.display_menu()

menu.remove_item("Pizza")

menu.display_menu()


20. Create a Python library with the function to input the values with expectation handling and demonstrate with the example.

def get_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    celsius = get_input("Enter the temperature in Celsius: ", float)
    fahrenheit = (celsius * 9 / 5) + 32
    print("The temperature in Fahrenheit is:", fahrenheit)


21. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

list = [1, 2, 3, 4, 5]

try:
    index = int(input("Enter the index: "))
    value = list[index]

    print("Value at index", index, ":", value)

except IndexError:
    print("Index is out of range.")


22. Write a Python program input and add two integers only and handle the exceptions.

"""
RUN 1:
Enter First Value: 10
Enter Second Value: 20
0.5

RUN 2:
Enter First Value: 10
Enter Second Value: Hello
Pls Input Integer Only invalid literal for int() with base 10: 'Hello'

RUN 3:
Enter First Value: 10
Enter Second Value: 0
Second Number Should Not Be Zero division by zero              """

while True:
    try:
        x = int(input("Enter First Value: "))
        y = int(input("Enter Second Value: "))

        if y == 0:
            raise ZeroDivisionError("Second Number Should Not Be Zero")

        result = x / y
        print("Result:", result)
        break

    except ValueError as e:
        print("Pls Input Integer Only:", e)

    except ZeroDivisionError as e:
        print(e)

    except Exception as e:
        print("Other Error:", e)

23. The program takes input from the user and checks if whether the input value is an integer or not, if the input value is 
not an integer then the program will through a Type exception.
"""
Run 1:
Enter First Number: 43
43

Run 2:
Enter First Number: 123.1
Invalid Input..Please Input Integer Only..
Enter First Number: 43
43            """


while True:
    try:
        num = int(input("Enter First Number: "))
        print(num)
        break
    except ValueError:
        print("Invalid Input. Please Input Integer Only.")


24.Implement the game rock, paper, scissors
    Rock smashes scissors.
    Paper covers rock.
    Scissors cut paper.
    
    def determine_winner(player1_choice, player2_choice):
        if player1_choice == player2_choice:
            return "It's a tie!"
        elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
             (player1_choice == 'paper' and player2_choice == 'rock') or \
             (player1_choice == 'scissors' and player2_choice == 'paper'):
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    
    def main():
        choices = ['rock', 'paper', 'scissors']
    
        while True:
            player1_choice = input("Player 1, enter your choice (rock, paper, or scissors): ").lower()
            if player1_choice not in choices:
                print("Invalid choice. Please enter either 'rock', 'paper', or 'scissors'.")
                continue
    
            player2_choice = input("Player 2, enter your choice (rock, paper, or scissors): ").lower()
            if player2_choice not in choices:
                print("Invalid choice. Please enter either 'rock', 'paper', or 'scissors'.")
                continue
    
            print(determine_winner(player1_choice, player2_choice))
    
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
    
    main()


25.  Quiz Game in Python

    questions = [
        {"prompt": "What color is the sky?\n(a) Blue\n(b) Red\n(c) Green\n", "answer": "a"},
        {"prompt": "What animal says 'meow'?\n(a) Dog\n(b) Cat\n(c) Bird\n", "answer": "b"},
        {"prompt": "How many legs does a cat have?\n(a) 2\n(b) 4\n(c) 6\n", "answer": "b"},
    ]
    
    
    def run_quiz(questions):
        score = 0
        for question in questions:
            print(question["prompt"])
            answer = input("Enter your answer (a, b, or c): ").lower()
            if answer == question["answer"]:
                score += 1
                print("Correct!")
            else:
                print("Incorrect!")
        print(f"You got {score}/{len(questions)} correct.")
    
        percentage_score = (score / len(questions)) * 100
    
        if percentage_score >= 70:
            print("Great job! You have a strong knowledge.")
        elif 50 <= percentage_score < 70:
            print("Not bad! You have some knowledge.")
        else:
            print("Keep learning! You can do even better.")
    
    
    print("Welcome to the Kids Quiz")
    run_quiz(questions)
