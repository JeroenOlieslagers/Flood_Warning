from math import sqrt
import numpy as np
import matplotlib.dates as mdates

def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

def down_right_config(l, limit):
    """Takes in length of list and returns number of rows and columns
    required for graph to form down-right configuration """
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
    return row, col

def loc_and_fmt_calc(dt):
    """ Function that sets axes boundaries"""
    if dt < 9:
        #Major X-axis every day
        #Minor X-axis dependant on dt
        ls = np.linspace(0, 24, 24/dt, dtype=int)
        Loc = mdates.DayLocator()
        loc = mdates.HourLocator(byhour = ls[1:-1])
        Fmt = mdates.DateFormatter('%d-%b')
        fmt = mdates.DateFormatter('%H:%M')
        
    else:
        Loc = mdates.DayLocator()
        Fmt = mdates.DateFormatter('%d-%b')
        loc = 0
        fmt = 0
        
    return Loc, loc, Fmt, fmt