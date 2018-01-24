"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list
import numpy as np
from floodsystem.utils import sorted_by_key
from dateutil import parser
from datetime import *
import plotly.plotly as py
import plotly


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
    #Checks if river is in dictionary and adds river and/or station
    #accordingly
    for station in stations:
        if station.river not in stationsbyriver:
            stationsbyriver[station.river]=[station.name]
        else:
            stationsbyriver[station.river].append(station.name)
    return stationsbyriver

def rivers_by_station_number(stations, N):
    """Determines the N rivers with the greatest number of monitoring
    stations"""
    #Creates empty dictionary for storing number of stations per river
    rivers={}
    #Checks if river is in dictionary and adds river and/or increases
    #station count accordingly
    for station in stations:
        if station.river not in rivers:
            rivers[station.river]=1
        else:
            rivers[station.river]+=1
    #Creates empty list for rivers
    rivers_list=[]
    #Converts dictionary keys and values into tuples and adds them to list
    for key, value in rivers.items():
        rivers_list.append((key, value))
    #Sorts tuples by number of stations
    rivers_list.sort(key=lambda tup: tup[1], reverse=True)
    #Adds first N rivers to final list
    first_N_rivers=rivers_list[:N]
    #Adds rivers with the same number of stations as the last river in
    #final list
    for n in range(N, len(rivers_list)-1):
        if first_N_rivers[-1][1]==rivers_list[n][1]:
            first_N_rivers.append(rivers_list[n])
        else: break
    return first_N_rivers

#You are now entering the Jeroen Sector - proceed with caution

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
        
def present_on_map(stations):
    """ Presents station on map of UK with colour intensities related to 
    typical high range. """
    
    #Log in to plotly
    plotly.tools.set_credentials_file(username='joliesla', 
                                      api_key='f4LO82wNWQlR4JUh2wpF')
    
    #Initialise variables
    long = []
    lati = []
    desc = []
    level = []
    
    #Create lists of required data
    for station in stations:
        if station.typical_range == None:
            pass
        elif station.river == None:
            pass
        elif station.town == None:
            pass
        else:
            long.append(station.coord[1])
            lati.append(station.coord[0])
            desc.append(station.name + 
                        station.town + 
                        station.river + 
                        str(station.typical_range[1]))
            level.append(station.typical_range[1])
        
    #Set colour scale for legend
    scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],
             [0.5,"rgb(70, 100, 245)"],[0.6,"rgb(90, 120, 245)"],
             [0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]
    
    #Create dictionary for scatter map data
    data = [dict(
            type = 'scattergeo',
            locations = 'GBR',
            lon = long,
            lat = lati,
            text = desc,
            mode = 'markers',
            marker = dict(
                size = 8,
                opacity = 0.8,
                reversescale = True,
                autocolorscale = False,
                symbol = 'circle',
                line = dict(
                    width=1,
                    color='rgba(102, 102, 102)'
                ),
                colorscale = scl,
                cmin = 0,
                color = level,
                cmax = max(level),
                colorbar=dict(
                    title="Water Levels UK"
                )
            ))]
     
    #Create layout for map    
    layout = dict(
        title = 'Water levels UK<br>(Hover for station names)',
        colorbar = True,
        geo = dict(
            scope='europe',
            projection=dict( type='mercator' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )
     
    #Put together map and data
    fig = dict(data=data, layout=layout)
    py.plot(fig, validate=False, filename='UK-water_levels')
    
        
    
     



