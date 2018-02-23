import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
from floodsystem.datafetcher import fetch_measure_levels

def polyfit(dates, levels, p):
    """A function that given the water level time history (dates, levels) for
    a station computes a least-squares fit of polynomial of degree p to water
    level data. The function returns a tuple of (1) the polynomial
    object and (2) any shift of the time (date) axis"""
    
    #Convert datetime object into integers
    x = matplotlib.dates.date2num(dates)
    y = levels
    
    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], y, p)
    
    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)
    
    return (poly, x[0])

def assess_risk(stations):
    """A function that given a list of MonitoringStations, calculates the risk
    of each station and places it in severe, high, moderate or low category"""
    ls = []
    
    for station in stations:
        #Get data
        dates, levels = fetch_measure_levels(station.measure_id,
                                                 dt=datetime.timedelta(days=5))        
        #Pass inconsistent data
        if levels == []:
            pass
        
        else:
            poly, d0 = polyfit(dates, levels, 1)
            
            if poly[1] < 0.01:
                status = 'Low'
            elif poly[1] < 0.05:
                status = 'Moderate'
            elif poly[1] < 0.1:
                status = 'High'
            else:
                status = 'Severe'
            ls.append(status)
    return ls
