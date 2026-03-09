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
        if self.credits < 18:
            print(self.name +"has" + str(self.credits))
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
