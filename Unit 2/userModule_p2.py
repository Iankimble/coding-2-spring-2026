
class CarModel:
    def __init__(self, model, color, motor, year):
        self.model= model
        self.color= color
        self.motor= motor
        self.year= year

    def colorDetails(self):
        print('the car details are below: ')
        print("car model =  " + self.model)
        print('car color =  ' + self.color)

    def speed(self):
        mph = self.motor * 3
        print("car model =  " + self.model)
        print("the maximum speed for this car is =  " + str(mph))







def drive():
    print('car is going!!!!')

grades = [12, 3443, 343, 23,23423, 435]