"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list
import numpy as np
from floodsystem.utils import sorted_by_key

def haversine(coord1, coord2):
    """Returns the distance between two points given their coordinates in 
    a tuple or list using the definition of a haversine """
    
    #Converting latitude and longitude into radians
    lat1 = (coord1[0]*np.pi)/180
    lat2 = (coord2[0]*np.pi)/180
    long1 = (coord1[1]*np.pi)/180
    long2 = (coord2[1]*np.pi)/180
    
    #Radius of earth
    r = 6371000
    
    #Using definition of haversine to find distance
    return 2*r*np.arcsin(np.sqrt(np.sin((lat2-lat1)/2)**2+np.cos(lat1)*np.cos(
            lat2)*np.sin((long2-long1)/2)**2))

def station_by_distance(stations, p):
    """ This function returns a list of (station, distance) tuples,
    where distance(float) is the distance of the station(MonitoringStation)
    from the coordinate p given a list of stations """
    
    #Initialising variables
    latlong = []
    b = []
    towns = []
    names = []
    data = build_station_list()
    d = []
    ls=[]
    
    for n in range(0, len(data)):
        #Creating a dummy MonitoringStation
        ID = data[n]
        for x in range(0, len(stations)):
            if stations[x] == ID.name:
                #If name of dummy is in list, add its coordinates to latlong
                latlong.append(ID.coord)
                towns.append(ID.town)
                b.append(ID.name)
            else:
                pass
            
    #Find distance from every item in latlong to coordinate
    for y in range(0, len(latlong)):
        d.append(haversine(latlong[y], p))
    
    #Create sorted list of tuples
    for z in range(0, len(stations)):
        ls.append((b[z],towns[z], d[z]))
    
    #Sort list by smallest distance
    ls = sorted_by_key(ls, 2)
    
    return ls





