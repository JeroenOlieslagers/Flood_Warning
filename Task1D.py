from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

stations = build_station_list()
rivers=rivers_with_station(stations)

def print_first_x_rivers_with_station(x=10):
    """Calls the <<rivers_with_station>> function and prints the
    total number of rivers and the first x rivers with a station"""
    #Prints the total number of rivers
    print("Total rivers with stations: {}\n".format(str(len(rivers))))
    #Converts the set into a sorted list
    rivers_in_order=sorted(rivers)
    #Creates empty list of first x rivers
    test_rivers=[]
    #Adds first x rivers to list
    for river in rivers_in_order[:x]:
        test_rivers.append(river)
    print("First {} rivers with stations: {}\n".format(x, test_rivers))

def print_stations_by_river(rivers):
    """Calls the <<stations_by_river>> function and prints a list of
    stations for each river in a list"""
    stationsbyriver=stations_by_river(stations)
    for river in rivers:
        #Calls list of stations on a river
        test_stations=stationsbyriver.get(river)
        #Sorts list of stations
        stations_in_order=sorted(test_stations)
        print("Stations on {}: {}\n".format(river, stations_in_order))
    
print_first_x_rivers_with_station()
print_stations_by_river(["River Aire", "River Cam", "Thames"])