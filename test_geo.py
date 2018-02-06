"""Unit test for the geo module"""

import pytest
import floodsystem.geo as geo
from floodsystem.stationdata import build_station_list

def test_rivers_with_station():
    #Initialise variables
    stations = build_station_list()
    rivers = geo.rivers_with_station(stations)
    test_river = "River Cam"
    if len(rivers) < 100:
        raise ValueError("Less than 100 rivers in set - data may be incomplete")
        #Checks of test_river is present in list of rivers
    if test_river not in rivers:
        raise ValueError("{} not present - data may be incomplete".format(test_river))
    
test_rivers_with_station()  

def test_stations_by_river():
    #Initialise variables
    stations = build_station_list()
    stationsbyriver=geo.stations_by_river(stations)
    test_river = "River Cam"
    test_station = "Cam"
    #Checks if test_station is present on test_river
    if test_station not in stationsbyriver[test_river]:
        raise ValueError("Station \"{}\" not present on {} - data may be incomplete".format(test_station, test_river))
    
test_stations_by_river()  

def test_rivers_by_station_number():
    #Initialise variables
    stations = build_station_list()
    N=9
    first_N_rivers=geo.rivers_by_station_number(stations, N)
    #River with expected greatest number of stations
    test_river = "Thames"
    #Checks that at least as many stations that are called for are returned
    if len(first_N_rivers) < N:
        raise ValueError("First {} rivers called for but only {} returned".format(N, len(first_N_rivers)))
    #Checks if test river has the greatest number of stations
    if first_N_rivers[0][0] != test_river:
        raise ValueError("{} does not have the greatest number of staions - data may be incomplete".format(test_river))

test_rivers_by_station_number()

#You are now entering the Jeroen Sector - proceed with caution

def test_haversine():
    #Initialise list of lat and long coordinates of test variables
    coord = [(10, 10), (5, 12), (52.342,63.435), (63.234, 1.234)]
    
    #Initialise list of corresponding distances from (0,0) according to 
    # https://www.movable-type.co.uk/scripts/latlong.html
    ls = [1569, 1444, 8244, 7032]
    
    for n in range(0, len(ls)):
        assert round(geo.haversine(coord[n], (0,0))) == ls[n]

def test_age_in_years():
    #Initialise variables
    ls = []
    age1 = [21, 21, 24, 26, 42]
    data = build_station_list()

    #Get age of dates
    ID = geo.age_in_years(data[:5])
    for station, age in ID:
        ls.append(age)
    
    #Check if ages match
    for n in range(0, len(ls)):
        assert ls[n] == age1[n]

def test_station_by_distance():
    
    #Initialise variables
    data = build_station_list()
    distances = [20.1, 72.8, 132.5, 161.7, 243.4]
    ls = []
    
    #Create list of all stations closest to Cambridge city centre
    ID = geo.station_by_distance(data[:5], (52.2053, 0.1218))
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
    data = geo.stations_within_radius(data, c, r)
    
    #Check if list contains correct number of objects
    assert len(data) == 22
    
