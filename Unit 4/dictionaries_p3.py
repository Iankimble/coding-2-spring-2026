# A python dictionary is a collection type that store values that describe 
# unique data. 
# IT IS AN OBJECT!
# Its similar to a class object but with less rules. 
# There are no methods on dictionaries

srProm= {
"name": "senior prom",
"date": "May 8th, 2026",
"gradeLevel":"12th"
} 

srFieldTrip= {
    "name":"senior Field Trip",
    "date": "May 22nd, 2026",
    "gradeLevel": "12th",
    "timeLeaving":"6 AM",
    "timeReturning":"12 AM"
}

graduation= {
    "name":"Graduation Day",
    "date": "June 2nd, 2026",
    "grade": "12th"
}

# print(graduation["date"])

# class is function that CREATES OBJECTS- these objects need to follow the class
# rules
# dicionaries are natural objects
class event():
    def __init__(self, name):
        self.name= name,

events = [graduation, srFieldTrip, srProm]

#print(events)

for special_Occassion in events:
    print(special_Occassion["name"] + " - " + special_Occassion['date'])
