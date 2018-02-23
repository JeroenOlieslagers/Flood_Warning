from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.datafetcher import count_inconsistent_sets

def run():
    """Requirement for Task 2E"""
    #Initialise variables
    data = build_station_list()
    update_water_levels(data)
    ls = []
    ID = []
    
    #Number of days in past taken data from
    dt = 7
    #How many graphs per window
    limit = 4
    #How many stations
    number = 6
    
    #Create list of measuring_id's sorted by water level
    for station in data:
        if station.typical_range_consistent() == True and station.relative_water_level() != None:
            ls.append((station, station.relative_water_level()))

    ls = sorted_by_key(ls, 1)
    
    for station in ls:
        ID.append(station[0])
        
    s = count_inconsistent_sets(ID[:number], dt)
    
    ID = ID[:number+s]

    plot_water_levels(ID, dt, limit, s)
      
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
