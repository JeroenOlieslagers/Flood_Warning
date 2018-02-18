import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

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
