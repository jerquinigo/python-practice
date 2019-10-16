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