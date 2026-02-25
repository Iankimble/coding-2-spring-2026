# Create a pet animal class function. 
# The class should have 4 properties and 4 methods. 

# Then create 3 pets objects. Each pet should have unique 
# properties and use at least 1 method.

class Pet_Constructor:
    def __init__(self, name, type, age, color):
        self.name = name
        self.type = type
        self.age = age
        self.color = color

    def wildness(self, food):
        if food == 0:
            print(self.name +' has a attitude and made a mess in the living room.')        
        else:
            print(self.name + ' is calm because they ate.')

    def sleep(self):
        print(self.name +' is tired.')

    def bathroom(self):
        print(self.name +' needs to go potty.')

pet_1 = Pet_Constructor('Brutus','Dog', 4,'Black')
pet_2 = Pet_Constructor('Slime','Snake',5, 'Whiite')
pet_3 = Pet_Constructor('Mittenz','Cat',7, 'Black and Grey')

pet_1.wildness(0)