from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirement for Task 1F"""
    
    #Initialise variables
    data = build_station_list()
    
    #Get list of stations with inconsistent typical range data
    ls = inconsistent_typical_range_stations(data)
    
    #Add names of stations with inconsistent typical range data
    for station in ls:
        ID.append(station.name)
        
    #Sort alphabetically
    ID.sort()
    
    print(ID)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
