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