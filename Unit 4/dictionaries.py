# A dictionary is a collection type that uses key / value pairs to 
# describe data. Its a simpler and faster form of objects. 


# A dictionary is very similar to a class.
# dictionaries ONLY focus on key value pairs. 
# NO methods

finals= {
    "name": "Finals Testing",
    "time": "9 AM",
    "date":"May 11",
    "grades":"9-11"
}

srProm= {
    "name": "Senior Prom",
    "time": "9 PM",
    "date":"May 8",
    "grades":"12"
}

srTrip= {
    "name": "Senior Feild Trip",
    "time": "10 AM",
    "date":"May 22",
    "grades":"12"
}

graduation= {
    "name": "Graduation Day",
    "time": "11AM",
    "date":"May 27",
    "grades":"12"
}

# dictionaries dont have indexes but rather they have keys
# key are the name/property type that contains the actual data. 

#print(graduation["date"])

maySchedule = [finals, srProm, srTrip, graduation]

print(maySchedule)

for event in maySchedule:
    print(event['name'])
    