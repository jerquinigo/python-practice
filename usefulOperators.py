myList1 = [1,2,3,4]

# range takes in a start:stop:step arguments
for num in range(2,11,2):
    print(num)

#2
#4
#6
#8
#10

#range is a generator. if you want to have the range be put in a list you can do this

newList1 = list(range(2,21,2))
print(newList1, "new list numbers")
# ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 'new list numbers')


indexCount = 0
word1 = "abcde"

for letter in word1:
    print(word1[indexCount])
    indexCount += 1
    print(indexCount, "the indexCount")
#a
#(1, 'the indexCount')
#b
#(2, 'the indexCount')
#c
#(3, 'the indexCount')
#d
#(4, 'the indexCount')
#e
#(5, 'the indexCount')

# enumerate is similar to using indexCount

for item in enumerate(word1):
    print(item)
#(0, 'a')
#(1, 'b')
#(2, 'c')
#(3, 'd')
#(4, 'e')

# the result of the index and the value comes back as tuples
# does the index count for us


# can also seperate the pair using two variables in the for loop


# example

for index,letter in enumerate(word1):
    print(index, "the index")
    print(letter, "the letter")
    print('\n')

#(0, 'the index')
#('a', 'the letter')
#
#
#(1, 'the index')
#('b', 'the letter')
#
#
#(2, 'the index')
#('c', 'the letter')
#
#
#(3, 'the index')
#('d', 'the letter')
#
#
#(4, 'the index')
#('e', 'the letter')



# zip function. The opposite of enumerate
newList1 = [1,2,3]
newList2 = ["a", "b", "c"]
newList3 = zip(newList1,newList2)
print(newList3)
# [(1, 'a'), (2, 'b'), (3, 'c')]
# this way puts the tuples in a list

for item in zip(newList1, newList2):
    print(item, "the new item using zip and a loop")

# ((1, 'a'), 'the new item using zip and a loop')
#((2, 'b'), 'the new item using zip and a loop')
#((3, 'c'), 'the new item using zip and a loop')


# zip pairs up the items and they match together.
# you can do this with more than two lists

# the list can only zip items that are equal. If the list1 has 6 items and list2 two has 3 items, It will zip up to the three items and ignore the last three

nList1 = [1,2,3,4,5,6]
nList2 = ["a", "b", "c"]
nList3 = [100,200,300]

nList4 = zip(nList1,nList2,nList3)
print(nList4)
# [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]

for item in zip(nList1,nList2,nList3):
    print(item)
#(1, 'a', 100)
#(2, 'b', 200)
#(3, 'c', 300)


# tuple packing using zip


# in is another keyword that returns a boolean True or False to see if an element is in a list, dictonaries , etc

print("n" in "nathalie", "results of using in")
#(True, 'results of using in')

# example of using in for dictionaries

d1 = {"key1": "jonathan"}

print("key1" in d1.keys())
# True
print("jonathan" in d1.values())
# True