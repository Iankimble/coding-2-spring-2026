# 1. In your own words, What is a Python module / library?
# Please write your answer as a string.
"A collection of classes (unique functions) that are "
"already written for us that we can use."

# 2. Inside your unit 2 folder, create a new document called
# userModule.py. Then, Create a class that creates 
#  a car model class. Your class should 
# have 3 properties and 2 methods.


# 3. In this document (moduleActivity) import your car class and create
# car objects. Print out the name and brand of the car 
# and use 1 method on each car.

import userModule_p2

userModule_p2.drive()

car1 = userModule_p2.CarModel('Camry','black',60,2020)
car2 = userModule_p2.CarModel("Focus",'silver',80, 2021)

print(car1.model)
car2.speed()
car1.speed()

print(userModule_p2.grades)