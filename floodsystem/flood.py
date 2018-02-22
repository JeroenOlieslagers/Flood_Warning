from floodsystem.stationdata import build_station_list

stations = build_station_list()
    
def stations_level_over_threshold(stations, tol):
    
    relativewaterlevels=[]
    
    for station in stations:
        #Checks if water level range is consistent
        if station.typical_range_consistent()==True:
            #Creates a tuple containing station name and relative water level
            rwl=(station.name, station.relative_water_level())
            #Checks if relative water level has a value
            if rwl[1]!=None:
                #Checks if relative water level is greater than the tolerance
                if rwl[1]>tol:
                    #Adds station and relative water level to list
                    relativewaterlevels.append(rwl)
    #Sorts tuples by relative water level
    relativewaterlevels.sort(key=lambda tup: tup[1], reverse=True)
    
    return relativewaterlevels