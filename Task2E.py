from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
import datetime
from dateutil import parser
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from math import sqrt

def run():
    """Requirement for Task 2E"""
    #Initialise variables
    data = build_station_list()
    ls = []
    dt = 5
    i = 0
    j = 0
    limit = 49
    
    #X-axis every day
    days = mdates.DayLocator()
    daysFmt = mdates.DateFormatter('%d-%m')
    
    #Get list of measuring_id's and rel water level
    for station in data[:49]:
        ls.append((station.measure_id, station.typical_range[1], station.name))#station.relative_water_level())
    
    #Create list of measuring_id's sorted by water level
    ls = sorted_by_key(ls, 1)
    
    #Set orientation of graphs
    sq = sqrt(len(ls))
    if len(ls) > limit:
        row = 1
        col = 1
    elif sq.is_integer():
        row = int(sq)
        col = int(sq)
    else:
        if sq - int(sq) < 0.5:
            row = int(sq)
            col = (int(sq)+1)
        else:
            row = (int(sq)+1)
            col = (int(sq)+1)
    
    #Loop over all stations
    fig, axarr = plt.subplots(row, col)
    for item in ls:
        a = fetch_measure_levels(item[0], dt=datetime.timedelta(days=dt))
        #On different graphs if no. of stations less than limit
        if len(ls) <= limit:
            #Set details for each subplot
            axarr[i, j].plot(a[0],a[1])
            axarr[i, j].xaxis.set_major_locator(days)
            axarr[i, j].xaxis.set_major_formatter(daysFmt)
            axarr[i, j].set_title(item[2])
            #Algorithm to move from top to bottom, left to right
            if i < row-1:
                i += 1
            elif i == row-1:
                j += 1
                i = 0
            plt.subplots_adjust(bottom=0.02, right=0.98, left=0.02, top=0.98)
            
        #On same graph if no. of stations greater than limit            
        else:
            plt.plot(a[0],a[1], label=item[2])
            plt.subplots_adjust(bottom=0.02, right=0.9, left=0.02, top=0.98)
            plt.legend(bbox_to_anchor=(1.005, 1), loc=2, borderaxespad=0.) 
    
    
    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
