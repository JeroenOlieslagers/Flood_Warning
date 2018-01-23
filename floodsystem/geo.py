"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list
import numpy as np
from floodsystem.utils import sorted_by_key
from dateutil import parser
from datetime import *


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

def age_in_years(d1):
    """ Function that takes in dateOpened format dates from JSON file
    and calculates how many years there are between it and the current date"""
    
    #Get today's date
    d2 = date.today()
    
    #Convert d1 to datetime object
    d1 = parser.parse(d1).date()
    
    #Calculates age in days and rounds to nearest year
    return round(abs((d2 - d1).days)/365.25)
    
    
def station_by_distance(stations, p):
    """ This function returns a list of (station, distance) tuples,
    where distance(float) is the distance of the station(MonitoringStation)
    from the coordinate p given a list of stations """
    
    #Initialising variables
    ls=[]
    
    #Add stations and distance of station from p to list
    for station in stations:
        ls.append((station, haversine(station.coord, p)))
    
    #Returns list sorted by distance
    return sorted_by_key(ls, 1)

def stations_within_radius(stations, centre, r):
    """ This function returns a list of all stations (type MonitoringStation) 
    within radius r of a geographic coordinate centre."""
    
    #Initialising variables
    ls = []
    
    #Add Check if distance of station to centre is less than radius
    for station in stations:
        if haversine(station.coord, centre) < r:
            ls.append(station)
        else:
            pass
    
    return ls

def stations_by_opening_date(stations):
    """ Returns a list of stations (type MonitoringStation) in ascending order
    of age and also displays the age."""
    
    #Initialising variables
    ls = []
    
    #Add stations and age from current date to list
    for station in stations:
        ls.append((station, age_in_years(station.dateOpened)))
    
     



