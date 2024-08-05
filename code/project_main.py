from geopy.geocoders import Nominatim # This is what we use to get longitude / latitude from a location name

import openmeteo_requests


locationDictionary = {}

# We create a class so we can reuse this for multiple locations whilst returning multiple values (Longitude and Latitude).
class GeoLocation: 
    def __init__(self, locationName):
        geolocator = Nominatim(user_agent="jrh-yr9-project")
        location = geolocator.geocode(locationName)
        self.longitude = location.longitude
        self.latitude = location.latitude

# Registers location to a dictionary, so we can keep it for later.
def registerLocation(locationInput):
    location = GeoLocation(locationInput)
    locationDictionary[locationInput] = {"longitude": location.longitude, "latitude": location.latitude}



def tempRepeat():
    locationRaw = input("Location Name: ")
    registerLocation(locationRaw)
    print(locationDictionary)
    tempRepeat()

tempRepeat()