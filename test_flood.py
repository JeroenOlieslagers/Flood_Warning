"""Unit test for the flood module"""

import pytest
import floodsystem.flood as flood
from floodsystem.stationdata import build_station_list, update_water_levels

def test_stations_level_over_threshold():
    #Initialise variables
    stations = build_station_list()
    update_water_levels(stations)
    #Unrealistic tolerance value
    tol=10
    #Checks no stations have an unrealistic relative water level
    slot=flood.stations_level_over_threshold(stations, tol)
    if slot!=[]:
        raise ValueError("Stations present with relative water level greater than {}".format(tol))
    #Realistic tolerance value
    tol2=0.5
    #Checks stations are present with a realistic relative water level
    slot2=flood.stations_level_over_threshold(stations, tol2)
    if slot2==[]:
        raise ValueError("No stations present with relative water level greater than {}".format(tol2))
    
test_stations_level_over_threshold()

def test_stations_highest_rel_level():
    #Initialise variables
    stations = build_station_list()
    update_water_levels(stations)
    N=10
    #Calls for N stations with highest relative water level
    shrl=flood.stations_highest_rel_level(stations, N)
    #Checks N stations are returned
    if len(shrl)!=N:
        raise ValueError("{} stations called for; {} returned".format(N, len(shrl)))

test_stations_highest_rel_level()