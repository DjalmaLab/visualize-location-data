import json
from data import google_location_data
from locationObj import LocationObj
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import sys

def fixLatLon(latLon):
    return latLon * 0.0000001

myLocations = []
with open(google_location_data) as dataFile:
    data = json.load(dataFile)
    locations = data["locations"]
    for location in locations:
        try:
            location["altitude"]
        except:
            location["altitude"] = 0
        lat = fixLatLon(location['latitudeE7'])
        lon = fixLatLon(location["longitudeE7"])
        myLocations.append(LocationObj(location["timestampMs"],
                                        lat,
                                        lon,
                                        location["altitude"]))

fig = plt.figure(figsize=(20,10))

map = Basemap(projection='gall',
                ellps='WGS84',
                resolution='h',
                area_thresh = 1000000.0,
                lat_0=37.5, lon_0=-119,
                llcrnrlat=35, urcrnrlat=41,
                llcrnrlon=-124, urcrnrlon=-121)
# Draw the coastlines on the map
map.drawcoastlines()

# Draw country borders on the map
map.drawcountries()

# Fill the land with grey
map.fillcontinents(color = '#888888')

map.drawstates()
# Draw the map boundaries
map.drawmapboundary(fill_color='#f4f4f4')

i = 0
for location in myLocations:
    x, y = map(location.getLon(), location.getLat())

    map.plot(x, y, 'ro', markersize=6)
    i+=1
    if i > 10000:
        break


plt.show()