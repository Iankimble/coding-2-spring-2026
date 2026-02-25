# Create a pet animal class function. The class should have 4 properties 
# and 4 methods. 

# Then create 3 pets objects. Each pet should have unique 
# properties and use at least 1 method.

class PetCreator:
    def __init__(self, color, age, name, attitude, type):
        self.color= color
        self.age= age
        self.name= name
        self.attitude= attitude
        self.type = type

    def feedPet(self):
        print(self.name + ' is hungry')
        print("time to feed your pet")

    def sleeping(self):
        print(self.name + ' is tired')
        print("our pet is resting.")

    def playtime(self):
        print(self.name + ' is bored')
        print("our pet want to play a game.")
    
    def bathroom(self):
        print("needs to relieve itself")

    def fetchGame(self):
        ball = ''
        caught = False
        print("throw")
        if ball == caught:
            print(self.name +' caught the ball')
        else:
            print(self.name +' did not catch ball')


pet_1 = PetCreator("brown", 4, "Brutus", "Friendly", "  Dog")
pet_2 = PetCreator("grey", 6, "Sam", "Independent", "Cat")
pet_3 = PetCreator("green", 2, "Iggy", "Timid", "Lizard")

pet_1.feedPet()
