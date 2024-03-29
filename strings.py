# strings have indexes just like how arrays would work in js.
# python has reverse indexing
#example
# h e l l o
# 0 1 2 3 4
# h  e  l  l  0
# 0 -4 -3 -2 -1
# reverse indexing is used to grab the last element of the indexed item

name = "Nathalie"
print(name[-1])

# slicing allows you to grab a subsection of multiple characters, a slice of the string.

# syntax for slice is [start:stop:step]
# start is a numerical index for the slice start

#escape sequence
print("hello \n world")
#prints on a new line

#slicing

myString = "Jonathan"
# to print to the end of the line, you would use :
# to print the entire length of the string you will have to type myString[0:]
print(myString[0:], "to print the entire word")

#to print out to a certain length, you can set it either as myString[0:8] or myString[:8]
print(myString[:7])

# there is also a step size. It is the third parameter for the index values. having index[::] means that it will start from the beginning and will go to the end of the string. 
# there is a third parameter. An example will be [::2]

print(myString[::2], "jumping steps from two and starting and ending from the end of the string")

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[::2], "stepping by two")
#acegikmoqsuwy stepping by two
print(alphabet[::3], "stepping by three")
#adgjmpsvy stepping by three

# the index parameters will have a start, stop and a step size
# [start:stop:step]

#doing this with the arguments will reverse a string
print(alphabet[::-1])
# zyxwvutsrqponmlkjihgfedcba

#can also do this to find an index of a string without variables
# "hello world"[8]
print("hello world"[8])

# slicing strings
print("tinker"[1:4], "will print out ink")


# Strings are immutable. Cannot change it my reassigning a value by index. Item assignment.

# only way to have that functionality, you will have to create a new string with the value

# String Concatenation

name = "sam"
newName = name[1:]
newName = "P" + newName
print(newName, "after the concat")

# steps needed to create a new string and concat the values

# example 2

greeting = "hello world"
greeting = greeting + " it is beautiful outside <3"
print(greeting, "after the concat")

# can also use a multiplication of letters
sleeping = "z"
sleeping = sleeping * 10
print(sleeping, "goodnight")


# the split method for a string creates a list for python

newGreeting = greeting.split()
print(newGreeting)
#['hello', 'world', 'it', 'is', 'beautiful', 'outside', '<3']
# the split method also takes in arguments. If blank, it will split on the white space. If a letter, it will split on the letter.

newGreeting = greeting.split('i')
print(newGreeting)
#['hello world ', 't ', 's beaut', 'ful outs', 'de <3']


# string interpolation
# there are two methods for this
#.format()method
# f-strings(formatted string literals)

# examples of using the format() method

print('hello world, it is a {} day outside'.format("rainy"))
# by using the curly braces and .format() at the end of the string, you will be able to insert data into the curly braces location

# example 2

print("the {} {} {}".format("fox", "brown", "quick"))

# the fox brown quick

# you can have more than one instance of curly brances and format data. It will be inserted by order by the way the arguments are listed in order in format.


# example 3

print("the {2} {1} {0}".format("fox", "brown", "quick"))

# the quick brown fox

# you can also tell the index location of where you want the data from format argument to be inserted into the curly braces correctly to create a string of your choosing.


# example 4
# you can declare variables in format arguments and use them instead of index numbers and create a string of your choosing

print("the {q} {b} {f}".format(f="fox", b="brown", q="quick"))

#the quick brown fox

#using variables and indexes can be used for the format() method


# float formatting follows "{value:width.precision f}"

# value is the data and width is the white spaces that will be seperated from the main string text. Precision is the numbers that will show and truncate the rest of the data. need to follow precision with f

# example 1

resultDivision = 100/777
print(resultDivision)
# result of division 0.1287001287001287

print("the result was {r}".format(r=resultDivision))
# the result was 0.1287001287001287

print("the result was {r:1.7f}".format(r=resultDivision))

#the result was 0.1287001



# The second way is the string literal method. Same as string interpolation in JavaScript
# this is known as the fstrings

name = "Jonathan"
print(f"hello, my name is {name}")
#hello, my name is Jonathan

# its similar to format() method. changing the syntax to use f in front of the string and put the variable into the curly braces

