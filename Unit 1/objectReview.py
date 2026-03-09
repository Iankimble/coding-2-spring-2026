# 1. In your own words, describe what a class property is. Please write
# your response as a string.

"properties are just characteristics onn a class/ object."

# 2. In your own words, describe what a class method is. Please write your 
# response as a string. 

"methods are just functions inside  of a class/ object."

# 3. Create a student class function. This function should create unique student
# objects. Your class needs to have 4 properties and 3 methods.
# Once you created you class, create 2 student objects. Each
# should be using a method from your class.

class Student:
    def __init__(self, age, grade, name, uniform):
        self.age= age
        self.grade= grade
        self.name= name
        self.uniform= uniform 
        
    def is_in_uniform(self):
        if self.uniform == False:
            print("this studennt has detention.")
        else:
            print("student is good. no detention.")

    def study(self, subject):
        print(self.name + " is studying for " + subject)

    def updateGrade(self):
        score = test()
        average = 95
        average += score
        average /= 5
        print(average)

def test():
    score = 0
    print('1. what is the capital of PA')
    answer= input()
    if answer == 'harrisburg':
        score +=1
    print('2. what 2 + 2')
    answer= input()
    if int(answer) == 4:
        score +=1
    print('test complete here is your score')
    print(score)
    return score

student1 = Student(15, 10, 'John', True)
student2 = Student(17, 11, 'Rick', False)

student1.is_in_uniform()
student2.updateGrade()

# 4. Create a video game character class function. This function 
# should create a basic video game character object. 
# The character can be inspired by fanatasy games or sports games. 
# Your class needs to have 4 properties and 3 methods.
# Once you created you class, create 2 video game character objects.
# each should be using a method from your class

score = 0

class VGC:
    def __init__(self, name, health, archetype, power,ammo,shootingPercent):
        self.name= name
        self.health= health
        self.archetype= archetype
        self.power= power
        self.ammo= ammo
        self.shootingPercen= shootingPercent

    # method FPS games
    def fireWeapon(self, weapon):
        if self.ammo != 0:
            weapon(self.ammo) # fire the weapon function
        else:
            print('out of ammo')

    # method Fighting games
    def block(self, damage):
        damage = 0
        return damage

    def normalAttack(self,hitConnects, opponent):
        if hitConnects:
            opponent.health -= self.power
        
    # method (Any) Sports games
    def shooting_2pt(self,shootingPercent):
        if shootingPercent > 70:
            print('score')
            score += 2 

    def shooting_3pt(self, shootingPerccent):
        if shootingPerccent> 90:
            print('score')
            score += 2 






