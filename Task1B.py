from floodsystem.geo import station_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def run():
    """Requirement for Task 1B"""
    
    # Build list of stations and initialise variables
    ID = []
    data = build_station_list()
    
    #Create list of all stations closest to Cambridge city centre
    ls = station_by_distance(data, (52.2053, 0.1218))
    
    #Select first and last 10 and print them
    for station in ls:
            ID.append((station[0].town, station[0].name, station[1]))
        
    print(ID[:10], ID[-10:])
    
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

