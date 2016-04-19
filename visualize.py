import json
from data import google_location_data

with open(google_location_data) as dataFile:
    data = json.load(dataFile)
    locations = data["locations"]
    print len(locations)