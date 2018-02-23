"""Unit test for the station module"""

import pytest
from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    dateOpened = "some date"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town,
                          dateOpened)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    assert s.dateOpened == dateOpened

def test_inconsistent_monitoring_station_data():
    
    #Create a station with inconsistent typical range data
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = 'some inconsistent data'
    river = "River X"
    town = "My Town"
    dateOpened = "some date"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town,
                          dateOpened)
    
    assert s.typical_range_consistent() == False    