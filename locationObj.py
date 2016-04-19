class LocationObj(object):
    def __init__(self, time, lat, lon, altitude):
        self.time = time
        self.lat = lat
        self.lon = lon
        self.altitude = altitude

    def getLat(self):
        return self.lat
    def getLon(self):
        return self.lon