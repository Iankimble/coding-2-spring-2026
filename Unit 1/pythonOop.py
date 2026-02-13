# Python OOP - Object Oreinted Programming

# Object - A representation 
# of some complex data structure.
# *data = data types (... and functions in this case)
# Although they maybe the same thing, objectively, objects
# can different characteristics/ features

# Class - is a constructor/ blueprint for creating
# objects. 

class computers:
    def __init__(self, name, color, shape, storage, portability, camera, ram, processor):
        self.name = name
        self.color = color
        self.shape = shape
        self.storage = storage
        self.portability = portability
        self.camera = camera
        self.ram = ram
        self.processor = processor
    
apple_1 = computers("apple m4", "black", 10.00, 320, True, True, 60, 'm4')

