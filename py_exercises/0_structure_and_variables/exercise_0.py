"""
Triple quotes represent block comments in python. These comments may
be of any arbitrary length, but must be deliniated by triple double-quotes
on the top/bottom of the comment.

It is generally a good idea to include comments at the beginning of every
python file, so that you can remember (and communicate to others) what
the file does.
"""


"""
In most circumstance, python files begin with 'import' statements,
which are libraries - either included with the standard python
distribution or installed by you -  that allow you to utilize
various libraries to implement your intended program.

Below, we import 'glob', which is a library that allows you to list
files in a particular directory, and 'os', which allows you to access
your underlying file system.
"""

import math
import glob
import os


"""
Python code itself is organized into functions and classes.
(We'll cover classes later, so no worries!)

You can write python code without functions using a list of
statements in the file - however, it is good practice to use
a main function in each python program.

Unlike other programming languages that use curly braces: {}
to delinate between sections and scopes of code, python uses
spaces or tabs. VSCode is already set up to use 4 spaces for each
press of a tab key.

It will be a bit confusing at first to figure out when a tab
should be included in a program, but I promise you'll be able
to intuit after a few exercises. 

The following is a main function, the starting point of 
a python program:
"""


def main():

    print("Hello World, I'm a main function!")

    # Comments may also be written with the hash character.
    # The following function is called inside of the main function,
    # when you run the program.
    exerciseFunction()

    # in Python, "pass" is a keyword that indicates that your function
    # does not return a value.
    pass


def exerciseFunction():
    """
    In this function, we're going to work on variables and
    data structures

    Readings:

    Python basic data types: https://realpython.com/python-data-types/
    Python lists and tuples: https://realpython.com/python-lists-tuples/

    """

    
    """
    Example Exercise 1
    """

    # For how many full decades have you been alive?

    age = 33  # my guess of your age!
    decade_length = 10
    number_of_decades_int = math.floor(age/decade_length)

    # the string representation of this number
    number_of_decades_string = str(number_of_decades_int)

    print(f"I am {number_of_decades_string} decades old")

    pass


    """
    Exercise 2: How many files are in your home directory
    """

    home_directory_location = os.path.expanduser("~")
    home_directory_files = glob.glob(f"{home_directory_location}/*")
    
    # uncomment below and fill in the misssing code
    # HINT: you will need to use a built-in python function that returns the length of a list
    
    # count_of_home_directory_files = ???
    # print("There are {count_of_home_directory_files} in {home_directory_location}")


    """
    Why are we using f before a string, and what is the meaning of the curly brackets?
    
    https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36



    Additional exercises to complete:

    https://imperialcollegelondon.github.io/python-novice-mix/03-types-conversion/index.html

    """


"""
The following is a command that is particular to python
to ensure your main function runs when you run your python
file at the command line. For now, you can copy and paste this.
"""

if __name__ == "__main__":
    main()


