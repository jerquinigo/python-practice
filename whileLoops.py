# while loops will continue to execute a block of code while some condition remains True.
# ex. while my pool is not full, keep filling my pool with water until full

# syntax
# while someBooleanCondition:
#   do something

# can also combine a control flow operators with the while loop

#while someBooleanCondition:
    # do something
#else:
    # do something different

currentNum = 0

while currentNum < 10:
    print(f"the curent value of the number is {currentNum}")
    currentNum += 1
# white spacing is super important while setting up logic. If it is not set up correctly, it would be like putting the logic outside the curly braces in js.
#the curent value of the number is 0
#the curent value of the number is 1
#the curent value of the number is 2
#the curent value of the number is 3
#the curent value of the number is 4
#the curent value of the number is 5
#the curent value of the number is 6
#the curent value of the number is 7
#the curent value of the number is 8
#the curent value of the number is 9

# a while loop with an else statement

while currentNum < 10:
    print(f"the current number is {currentNum}")
    currentNum += 1
else: 
    print(f"after the loop number is {currentNum}")

#the curent value of the number is 0
#the curent value of the number is 1
#the curent value of the number is 2
#the curent value of the number is 3
#the curent value of the number is 4
#the curent value of the number is 5
#the curent value of the number is 6
#the curent value of the number is 7
#the curent value of the number is 8
#the curent value of the number is 9
#fter the loop number is 10

#  python also has a break, continue and pass statements

# break: breaks out of the current closest enclosing loop
#continue: goes to the top of the closest enclosing loop
# pass: does nothing at all


# example of pass 
# pass is great for setting up placeholder. There need to be code in the block of code or it will throw an error. Use pass as a placeholder

tempList = [1,2,3,4,5]

for item in tempList:
    pass
# pass is a keyword that is great as a placeholder
print("after the for loop example")

# continue tells the loop to go to the next enclosing loop after a condition been met

# example:
myString1 = "nathalie"

for letter in myString1:
    if letter == "h":
        continue
    print(letter)
#n
#a
#t
#a
#l
#i
#e

#will continue the loop ignoring what was declared from the condition


#break statement stops the loop when a condition is met

whileLoopNum = 0

while whileLoopNum < 10:
    if(whileLoopNum >= 5):
        break
    print(whileLoopNum)
    whileLoopNum += 1
# prints out up to 4 because of the break statement.

