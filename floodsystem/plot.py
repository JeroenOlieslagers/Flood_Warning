from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np
from dateutil import parser
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib
from math import sqrt
from floodsystem.analysis import polyfit
from floodsystem.utils import down_right_config
from floodsystem.utils import loc_and_fmt_calc


def plot_2D(row, col, stations, dt, Loc, Fmt, fit=False, p=0):
    """ Function that plots data in two dimensional grid"""
    #Initialise variables
    i = 0
    j = 0
    fig, axarr = plt.subplots(row, col)
    
    for station in stations:      
            
        dates, levels = fetch_measure_levels(station.measure_id,
                                                 dt=datetime.timedelta(days=dt))
        #Pass inconsistent data
        if levels == []:
            pass
        else:
            #Set details for each subplot
            axarr[i, j].plot(dates, levels)
            axarr[i, j].xaxis.set_major_locator(Loc)
            axarr[i, j].xaxis.set_major_formatter(Fmt)
            axarr[i, j].set_title(station.name)
            line1 = axarr[i, j].axhline(y=station.typical_range[0], c='g',
                         label='Typical low', linestyle='--')
            line2 = axarr[i, j].axhline(y=station.typical_range[1], c='r',
                         label='Typical high', linestyle='--')
            if fit == True:
                #Convert datetime object into integers
                x = matplotlib.dates.date2num(dates)
                y = levels
    
                #Get line of best fit object and x-axis shift
                poly, d0 = polyfit(dates, levels, p)

                # Plot polynomial fit at 30 points along interval 
                x1 = np.linspace(d0, d0 - dt, 30)
                line3, = axarr[i, j].plot(x1 , poly(x1 - d0),
                             label='Line of best fit')
                plt.legend(handles = [line3, line2, line1])
            else:
                plt.legend(handles=[line2, line1])
                pass
            
            #Algorithm to move from top to bottom, left to right
            if i < row-1:
                i += 1
            elif i == row-1:
                j += 1
                i = 0
            plt.subplots_adjust(bottom=0.02, right=0.98, left=0.02, top=0.98)
            

def plot_1D(col, stations, dt, Loc, Fmt, fit=False, p=0):
    """Function that plots data in one dimensional grid"""
    #Initialise variables
    i = 0
    fig, axarr = plt.subplots(1, col)
    
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                                 dt=datetime.timedelta(days=dt))
        #Pass inconsistent data
        if levels == []:
            pass
        else:
            #Set details for each subplot
            axarr[i].plot(dates, levels)
            axarr[i].xaxis.set_major_locator(Loc)
            axarr[i].xaxis.set_major_formatter(Fmt)
            axarr[i].set_title(station.name)
            line1 = axarr[i].axhline(y=station.typical_range[0], c='g',
                         label='Typical low', linestyle='--')
            line2 = axarr[i].axhline(y=station.typical_range[1], c='r',
                         label='Typical high', linestyle='--')
            
            if fit == True:
                #Convert datetime object into integers
                x = matplotlib.dates.date2num(dates)
                y = levels
    
                #Get line of best fit object and x-axis shift
                poly, d0 = polyfit(dates, levels, p)

                # Plot polynomial fit at 30 points along interval 
                x1 = np.linspace(d0, d0 - dt, 30)
                line3, = axarr[i].plot(x1 , poly(x1 - d0),
                             label='Line of best fit')
                plt.legend(handles = [line3, line2, line1])
            else:
                plt.legend(handles=[line2, line1])
                pass
            
            i += 1
            plt.subplots_adjust(bottom=0.02, right=0.98, left=0.02, top=0.98)
            
def plot_0D(stations, dt, Loc, loc, Fmt, fmt, fit=False, p=0):
    """ Function that plots data in one graph"""
    #Initialise variables
    fig, axarr = plt.subplots(1, 1)
    
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id,
                                                 dt=datetime.timedelta(days=dt))
        #Pass inconsistent data
        if levels == []:
            pass
        else:
            plt.plot(dates,levels, label=station.name)
            axarr.xaxis.set_major_locator(Loc)
            axarr.xaxis.set_major_formatter(Fmt)
            if loc and fmt != 0:
                axarr.xaxis.set_minor_locator(loc)
                axarr.xaxis.set_minor_formatter(fmt)
            axarr.tick_params(which = 'major', labelsize = '14')
            #line1 = axarr.axhline(y=station.typical_range[0], c='g',
                        #label='Typical low', linestyle='--')
            #line2 = axarr.axhline(y=station.typical_range[1], c='r',
                        #label='Typical high', linestyle='--')
            if fit == True:
                #Convert datetime object into integers
                x = matplotlib.dates.date2num(dates)
                y = levels
    
                #Get line of best fit object and x-axis shift
                poly, d0 = polyfit(dates, levels, p)

                # Plot polynomial fit at 30 points along interval 
                x1 = np.linspace(d0, d0 - dt, 30)
                line3, = axarr.plot(x1 , poly(x1 - d0),
                             label='Best fit ' + station.name)
                plt.legend(handles = [line3])#, line2, line1])
            #else:
                #plt.legend(handles=[line2, line1])
                #pass
            plt.subplots_adjust(bottom=0.02, right=0.9, left=0.02, top=0.98)
            plt.legend(bbox_to_anchor=(1.005, 1), loc=2, borderaxespad=0.)


def plot_water_levels(stations, dt, limit, s):
    """ A function that displays a plot (using Matplotlib) of the water level
    data against time for a station, a maximum of 49 graphs are plotted
    separately, more than 49 will result in levels being displayed on one
    graph"""
    
    #Get axes data
    Loc, loc, Fmt, fmt = loc_and_fmt_calc(dt)

    #Set orientation of graphs
    l = len(stations) - s
    row, col = down_right_config(l, limit)
            
    #On different graphs if no. of stations less than limit
    if l <= limit and l >2:
        plot_2D(row, col, stations, dt, Loc, Fmt)
    
    #Special case for one dimensional grid    
    elif l == 2:
        plot_1D(col, stations, dt, Loc, Fmt)
        
    #On same graph if no. of stations greater than limit and if only one graph         
    else:
        plot_0D(stations, dt, Loc, loc, Fmt, fmt)
        
    
def plot_water_level_with_fit(stations, dt, limit, s, p):
    """A function that plots the water level data and the best-fit 
    polynomial for list of stations"""
    
    #Get axes data
    Loc, loc, Fmt, fmt = loc_and_fmt_calc(dt)
    
    #Set orientation of graphs
    l = len(stations) - s
    row, col = down_right_config(l, limit)
    
    #On different graphs if no. of stations less than limit
    if l <= limit and l >2:
        plot_2D(row, col, stations, dt, Loc, Fmt, fit=True, p=p)
    
    #Special case for one dimensional grid    
    elif l == 2:
        plot_1D(col, stations, dt, Loc, Fmt, fit=True, p=p)
        
    #On same graph if no. of stations greater than limit and if only one graph         
    else:
        plot_0D(stations, dt, Loc, loc, Fmt, fmt, fit=True, p=p)
        
        