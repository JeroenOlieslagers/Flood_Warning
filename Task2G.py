from floodsystem.stationdata import build_station_list
from floodsystem.analysis import assess_risk

def run():
    """Requirement for Task 2G"""
    #Initialise variables
    data = build_station_list()
    
    risk = assess_risk(data[:50])
    print(risk)

    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()