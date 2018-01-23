from floodsystem.geo import present_on_map
from floodsystem.stationdata import build_station_list

def run():
    """Requirement for extension"""
    #Build station list
    data = build_station_list()
    ls = data
    
    #Run
    present_on_map(ls)


if __name__ == "__main__":
    print("*** Extension: CUED Part IA Flood Warning System ***")
    run()

