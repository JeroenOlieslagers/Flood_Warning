from floodsystem.geo import present_on_map
from floodsystem.stationdata import build_station_list

def run():
    """Requirement for extension"""
    #Build station list
    data = build_station_list()
    
    #Run
    present_on_map(data)


if __name__ == "__main__":
    print("*** Extension_map: CUED Part IA Flood Warning System ***")
    run()

