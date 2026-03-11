# 1. In your own words, What is a Python module / library?
# Please write your answer as a string.

"code that can be called from another location."
"developers do not need to write all the functions just call it. "

" A module is a document that contains classes that we can call on from"
"another location to use its properties and methods (functions) "

# 2. Inside your unit 2 folder, create a new document called
# userModule.py. Then, Create a class that creates 
#  a car model class. Your class should 
# have 3 properties and 2 methods.

import userModule_p3

# 3. In this document (moduleActivity) import your car class and create
# car objects. Print out the name and brand of the car 
# and use 1 method on each car.

car1 = userModule_p3.FordCars("red",40, "bronco", "wide", "red")
car1.startEngine()

print(car1.name)
