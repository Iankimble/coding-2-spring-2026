# 3. Create a class named Smartphone.

# The Constructor (__init__): Should
#  accept 3 parameters; brand, model, and battery_level 
# (an integer).

# Your class should have a method called charge. 
# This method should use a loop to continuously add
#  10 to the battery_level if the user selects yes to 
# charge. If the battery gets to 100, the loop should 
# stop and tell the user the battery is charged.

# There should another method called get_status. 
# This should print out a string that shows the phone 
# object Brand and model.

class Smartphone:
    def __init__(self,brand, model, batteryLevel):
        self.brand = brand
        self.model= model
        self.batteryLevel = batteryLevel
    

    def charge(self):
        print("your battery level is currently "+ str(self.batteryLevel))
        charge = input("whould you like to charge your phone? hit y to charge and n to not charge ")
        if charge == "y":
            while self.batteryLevel < 100:
                self.batteryLevel += 10
                print(self.batteryLevel)
                charge = input("do you want to continue charging?")
            else:
                print("your battery level is "+ str(self.batteryLevel))

    def getStatus(self):
        print("here is your phone info: "+ "brand=" + self.brand + " model = "+ self.model)    

momPhone= Smartphone('apple','17',20)
dadPhone= Smartphone('android','28',30)

momPhone.getStatus()
dadPhone.charge()



# 5. Create a function that will multiply a numbers between 
# the range of 1 and 10 by another number passed into the 
# function as a parameter. Your function should use a loop to 
# go through the range of numbers. 


def multiply_x(number):
    x = range(1, 11)
    for n in x:
        print(number *n)

multiply_x(23)