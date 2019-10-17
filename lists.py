# Lista are ordered sequences that can hold a variety of object types
# they use [] brackets and commas to separate objects in the list
#ex [1,2,3,4,5]

# lists support indexing and slicing. Lists can be nested and also have a variety of useful methods that can be called off of them

myList = [1,2,3,4,5]
print(myList)

# to print out the length of a list
print(len(myList), "is the length of my list")

#indexing works here as well
print(myList[1])
# 2

#similar to strings, you can do slicing, and stepping
print(myList[::2])
# [1, 3, 5]

# you can also concatenate lists

secondList = [6,7,8,9,10]
myList = myList + secondList
print(myList, "the new list")
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] the new list

# changing data inside an index of a list
myList[0] = 100
print(myList)

# there are list methods similar to js. One is to append

myList.append(999)
print(myList, "with the new append")
#[100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999] with the new append

myList.pop()
print(myList, "list with the last element removed")
#[100, 2, 3, 4, 5, 6, 7, 8, 9, 10] list with the last element removed

poppedItem = myList.pop()
print(poppedItem)
# 10

# you can also put int the pop arguments what location you want to pop any item in the list.

# example 1
firstPoppedItem = myList.pop(0)
print(firstPoppedItem, "the first element removed")
print(myList, "my list after removing first element")

#100 the first element removed
#[2, 3, 4, 5, 6, 7, 8, 9] my list after removing first element

# you can also use the reverse indexing as an argument for the pop(). example would be .pop(-1)

newList = ['a','e','x','b','c']
numList = [4,1,8,3]

# using the sorted method, you do not have to store it to a variable, because it does not return anything. It is something it does in place. Just run the method then print out the list again and it will be sorted.

newList.sort()
numList.sort()
print(newList, "sorted list after sort method has been run")
print(numList, "sorted list after sort method has been run")

#['a', 'b', 'c', 'e', 'x'] sorted list after sort method has been run
#[1, 3, 4, 8] sorted list after sort method has been run


# None is a null value just like null is to js. 
#None is a return value of a function that does not return anything. It is used for search functions that may or may not return anything.
#print(None)

#reverse method does not return anything either. Can be run one line above and then print out the list values

numList.reverse()
print(numList, "reverse method has reversed the values")
# [8, 4, 3, 1] reverse method has reversed the values