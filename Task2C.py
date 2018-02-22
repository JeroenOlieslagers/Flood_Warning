from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_latest_water_level_data
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requrement for Task 2C"""
    
    stations = build_station_list()
    update_water_levels(stations)
    
    #Creates list of stations with 10 greatest relative water levels
    #sorted by relative water level
    shrl=stations_highest_rel_level(stations, 10)
    
    for station in shrl:
        print("{} {}".format(station[0], station[1]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
