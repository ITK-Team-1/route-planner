# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 13:08:14 2021

@author: Hamzah
"""

import pandas as pd
d={'Type':['Benzin','Diesel','Natural gas','Electric','Bus(long route)','Bus(short route)','Flight','Tram','Subway'],
   'Emission':[135,124,116,90,29,83,214,90,54]}
database_fuel=pd.DataFrame(data=d)
database_fuel=database_fuel.set_index('Type')
def co2_mapping(list_of_routes,mode="transit",driving_fuel="Diesel"):
    if mode== "driving":
        updated_routes=[]
        
        for i in range(len(list_of_routes)):
            temp=[]
            route=list_of_routes[i]
            for i in range(len(route)):
                if driving_fuel == "Diesel":
                    temp.append((database_fuel.loc['Diesel']['Emission'])*route.iloc[i]['Distance']/1000)
                if driving_fuel == "Benzin":
                    temp.append((database_fuel.loc['Benzin']['Emission'])*route.iloc[i]['Distance']/1000)
                if driving_fuel == "Natural gas":
                    temp.append((database_fuel.loc['Natural gas']['Emission'])*route.iloc[i]['Distance']/1000)
                if driving_fuel == "Electric":
                    temp.append((database_fuel.loc['Electric']['Emission'])*route.iloc[i]['Distance']/1000)
            route_update=route.copy()
            route_update['CO2 Emission']=temp
            updated_routes.append(route_update)
        
    if mode == "transit":
        updated_routes=[]
        
        for i in range(len(list_of_routes)):
            route=list_of_routes[i]
            temp=[]
            for i in range(len(route)):
                if route.iloc[i]['Name of Public Transport'] == "Train" or route.iloc[i]['Name of Public Transport'] == "Subway":
                    temp.append((route.iloc[i]['Distance'])*54/1000)
                elif(route.iloc[i]['Name of Public Transport'] == "Bus"):
                    temp.append((route.iloc[i]['Distance'])*83/1000)
                elif(route.iloc[i]['Name of Public Transport'] == "Tram"):
                    temp.append((route.iloc[i]['Distance'])*90/1000)
                else:
                    temp.append(0)
            route_update=route.copy()
            route_update['CO2 Emission']=temp
            updated_routes.append(route_update)
    else:
        updated_routes="Incorrect parameters"
    
    return updated_routes
