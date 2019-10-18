# Dictionaries are unordered mappings for storing objects. Previously, we saw how lists store objects in an ordered sequence.
# Dictionaries use a key-value pairing instead. 
# this key-value pair allows users to quickly grab objects without needing to know an index location

#dictionaries and lists

# Dictionaries are objects retrieved by key name. They are unordered and can not be sorted.

# lists are objects retrieved by location. Ordered Sequence can be indexed or sliced.

dict1 = {"name": "Nathalie"}

print(dict1['name'], "dict1 example")

dict2 = {
    "name": "Daniel", 
    "admins": {"admin1": "Jonathan", "admin2": "David"}
    }


print(dict2['admins']['admin1'], "print out nested dictionaries")


# can use the power of dictionaries to have nested dictonaries hold lists

# example1

dict3 = {"list1": ["apple", "pear", "peach"]}
print(dict3['list1'][2])
# will return peach

# you can add a new key value pair to a dictonary. 
# example

dict3["list2"] = "groceries for the week"
print(dict3)
#{'list1': ['apple', 'pear', 'peach'], 'list2': 'groceries for the week'}

# you can print out either all the keys or all the values of a dictonary with a method. The methods are
# .keys() and .values()

#example

print(dict3.keys(), "the keys for dict3")
# (['list1', 'list2'], 'the keys for dict3')
print(dict3.values(), "the values for dict3")
#([['apple', 'pear', 'peach'], 'groceries for the week'], 'the values for dict3')

# another method is .items() This allows to show its key value pair in a tuple form
print(dict3.items(), "item method results")
# ([('list1', ['apple', 'pear', 'peach']), ('list2', 'groceries for the week')], 'item method results')

# the keys for dictionaries should be strings.