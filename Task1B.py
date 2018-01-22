from floodsystem.geo import station_by_distance


def run():
    """Requirement for Task 1B"""
    
    # Build list of stations
    stations = []
    build = build_station_list()
    for station in build:
        stations.append(station.name)
        
    
    #Create list of all stations closest to Cambridge city centre
    ls = station_by_distance(stations, (52.2053, 0.1218))
    
    #Select first and last 10 and print them
    print(ls[:10], ls[-10:])
    
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

