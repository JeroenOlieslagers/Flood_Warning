from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.datafetcher import count_inconsistent_sets

def run():
    """Requirement for Task 2E"""
    #Initialise variables
    data = build_station_list()
    ls = []
    ID = []
    dt = 5
    limit = 600
    number = 9
    
    #Create list of measuring_id's sorted by water level
    for station in data:
        if station.typical_range_consistent() == True:
            ls.append((station, station.typical_range[1]))#station.relative_water_level()

    ls = sorted_by_key(ls, 1)
    
    for station in ls:
        ID.append(station[0])
        
    s = count_inconsistent_sets(ID[:number], dt)
    
    ID = ID[:number+s]

    plot_water_levels(ID, dt, limit, s)
      
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
