# Library - stores books and information --> generally quite

# Python Library - a file or folder that contains objects, functions, and data
# that we can access quickly. These collections of logic are created by other 
# programmers who wanted to share their code, to make it easier for others. 

# Modules == Libraries *they are the same

# to access a library/ module, we use the import keyword
import random

print(random.randrange(1, 10))

# modules/ libraries help us to speed up development time and write less code,
# because someone already wrote it for us.

# local modules - functions and data from another document in our folder 
# structure

import example

student1 = example.Student(20,'college','Billy', False)

print(student1.name)
print(student1.is_in_uniform())

