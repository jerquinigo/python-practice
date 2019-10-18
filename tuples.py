# tuples are very similar to lists. However they have one key difference- They have immutability

#once an element is inside a tuple, it can not be reassigned

# tuples use parenthesis(1,2,3)

# Just like a list, you can use slicing and indexing

# two new methods in the tuples are the index method and the count method

tuple1 = ('a', 'a', 'a', 'a', 'b', 'b')
print(tuple1.count('a'), 'count the number of times it sees what is put in the argument')
# 4
print(tuple1.index('a'), 'prints out the first time the argument appears in the tuple')
# 0

# tuples have fewer available methods and do not have the mutability of a list.

