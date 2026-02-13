# 1. Create a function that checks the price of an item, and depending 
# on the item they will get a specific discount amount. Your function
# should take in the item price as an input from the user. If the user's
# item costs between 50 and 75 dollars, they will get a 15% discount.
# If the item is above 75 dollars, they will recieve a 25% discount.
# Your program should print out and inform the user how much of a 
# discount they will get and what the new total for the item be with 
# the applied discount. 

# Take a price and depending on the price amount the user will get 
# a 15%, 25% discount or no discount.

# input - we need to take in the item price as an input
# the output needs to calculate and show the disccount amount
# needs to be a function
# if price is > 50 but < than 75 = should get 15% off
# if pricce  > 75 = should be 25% off
# conditonal statement if/ else

def discount():
    price = int(input("how much is the item? "))
    if price > 50 and price < 75:
        sum = price * .15
        total = price - sum
        print(sum)
        print("your new total is "+ str(total))
    elif price > 75:
        sum = price * .25
        total = price - sum
        print(sum)
        print("your new total is "+ str(total))        
    else:
        print("Sorry, no discount")

#discount()


# 2. Create a function that will check a users age and GPA 
# and determine if they qaulify to attend the job fair. 
# Your function should take the user's age and GPA in as parameters. 
# If the user is above 17 and has atleast a 90 or above GPA they 
# can go to the job fair. Otherwise they are not permitted to go.

def gpa(age, gpa):
    if age >= 17 or gpa >= 90:
        print("you can go to the job fair")
    else: 
        print("sorry you do not meet the requirements.")

gpa(17, 86)









# 3. Create a function that will loop through a list, 
# remove all the grades lower than 85, and then print out 
# the GPA with only the numbers above 85.  

myGrades =[76, 87, 79, 84, 100, 81, 99, 72, 100, 98, 91]



