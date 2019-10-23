# syntax for functions

#def nameOfFunction():
    #print("hello")
# nameOfFunction()


def myFirstFunction():
    print("my first python function")

myFirstFunction()

# functions should have snake_casing to seperate the words

# reason function names should be lowercase with words seperated by underscores as necessary to improve readability.

def greeting_name(name):
    print(f"hello {name}")

greeting_name("Jonathan")

def adding_numbers(num1, num2):
    return num1 + num2

print(adding_numbers(7,7), "the function adding")


# functions have docstrings in them. It is good practice to put them in the function block. it is made up of three single quotes. It is used for the help function to see what the function supposed to input and output


def test_function():
    '''
    DOCSTRING: Information about the function
    INPUT:  no input...
    OUTPUT: hello test function
    '''
    print("hello test function")

#help(test_function)
#test_function()
#DOCSTRING: Information about the function
#INPUT:  no input...
#OUTPUT: hello test function

# to see the doc string in a function, you should not invoke it when you are checking it out with the help function
# example help(test_function)

# you can have default parameters in python functions

#example1

def default_name_function(name="jonathan"):
    print(f"hello {name}")

default_name_function()
#hello jonathan
default_name_function("nathalie")
#hello nathalie

#having default arguments assigned is good if there is no argument that has been passed to the function.

def to_return_name_function(name="daniel"):
    return f"hello {name}, how are you doing today"

results2 = to_return_name_function()

print(results2)
#hello daniel, how are you doing today