from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_latest_water_level_data
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requrement for Task 2B"""
    
    stations = build_station_list()
    update_water_levels(stations)
    
    #Creates list of stations with relative water level greater than 0.8
    #sorted by relative water level
    slot=stations_level_over_threshold(stations, 0.8)
    
    for station in slot:
        print("{} {}".format(station[0], station[1]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

