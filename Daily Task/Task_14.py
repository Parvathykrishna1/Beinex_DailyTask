"""
Task - 1
Create a class called Add , it must have __call__ defined. Create an object of that class.
When the object is directly called with a list of integers - like - obj([1,2,3,4,5]) It must return the sum
of elements in the list.
Eg:
add = Add()
total = add([1,2,3,4,5,6])   """


class Add:
    def __call__(self, n):
        return sum(n)


add = Add()
result = add([2, 4, 6, 7])
print(f"Sum = {result}")

"""
Task - 2
Create a class for creating and writing data to a text file. The class must have __enter__ and __exit__
defined.
__enter__ must use the built in `open` to open the file and set the file pointer to self.
__exit__ must close the file pointer on exit.
If the user entered text contains the word 'bug' then __exit__ must delete the file on exiting.
Or if any exception has occurred, then also __exit__ must delete the file.(remember to close file
before deleting)
Use a `with` block to execute the logic.    """

import os


class TextFileHandling:
    def __enter__(self):
        self.file = open("f1.txt", "w")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if "bug" in open("f1.txt").read() or exc_type is not None:
            os.remove("f1.txt")


with TextFileHandling() as file:
    try:
        data = input("Enter the text: ")
        file.write(data)
    except Exception as e:
        print(f"An error occurred: {e}")
