from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import count_inconsistent_sets

def run():
    """Requirement for Task 2F"""
    
    #Initialise variables
    data = build_station_list()
    ls = []
    ID = []
    
    #Number of days in past taken data from
    dt = 9
    #Degree of polynomial line of best fit
    p = 3
    #How many stations
    number = 27
    #How many graphs per window
    limit = 50

    
    #Create list of measuring_id's sorted by water level
    for station in data:
        if station.typical_range_consistent() == True:
            ls.append((station, station.typical_range[1]))#station.relative_water_level()

    ls = sorted_by_key(ls, 1)
    
    for station in ls:
        ID.append(station[0])
        
    s = count_inconsistent_sets(ID[:number], dt)
    
    ID = ID[:number+s]
        
    plot_water_level_with_fit(ID, dt, limit, s, 3)
    
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()