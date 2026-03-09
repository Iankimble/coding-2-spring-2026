# 1. In your own words, describe what a class property is. Please write
# your response as a string.

"A variable that stores descriptive information about an object."
"These descriptors will be data types."

# 2. In your own words, describe what a class method is. Please write your 
# response as a string. 

"A function that resides inside of a class."

# 3. Create a student class function. This function should create unique student
# objects. Your class needs to have 4 properties and 3 methods.
# Once you created you class, create 2 student objects. Each
# should be using a method from your class.

class Student:
    def __init__(self, name, grade, age, major, present, credit):
        self.name= name 
        self.grade= grade
        self.age= age
        self.major= major 
        self.present= present
        self.credits = credit

    def attendence(self):
        if self.present == False:
            print(self.name + ' is absent.')
        else:
            print(self.name + ' is present.')

    def graduationCheck(self):
        if credits < 18:
            print(self.name +" needs "+  " to graduate")
        else:
            print("Congrats you can graduate")
    
    def internshipCheck(self):
        if self.age < 16.5:
            print('you are too young for internship')
        else:
            print('cool please complete application')

    def gradeChecker(self):
        if self.grade < 59:
            print("Sorry you are behind in your studies")
        elif self.grade > 60 and self.grade < 69:
            print("You have a D letter grade.")
        elif self.grade > 70 and self.grade < 79:
            print("You have a C letter grade.")
        elif self.grade > 80 and self.grade < 89:
            print("You have a B letter grade.")     

student1 = Student('Barry',70, 16, 'Political Science',True, 15)
student2 = Student('Wilma',85, 17, 'Engineering',False, 19)

student1.graduationCheck()
student2.graduationCheck()


# 4. Create a video game character class function. This function 
# should create a basic video game character object. 
# The character can be inspired by fanatasy games or sports games. 
# Your class needs to have 4 properties and 3 methods.
# Once you created you class, create 2 video game character objects.
# each should be using a method from your class


class VGC:
    def __init__(self, name, health, moveList, equip, ammo, archetype,ability):
        self.name= name # String
        self.health= health # Integer  
        self.moveList= moveList # List [{},{},{}]
        self.equip = equip
        self.ammo = ammo
        self.ability= ability
        self.archetype= archetype 

        def typeAdvantage(self,opp):
            if opp.archetype == "grass":
                print("advantage")

        def triggerAbility(self):
            if self.ability == 'static':
                print()
            elif self.ability == 'lightning rod':
                print()

        def fireWeapon(equip, ammo):
            print("")
        
        def attackOne(inputData):
            if inputData == 'a,r,up, down':
                print('attack')


