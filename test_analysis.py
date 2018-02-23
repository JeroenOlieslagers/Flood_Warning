"""Unit test for the analysis module"""

import pytest
import datetime
import numpy as np
from floodsystem.analysis import polyfit
import matplotlib
import matplotlib.pyplot as plt

def test_polyfit():
    
    #Create sets of data
    base_d = datetime.datetime.today()
    dates = [base_d - datetime.timedelta(seconds=x) for x in range(0, 100000)]
    levels = np.linspace(0, 10, 100000)

    poly, x = polyfit(dates, levels, 3)
    
    #Round both shifts to same number of decimal places
    r1 = round(matplotlib.dates.date2num(base_d), 6)
    r2 = round(x, 6)
    
    assert r1 == r2