# List comprehensions are a unique way of quickly creating a list with Python
# if you find yourself using a for loop along with .append() to create a list, List comprehension are a good alternative

# the long way to create a list

name1 = "nathalie"
list1 = []

for letter in name1:
    list1.append(letter)

print(list1)
#['n', 'a', 't', 'h', 'a', 'l', 'i', 'e']

# the more efficient way/ or another way 

list2 = [letter for letter in name1]
print(list2, "the flatten out for loop")
# ['n', 'a', 't', 'h', 'a', 'l', 'i', 'e'] the flatten out for loop

# can do the logic in a flatten out for loop in the variable itself

# syntax for flatten for loops are element for element in itemToLoop

# squaring numbers in the flatten for loop and using range is possible

list3 = [num**2 for num in range(1,21)]
print(list3, "the result of the square")
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400] the result of the square

# can also combine if else statements in a flatten for loop

list4 = [num for num in range(1,21) if num % 2 == 0]
print(list4, "the modulus return ")
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] the modulus return

# can also handle more complex arithmetic

celcius = [0,10,20,34.5]
fahrenheit = [(9/5*temp+32) for temp in celcius]
print(fahrenheit, "the results for the conversions")

#[32.0, 50.0, 68.0, 94.1] the results for the conversions

# second way to do it

fahrenheit2 = []
for temp in celcius:
    fahrenheit2.append((9/5)* temp + 32)

print(fahrenheit2, "results the long way")
#[32.0, 50.0, 68.0, 94.1] results the long way


# can do an if else statement in a flatten for loop (list comprehension)

results1 = [x if x % 2 == 0 else "ODD" for x in range(0,11)]
print(results1, "the results for flatten for loop with if else logic")
# [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10] the results for flatten for loop with if else logic

# can do nested loops in list comprehension
# fore showing a nested loop in list comprehension, lets do two for loops the long way


ylist1 = []

for x in [2,4,6]:
    for y in [100,200,300]:
        ylist1.append(x*y)
print(ylist1, "the two for loops result")
#[200, 400, 600, 400, 800, 1200, 600, 1200, 1800] the two for loops result

# the list comprehension way

ylist2 = [x*y for x in [2,4,6] for y in [100,200,300]]

print(ylist2, "list comprehension way")
#[200, 400, 600, 400, 800, 1200, 600, 1200, 1800] list comprehension way


# note you can print out what a method can do using the help() function
list99 = [1,2,3]
print(help(list99.insert))