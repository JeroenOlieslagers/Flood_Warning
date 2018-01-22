"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list
import numpy as np
from floodsystem.utils import sorted_by_key


def rivers_with_station(stations):
    """Returns all rivers by name with a monitoring station"""
    #Creates empty list of rivers
    rivers = []
    #Adds station rivers to list if station is attributed to a river
    for station in stations:
        if station.river!=None:
            rivers.append(station.river)
    #Converts list of rivers to a set, removing duplicates
    rivers_set = set(rivers)
    return(rivers_set)

def stations_by_river(stations):
    """Returns a dictionary mapping river names to a list of stations
    on a given river"""
    #Creates empty dictionary of rivers
    stationsbyriver={}
    #Checks if river is in dictionary and adds river and/or
    #station accordingly
    for station in stations:
        if station.river not in stationsbyriver:
            stationsbyriver[station.river]=[station.name]
        else:
            stationsbyriver[station.river].append(station.name)
    return stationsbyriver

def haversine(coord1, coord2):
    """Returns the distance between two points in kilometres given their 
    coordinates in a tuple or list using the definition of a haversine """
    
    #Converting latitude and longitude into radians
    lat1 = (coord1[0]*np.pi)/180
    lat2 = (coord2[0]*np.pi)/180
    long1 = (coord1[1]*np.pi)/180
    long2 = (coord2[1]*np.pi)/180
    
    #Radius of earth
    r = 6371000
    
    #Using definition of haversine to find distance
    return (2*r*np.arcsin(np.sqrt(np.sin((lat2-lat1)/2)**2+np.cos(lat1)*np.cos(
            lat2)*np.sin((long2-long1)/2)**2)))/1000

def station_by_distance(stations, p):
    """ This function returns a list of (station, distance) tuples,
    where distance(float) is the distance of the station(MonitoringStation)
    from the coordinate p given a list of stations """
    
    #Initialising variables
    latlong = []
    b = []
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
                b.append(ID)
            else:
                pass
            
    #Find distance from every item in latlong to coordinate
    for y in range(0, len(latlong)):
        d.append(haversine(latlong[y], p))
    
    #Create sorted list of tuples
    for z in range(0, len(stations)):
        ls.append((b[z], d[z]))
    
    #Sort list by smallest distance
    ls = sorted_by_key(ls, 1)
    
    return ls

def stations_within_radius(stations, centre, r):
    """ This function returns a list of all stations (type MonitoringStation) 
    within radius r of a geographic coordinate centre."""
    #Initialising variables
    data = build_station_list()
     
     




