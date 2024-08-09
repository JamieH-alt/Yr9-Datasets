from geopy.geocoders import Nominatim # This is what we use to get longitude / latitude from a location name

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import openmeteo_main

locationDictionary = {}
dataframes = []

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
    locationDictionary[locationInput] = {"name": locationInput, "longitude": location.longitude, "latitude": location.latitude}

def mapTemperatures():
    for entry in locationDictionary:
        locationDictionary[entry]["dataframe"] = openmeteo_main.getDataframe(locationDictionary[entry]["latitude"], locationDictionary[entry]['longitude'])
        dataframes.append(locationDictionary[entry])
    firstplot = dataframes[0]["dataframe"].plot(kind="line", x="date", y="temperature_2m", xlabel="Date", ylabel="Temperature (Celsius)", label=dataframes[0]["name"])
    for i in range(0, len(dataframes)):
        if i == 0:
            continue
        dataframes[i]["dataframe"].plot(kind="line", x="date", y="temperature_2m", xlabel="Date", ylabel="Temperature (Celsius)", label=dataframes[i]["name"], ax=firstplot)
    plt.show()


def tempRepeat():
    locationRaw = input("Location Name: ")
    registerLocation(locationRaw)
    if (input("exit: ") == "y"):
        mapTemperatures()
    else:
        tempRepeat()

tempRepeat()