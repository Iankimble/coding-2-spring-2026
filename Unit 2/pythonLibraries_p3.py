# Library = place that stores alot of books/ information. 

# Python Libraries/ Modules = files/folders that contain functions and data that we can
# use quickly and easily. These are code instructions that were already written
# for us. We just need to call it.

# We use the IMPORT keyword to bring in libraries/ modules into our code.
# import example

# built-in module - a object that is already built in to the programming language. 
import random

number = random.randrange(0,10)

print(number)

# local modules - object that stored inside of a fille in our system. 
import example

newStudnt = example.Student('Billy', 90 ,10, 'NA',True, 10)
print(newStudnt.name)

print(newStudnt.graduationCheck())


