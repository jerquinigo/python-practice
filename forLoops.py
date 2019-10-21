#syntax for a for loop
# myList = [1,2,3,4,5]
# for itemName in myList:
#   print(itemName)

# whitespace is very important for python. If indented and not in the correct place, it will not execute even if the code block is correct
myList = [1,2,3,4,5,6,7,8,9]

for myTest in myList:
     print(myTest)

myList2 = ["nathalie", "jonathan", "Daniel"]

for names in myList2:
    print(names)

for num in range(1,21):
    string = " "
    if num % 3 == 0:
        string = string + "fizz"
    if num % 2 == 0:
        string = string + "buzz"
    if num % 2 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string, end=" ")

    # 1  buzz  fizz  buzz  5  fizzbuzz  7  buzz  fizz  buzz  11  fizzbuzz  13  buzz  fizz  buzz  17  fizzbuzz  19  buzz

    # indentation of the print statement can show the progress of what is going on inside the for loop or show the final results

    #example

myList3 = [2,4,6,8,10]
list3Sum = 0

for num in myList3:
    list3Sum = list3Sum + num
    print(list3Sum, "indenting the print will show the steps in the for loop")
print(list3Sum, "not indenting the print shows the final results")

# can also iterate in a tuple.  Can also iterate through a list with tuple with packing.
tupleEx1 = (1,2,3,4,5,6)
for num in tupleEx1:
    print(num, "the tuple elements")

# list with tuple elements

listTupleCombo = [(1,2), (3,4), (5,6), (7,8)]
print(len(listTupleCombo), "the length of the combo")

# prints out the length of the tuple combo
#4

for item in listTupleCombo:
    print(item)
#(1, 2)
#(3, 4)
#(5, 6)
#(7, 8)

# this data structure is used alot in python
#its called tuple in packing

# can also take out the packing and have it print in different lines

for(a,b) in listTupleCombo:
    print(a, "first variable")
    print(b, "second variable")
#1 first variable
#2 second variable
#3 first variable
#4 second variable
#5 first variable
#6 second variable
#7 first variable
#8 second variable

# can use parantheses or not for the tuple and packing.

# another example of tuple unpacking

myList4 = [(1,2,3),(4,5,6),(7,8,9)]

for a,b,c in myList4:
    print(b, "printing the b tuple packing variables")

#2 printing the b tuple packing variables
#5 printing the b tuple packing variables
#8 printing the b tuple packing variables


# you can also use for loops to interate through a dictionary.

nameDict = {"name1": "tom", "name2": "nathalie", "name3": "jonathan"}

for item in nameDict:
    print(item, "this will print out the key in the dictionary")
#name1 this will print out the key in the dictionary
#name2 this will print out the key in the dictionary
#name3 this will print out the key in the dictionary

# print out the values from the dictonary, you can do this

for item in nameDict.items():
    print(item, "will print out the key and value pairs")
#('name1', 'tom')
#('name2', 'nathalie')
#('name3', 'jonathan')


# to print out either the key or value in a dictionary
for key,value in nameDict.items():
    print(key, "the key in a dictionary")
    print(value, "the value in a dictionary")
#name1 the key in a dictionary
#tom the value in a dictionary
#name2 the key in a dictionary
#nathalie the value in a dictionary
#name3 the key in a dictionary
#jonathan the value in a dictionary


