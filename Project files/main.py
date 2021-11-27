# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:52:05 2021

@author: Hamzah
"""

from . import get_routes
from . import co2_mapping

def find_routes(origin="Nymphenburg Palace",destination="Marienplatz",departure_time="1638196470",driving_fuel="Diesel"):
    import requests
    import pandas as pd
    modes=["driving","transit","bicycling","walking"]
    dict={}
    dict1={}
    #temp=[]
    for i in modes:
        #temp.append(get_routes(origin, destination,i, departure_time))
        dict[i]=get_routes(origin,destination,i,departure_time)
    for i in modes:
        dict1[i]=co2_mapping(dict[i],i,driving_fuel)
        
    json=tojson(dict1)
    return json  #dict1
