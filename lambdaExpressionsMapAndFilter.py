def square(num):
    return num**2

myNums = [1,2,3,4,5]

# map took in the function square in the first argument and then the variable list in the second argument. We then looped through it and printed the results of it squared
for item in map(square, myNums):
    print(item)

#1
#4
#9
#16
#25

# this way will put the results in a list format
print(list(map(square,myNums)))
# [1, 4, 9, 16, 25]