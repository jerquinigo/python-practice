# Object oriented programming (OOP)
#allows programmers to create their own objects that have methods and attributes.
 
# OOP allows users to create their own objects. OOP allows us to create code that is repeatable and organized.

# class NameOfClass():

   # def __init__(self,param1, param2):
      #  self.param1 = param1
     #   self.param2 = param2

     #init method allows you to create an instance of the object

    # self is a keyword  and it is used to call the object itself and work with the params. By doing this, it will link it to the object itself.

    #def some_method(self):
        #perform some action
        #print(self.param1)

    # the second function allows for the whole initial object to enter. Printing self.param1 will print out param1


    # example of an inital object with python 

# class People():
#   def __init__(self,personName):
#     self.person = personName


# person1 = People("jonathan")

# print(person1.person)


# example to understand self more
# class People():
#     # Attributes
#     # we take in the argument
#     # assign it using self.attribute_name
#   def __init__(self, personName):
#     self.my_attribute = personName


# person1 = People("jonathan")
# print(person1.my_attribute)


# an example with many attributes 

# class People():
#   def __init__(self, personName,age):
#     self.personName = personName
#     self.age = age


# person1 = People("jonathan", 28)
# print(person1.personName)
# print(person1.age)


## class object attributes and methods


# using class object attributes and methods 
# class People():
#   # CLASS OBJECT ATTRIBUTE will always have to be true for the instance of the class
#   speciesType = "human"

#   def __init__(self, personName,age):
#     self.personName = personName
#     self.age = age

#   def gretting(self):
#     print("hello, my name is {}".format(self.personName))

# person1 = People("jonathan", 28)
# print(person1.speciesType)
# person1.gretting()