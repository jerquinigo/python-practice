# sets are unordered collections of unique elements
# There can be one representative of the same object

myset1 = set()
print(myset1)
#set()
myset1.add(1)
print(myset1)
#{1}

mylist1 = [1,1,1,1,1,12,2,2,2,3,3,3,3,4,4,4,4,44,44,5]

myset2 = set(mylist1)
print(myset2, "new set with unique values from the list")
# {1, 2, 3, 4, 5, 12, 44} new set with unique values from the list