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

# example

#list1 = [2,4,6,8,10]

#def mult2(li):
 # return li * 2


#print(list(map(mult2,list1)))

#for n in map(mult2, list1):
 # print(n)

 # this is iterating through the values of map

 # both ways will return 4,8,12,16,20

# need to put in the values in a list for the map to return the results
# also got to put in a function in the first argument and then the list you want to apply that data to.
# transform it to a list or iterate through it



# a lambda expression is also known as an anonomous function. (means its a function that we only use one time.)

# it is the same as a regular function in python. Instead of naming it, you would call it lambda and no return value needs to be present because it will be return 

#example
# traditional function
# def square(num):
#    return num ** 2

# lambda function is not named
# square = lambda num: num ** 2
# square(3)

## you can use lambda in place of the function 
#print(list(map(lambda num: num ** 2, [2,4,6])))
#[4, 16, 36]