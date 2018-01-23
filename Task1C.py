from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirement for Task 1C"""
    
    #Set station list, centre and radius
    ID = []
    ls = []
    data = build_station_list()
    stations = data[:]
    c = [52.2053, 0.1218]
    r = 10
    
    #Get list of stations within radius
    ls = stations_within_radius(stations, c, r)
    
    #Add names of stations within radius to ID
    for station in ls:
        ID.append(station.name)
        
    #Sort alphabetically
    ID.sort()
    
    print(ID)
    
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()