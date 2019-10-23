# *args and **kwargs

# *args are arguments
# **kwargs are keyword arguments

# positional arguments - means the order that arguments are listed as in the function arguments. 

def wildcard_function(*args):
    print(args)

wildcard_function("hello my name is" "" "jonathan")
#to print out the wildcards args without the wildcard, the return result will be in a tuple form

#('hello my name isjonathan',)

#*args is not a keyword and other words can be used as an argument as long as the wildcard is in front
# it is better practice to stick to using *args

# can also pass in how many arguments you want and even loop through them.


def wildcard_looping_function(*args):
    for item in args:
        print(item)

wildcard_looping_function(1,2,3,4,5,6,7,8,9)

# it will print out 1-9 in a loop

## **kwargs print out a dictionary of keys and values

def wildcard_looping_kwargs1(**kwargs):
    print(kwargs, "the dictionary created using **kwargs")
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format('fruit'))

wildcard_looping_kwargs1(fruit="apple", veggie="lettuce")


#{'fruit': 'apple', 'veggie': 'lettuce'} the dictionary created using **kwargs
#my fruit of choice is fruit
