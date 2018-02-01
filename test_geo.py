"""Unit test for the geo module"""

import pytest
from floodsystem.stationdata import build_station_list

def test_haversine():
    #Initialise list of lat and long coordinates of test variables
    coord = [(10, 10), (5, 12), (52.342,63.435), (63.234, 1.234)]
    
    #Initialise list of corresponding distances from (0,0) according to 
    # https://www.movable-type.co.uk/scripts/latlong.html
    ls = [1569, 1444, 8244, 7032]
    
    for n in range(0, len(ls)):
        assert round(haversine(coord[n], (0,0))) == ls[n]

def test_age_in_years():
    #Initialise variables
    ls = []
    age1 = [21, 21, 24, 26, 42]
    data = build_station_list()

    #Get age of dates
    ID = age_in_years(data[:5])
    for station, age in ID:
        ls.append(age)
    
    #Check if ages match
    for n in range(0, len(ls)):
        assert ls[n] == age1[n]

def test_station_by_distance():
    
    #Initialise variables
    data = build_station_list()
    distances = [20.1, 72.8, 132.5,161.7, 243.4]
    ls = []
    
    #Create list of all stations closest to Cambridge city centre
    ID = station_by_distance(data[:5], (52.2053, 0.1218))
    for item in ID:
        ls.append(round(item[1],1))
    
    #Check if distances match
    for n in range(0, len(ls)):
        assert ls[n] == distances[n]
def test_stations_within_radius():
    
    #Initialise variables
    data = build_station_list()
    c = [52.2053, 0.1218]
    r = 20
    
    #Get list of stations within radius
    data = stations_within_radius(data, c, r)
    
    #Check if list contains correct number of objects
    assert len(data) == 22
