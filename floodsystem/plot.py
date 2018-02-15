from floodsystem.datafetcher import fetch_measure_levels
import datetime
from dateutil import parser
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from math import sqrt

def plot_water_levels(stations, dt, limit, s):
    """ A function that displays a plot (using Matplotlib) of the water level
    data against time for a station, a maximum of 49 graphs are plotted
    separately, more than 49 will result in levels being displayed on one
    graph"""
    
    #Initialise variables
    ls = []
    i = 0
    j = 0
    
    #X-axis every day
    days = mdates.DayLocator()
    daysFmt = mdates.DateFormatter('%d-%m')
    
    #Get list of measuring_id's and rel water level
    #for station in stations:
        #ls.append((station.measure_id, station.typical_range[1], station.name))#station.relative_water_level())
    
    #Set orientation of graphs
    l = len(stations) - s
    sq = sqrt(l)
    if l > limit:
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
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=dt))
        if levels == []:
            pass
            
        #On different graphs if no. of stations less than limit
        elif l <= limit and l >2:
            #Set details for each subplot
            axarr[i, j].plot(dates, levels)
            axarr[i, j].xaxis.set_major_locator(days)
            axarr[i, j].xaxis.set_major_formatter(daysFmt)
            axarr[i, j].set_title(station.name)
            line1 = axarr[i, j].axhline(y=station.typical_range[0], c='g',
                 label='Typical low', linestyle='--')
            line2 = axarr[i, j].axhline(y=station.typical_range[1], c='r',
                 label='Typical high', linestyle='--')
            plt.legend(handles=[line2, line1])
            #Algorithm to move from top to bottom, left to right
            if i < row-1:
                i += 1
            elif i == row-1:
                j += 1
                i = 0
            plt.subplots_adjust(bottom=0.02, right=0.98, left=0.02, top=0.98)
            
         
        #Special case for one dimensional grid    
        elif l == 2:
            
            axarr[i].plot(dates, levels)
            axarr[i].xaxis.set_major_locator(days)
            axarr[i].xaxis.set_major_formatter(daysFmt)
            axarr[i].set_title(station.name)
            
            i += 1
            plt.subplots_adjust(bottom=0.02, right=0.98, left=0.02, top=0.98)
        #On same graph if no. of stations greater than limit and if only one 
        #graph            
        else:
            plt.plot(dates,levels, label=station.name)
            plt.subplots_adjust(bottom=0.02, right=0.9, left=0.02, top=0.98)
            plt.legend(bbox_to_anchor=(1.005, 1), loc=2, borderaxespad=0.)
            
    plt.show()