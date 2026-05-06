# A dictionary representing a local Philly event
event = {
    "title": "Tech Town Hall",
    "location": "Free Library of Philadelphia",
    "topic": "Digital Resources",
    "attendees": 40
}

# prints all keys
for key in event:
    print(key)
#prints all values
for value in event.values():
    print(value)

#looping through list
scraped_events = [
    {"title": "Jazz in the Park", "venue": "Rittenhouse Square"},
    {"title": "Tech Mixer", "venue": "Science Center"},
    {"title": "Open Mic", "venue": "World Cafe Live"}
]

# returns all titles for events in list
for event in scraped_events:
    # 'event' is a dictionary
    print(f"Checking event: {event['title']}")

