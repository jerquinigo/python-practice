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

class Circle():
    # class object attribute is something that always true with an instance of the class
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        # you can reference class object attribute cause it will always be the same in the class. you can reference it by Classname.variable example below
        self.area = radius * radius * Circle.pi
    
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle()
# can also do my_circle = Circle(30)
print(my_circle.get_circumference())
# prints out 6.28
print(my_circle.pi)
#prints out 3.14
print(my_circle.area, "the area")
# with the default values, it is 3.14. If it had 30 as radius, it comes out to 2826

# you can have a default value in the class and overwrite it when creating an instance of it and pass the arguments in the parenthesis.



### Inheritance and polymorphism

#Inheritance is defining new classes with classes that has already been defined
# first we create the base class

class Animal():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myAnimal = Animal()
print(myAnimal.eat())
print(myAnimal.who_am_i())

#we create a new class and it will be inheriting the base class
#passing in the class animal will inherit the base class for this new class
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("dog created")
        #^this will create an instance of Animal class when Dog class instance is created

        # you can overwrite methods from the parent class in the extended class. You will have to call it the same method name and then write what you want the new function to do
    def who_am_i(self):
        print("i am a dog")

myDog = Dog()
# we know have access to methods from Animal class into the Dog class. Using eat from Animals
print(myDog.eat())
#prints out I am eating
print(myDog.who_am_i())
# prints out i am a dog
