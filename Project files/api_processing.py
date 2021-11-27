# -*- coding: utf-8 -*-
"""

Created on Fri Nov 26 22:43:00 2021

@author: Hamzah
"""
#modes=transit,driving,bicycling
import requests
import pandas as pd
origin="Nymphenburg Palace"
destination="Marienplatz"
mode="driving"
mode="transit"


def get_routes(origin,destination,mode="transit"):
    url="https://maps.googleapis.com/maps/api/directions/json?origin="+origin+"&destination="+destination+"&mode="+mode+"&alternatives=true&key=AIzaSyA21A1YTf1TOEJPnb67dFJeQaLm1vdeEAc"
    
    if(mode=="transit"):
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        result=response.json()
        routes_dict=result['routes']
        list_of_routes=[]
        for i in range(len(routes_dict)):
            route1=routes_dict[i]
            distance=[]
            duration=[]
            start_lat=[]
            start_lon=[]
            end_lat=[]
            end_lon=[]
            mode=[]
            transport_name=[]
            transport_operator=[]
            for i in range(len(route1['legs'][0]['steps'])):
                #root=route1['legs'][0]['steps']
                
                if route1['legs'][0]['steps'][i]['travel_mode'] != "TRANSIT":
                    way=route1['legs'][0]['steps'][i]
                    #print(way.keys())
                    
                    #for j in range(len(way)):
                    distance.append(way['distance']['text'])
                    duration.append(way['duration']['text'])
                    start_lat.append(way['start_location']['lat'])
                    start_lon.append(way['start_location']['lng'])
                    end_lat.append(way['end_location']['lat'])
                    end_lon.append(way['end_location']['lng'])
                    mode.append(way['travel_mode'])
                    transport_operator.append("NA")
                    transport_name.append("NA")
                        
                else:
                    way=route1['legs'][0]['steps'][i]
                    #for j in range(len(way)):
                    distance.append(way['distance']['text'])
                    duration.append(way['duration']['text'])
                    start_lat.append(way['start_location']['lat'])
                    start_lon.append(way['start_location']['lng'])
                    end_lat.append(way['end_location']['lat'])
                    end_lon.append(way['end_location']['lng'])
                    mode.append(way['travel_mode'])
                    if route1['legs'][0]['steps'][i]['travel_mode'] == "TRANSIT":
                        transport_operator.append(way['transit_details']['line']['agencies'][0]['name'])
                        transport_name.append(way['html_instructions'].split()[0])
                            
                    else: 
                        transport_operator.append("NA")
                        transport_name.append("NA")
            detail = pd.DataFrame(list(zip(start_lat,start_lon,end_lat,end_lon,distance,duration,mode,transport_name,transport_operator)),
                      columns=['Start_lat','Start_lon','End_lat','end_lon','Ditance','Duration','Travelling mode','Name of Public Transport','Operator'])

            
            list_of_routes.append(detail)
            
    elif(mode=="driving"):
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        result=response.json()
        routes_dict=result['routes']
        list_of_routes=[]
        for i in range(len(routes_dict)):
            route1=routes_dict[i]
            distance=[]
            duration=[]
            start_lat=[]
            start_lon=[]
            end_lat=[]
            end_lon=[]
            mode=[]
            for i in range(len(route1['legs'][0]['steps'])):
                root=route1['legs'][0]['steps']
                
                if route1['legs'][0]['steps'][i]['travel_mode'] != "TRANSIT":
                    way=route1['legs'][0]['steps'][i]
                    #print(way.keys())
                    
                    #for j in range(len(way)):
                    distance.append(way['distance']['text'])
                    duration.append(way['duration']['text'])
                    start_lat.append(way['start_location']['lat'])
                    start_lon.append(way['start_location']['lng'])
                    end_lat.append(way['end_location']['lat'])
                    end_lon.append(way['end_location']['lng'])
                    mode.append(way['travel_mode'])
                        
                else:
                    way=route1['legs'][0]['steps'][i]
                    #for j in range(len(way)):
                    distance.append(way['distance']['text'])
                    duration.append(way['duration']['text'])
                    start_lat.append(way['start_location']['lat'])
                    start_lon.append(way['start_location']['lng'])
                    end_lat.append(way['end_location']['lat'])
                    end_lon.append(way['end_location']['lng'])
                    mode.append(way['travel_mode'])
            detail = pd.DataFrame(list(zip(start_lat,start_lon,end_lat,end_lon,distance,duration,mode)),
                                  columns=['Start_lat','Start_lon','End_lat','end_lon','Ditance','Duration','Travelling mode'])

            list_of_routes.append(detail)
    elif(mode=="bicycling"):
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        result=response.json()
        routes_dict=result['routes']
        list_of_routes=[]
        for i in range(len(routes_dict)):
            route1=routes_dict[i]
            distance=[]
            duration=[]
            start_lat=[]
            start_lon=[]
            end_lat=[]
            end_lon=[]
            mode=[]
            for i in range(len(route1['legs'][0]['steps'])):
                root=route1['legs'][0]['steps']
                
                if route1['legs'][0]['steps'][i]['travel_mode'] != "TRANSIT":
                    way=route1['legs'][0]['steps'][i]
                    #print(way.keys())
                    
                    #for j in range(len(way)):
                    distance.append(way['distance']['text'])
                    duration.append(way['duration']['text'])
                    start_lat.append(way['start_location']['lat'])
                    start_lon.append(way['start_location']['lng'])
                    end_lat.append(way['end_location']['lat'])
                    end_lon.append(way['end_location']['lng'])
                    mode.append(way['travel_mode'])
                        
                else:
                    way=route1['legs'][0]['steps'][i]
                    #for j in range(len(way)):
                    distance.append(way['distance']['text'])
                    duration.append(way['duration']['text'])
                    start_lat.append(way['start_location']['lat'])
                    start_lon.append(way['start_location']['lng'])
                    end_lat.append(way['end_location']['lat'])
                    end_lon.append(way['end_location']['lng'])
                    mode.append(way['travel_mode'])
            detail = pd.DataFrame(list(zip(start_lat,start_lon,end_lat,end_lon,distance,duration,mode)),
                                  columns=['Start_lat','Start_lon','End_lat','end_lon','Ditance','Duration','Travelling mode'])

            list_of_routes.append(detail)
    else:
        list_of_routes="Not Valid mode"
    return list_of_routes
            
            
origin='Berlin'
destination='Munich'
#m=get_routes(origin,destination,mode="transit")

