# Python OOP - Object Oreinted Programming

# Object - A representation 
# of some complex data structure.
# *data = data types (... and functions in this case)
# Although they maybe the same thing, objectively, objects
# can have different characteristics/ features

# Class - a blueprint for creating objects. 

# Properties = the datatype values of a object.

class Computers:
    def __init__(self, name, brand, color, shape, storage, portability, camera, ram, processor, price):
        self.name = name
        self.brand = brand
        self.color = color
        self.shape = shape
        self.storage = storage
        self.portability = portability
        self.camera = camera
        self.ram = ram
        self.processor = processor
        self.price = price

        def bluetoothConnection(self):
            print("")

        def internetConnectivity(self):
            print("")
        
        def powerOn():
            print("")
        
        def calculator():
            print()

        def camera():
            print()

class Phones:
    def __init__(self, storage, carrier, size, color, camera, name, warrenty, price,brand):
        self.storage = storage 
        self.carrier = carrier
        self.size = size
        self.color = color
        self.camera = camera
        self.name = name
        self. warrenty= warrenty
        self.price = price
        self.brand = brand

    

        # def hasWarrenty():
        #     if warrenty== True:
        #         print('replacement')
        #     else:
        #         print('sorry thats gonna be another 2k, sir')        

phone1 = Phones(16, 'att', 13.00,'yellow', False, 'brick Pro', False, 100.00,'brick')
phone1 = Phones(32, 'verizon', 7.00,'blue', False, 'brick mini', False, 100.00,'brick')

#apple_1 = Computers("apple m4", "black", 10.00, 320, True, True, 120, 'm4')
#apple_2 = Computers("apple m4", "white", 10.00, 320, True, True, 80, 'm4')

#print(apple_1.ram)
#print(apple_2.ram)
