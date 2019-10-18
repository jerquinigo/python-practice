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