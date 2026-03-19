class FordCars:
    def __init__(self, color, speed, name, body, interior):
        self.color= color 
        self.speed= speed 
        self.name= name
        self.body= body
        self.interior= interior
    
    def startEngine(self):
        print(self.name + " engine started.")

    def seating(self):
        if self.interior == 'leather':
            print(self.name + " only has 2 seats")

def doSomethingCool():
  print("wow")

def doSomethingElseCool():
  print("Decent")

