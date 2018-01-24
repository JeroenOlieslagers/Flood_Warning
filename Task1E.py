from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requrement for Task 1D"""

    stations = build_station_list()
    
    first_N_rivers=rivers_by_station_number(stations, 9)
    print(first_N_rivers)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

