from floodsystem.geo import age_in_years
from floodsystem.stationdata import build_station_list

def run():
    """Requirement for extension"""
    
    ID = []
    
    #Build station list
    data = build_station_list()
    
    #Get age of stations
    ls = age_in_years(data)
    for station, age in ls:
        ID.append((station.name, age))

    print(ID[:10])

if __name__ == "__main__":
    print("*** Extension_age: CUED Part IA Flood Warning System ***")
    run()