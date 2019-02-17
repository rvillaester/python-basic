import requests
import math
from haversine import *

myLat = -33.86882
myLong = 151.209296

#{"fall":"Fell","geolocation":{"type":"Point","coordinates":[6.08333,50.775]},"id":"1","mass":"21","name":"Aachen","nametype":"Valid","recclass":"L5","reclat":"50.775000","reclong":"6.083330","year":"1880-01-01T00:00:00.000"}

def getMeteorData():
    res = requests.get('https://data.nasa.gov/resource/y77d-th95.json', verify=False)
    return res.json()

def addDistanceToMeteorData(data):
    for d in data:
        if not ('reclat' in d and 'reclong' in d):
            continue
        d['distance'] = calculateDistance(float(d['reclat']), float(d['reclong']), myLat, myLong)

meteorData = getMeteorData()
#print(type(meteorData), meteorData)
addDistanceToMeteorData(meteorData)
meteorData.sort(key=lambda d: d.get('distance', math.inf))
#print(meteorData)
data = meteorData[0]
print('The nearest meteor landing is in {} with distance of {}'.format(data['name'], data['distance']))

#https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh
#https://www.findlatitudeandlongitude.com/
#https://data.nasa.gov/resource/y77d-th95.json