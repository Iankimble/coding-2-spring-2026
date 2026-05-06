# # 3. Create a class named Smartphone.

# # The Constructor (__init__): Should accept 3 parameters;
# #  brand, model, and battery_level (an integer).

# # Your class should have a method called charge. This method
# #  should use a loop to continuously add 10 to the battery_level 
# # if the user selects yes to charge. If the battery gets to 100, the 
# # loop should stop and tell the user the battery is charged.

# # There should another method called get_status. This should 
# # print out a string that shows the phone object Brand and model.

# class Smartphone:
#     def __init__(self, brand, model, battery_level):
#         self.brand = brand
#         self.model = model
#         self.battery_level = battery_level

#     def charge(self):
#         print("current battery level = " + str(self.battery_level))
#         charge= input("Would you like to charge? Enter y to charge and n to NOT charge.")
        
#         if charge == 'y':
#             while self.battery_level < 100:
#                 self.battery_level += 10
#                 print("new battery level = "+ str(self.battery_level))
#                 charge = input("Would you like to continue charging? ")     
#         else:
#             print("current battery level = " + str(self.battery_level))
    
#     def get_status(self):
#         print("Here is your phonne info: " +" phone brand = "+ self.brand + ". Phone model = " + self.model)

# momPhones = Smartphone("Apple", "iPhone 17 Pro", 30)
# brotherPhone = Smartphone("Samsung Android", "Galaxy 28", 40)

# momPhones.get_status()
# brotherPhone.get_status()

# momPhones.charge()




# # 10. Create a function that checks if a user is eligible for a 
# # travel discount. Your function should take 2 parameters; hasRoom (boolean)
# #  and hasPlaneTicket(boolean).

# # - 1. if the user has a has booked a room and has a plane ticket, 
# # print out a message telling them they will get the gold discount

# # - 2. if the user has booked a room or a plane ticket, but does not have 
# # the other, printout a message telling them they will get the silver discount

# # - 3. if the user has neither booked a room or a plane ticket inform them 
# # they are not eligible for a plane ticket. 

# def travelDiscount(hasRoom, hasPlaneTicket):
#     if hasRoom == True and hasPlaneTicket == True:

# 3. What will be displayed after the code executes?

scoresList = [75, 92, 84, 95, 88]
maxScore = scoresList[0]
n = 2
x=0
for x in range(4):
    if(scoresList[n] > maxScore):
        maxScore = scoresList[n]
    n += 1
print(maxScore)