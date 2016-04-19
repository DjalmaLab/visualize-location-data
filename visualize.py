import json
from data import google_location_data
from locationObj import LocationObj
import sys

myLocations = []
with open(google_location_data) as dataFile:
    data = json.load(dataFile)
    locations = data["locations"]
    for location in locations:
        try:
            location["altitude"]
        except:
            location["altitude"] = 0
        myLocations.append(LocationObj(location["timestampMs"],
                                        location['latitudeE7'],
                                        location["longitudeE7"],
                                        location["altitude"]))
print len(myLocations)