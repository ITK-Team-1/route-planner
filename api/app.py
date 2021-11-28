from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import requests
import pandas as pd
import json
d={'Type':['Benzin','Diesel','Natural gas','Electric','Bus(long route)','Bus(short route)','Flight','Tram','Subway'],
   'Emission':[135,124,116,90,29,83,214,90,54]}
database_fuel=pd.DataFrame(data=d)
database_fuel=database_fuel.set_index('Type')
app = Flask(__name__)
api = Api(app)

class Route(Resource):

    def apple(self):
        return "c"
    def get_routes(self,origin, destination, mode="transit", departure_time="1638023670"):
        url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination + "&mode=" + mode + "&departure_time=" + departure_time + "&alternatives=true&key=AIzaSyA21A1YTf1TOEJPnb67dFJeQaLm1vdeEAc"
        if (mode == "transit"):
            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            result = response.json()
            routes_dict = result['routes']
            list_of_routes = []
            for i in range(len(routes_dict)):
                route1 = routes_dict[i]
                distance = []
                duration = []
                start_lat = []
                start_lon = []
                end_lat = []
                end_lon = []
                mode = []
                transport_name = []
                transport_operator = []
                for i in range(len(route1['legs'][0]['steps'])):
                    # root=route1['legs'][0]['steps']
                    if route1['legs'][0]['steps'][i]['travel_mode'] != "TRANSIT":
                        way = route1['legs'][0]['steps'][i]
                        # print(way.keys())
                        # for j in range(len(way)):
                        distance.append(way['distance']['value'])
                        duration.append(way['duration']['value'])
                        start_lat.append(way['start_location']['lat'])
                        start_lon.append(way['start_location']['lng'])
                        end_lat.append(way['end_location']['lat'])
                        end_lon.append(way['end_location']['lng'])
                        mode.append(way['travel_mode'])
                        transport_operator.append("NA")
                        transport_name.append("NA")

                    else:
                        way = route1['legs'][0]['steps'][i]
                        # for j in range(len(way)):
                        distance.append(way['distance']['value'])
                        duration.append(way['duration']['value'])
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
                detail = pd.DataFrame(list(
                    zip(start_lat, start_lon, end_lat, end_lon, distance, duration, mode, transport_name,
                        transport_operator)),
                                      columns=['Start_lat', 'Start_lon', 'End_lat', 'end_lon', 'Distance', 'Duration',
                                               'Travelling mode', 'Name of Public Transport', 'Operator'])

                list_of_routes.append(detail)

        elif (mode == "driving"):
            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            result = response.json()
            routes_dict = result['routes']
            list_of_routes = []
            for i in range(len(routes_dict)):
                route1 = routes_dict[i]
                distance = []
                duration = []
                start_lat = []
                start_lon = []
                end_lat = []
                end_lon = []
                mode = []
                for i in range(len(route1['legs'][0]['steps'])):
                    root = route1['legs'][0]['steps']

                    if route1['legs'][0]['steps'][i]['travel_mode'] != "TRANSIT":
                        way = route1['legs'][0]['steps'][i]
                        # print(way.keys())
                        # for j in range(len(way)):
                        distance.append(way['distance']['value'])
                        duration.append(way['duration']['value'])
                        start_lat.append(way['start_location']['lat'])
                        start_lon.append(way['start_location']['lng'])
                        end_lat.append(way['end_location']['lat'])
                        end_lon.append(way['end_location']['lng'])
                        mode.append(way['travel_mode'])

                    else:
                        way = route1['legs'][0]['steps'][i]
                        # for j in range(len(way)):
                        distance.append(way['distance']['text'])
                        duration.append(way['duration']['text'])
                        start_lat.append(way['start_location']['lat'])
                        start_lon.append(way['start_location']['lng'])
                        end_lat.append(way['end_location']['lat'])
                        end_lon.append(way['end_location']['lng'])
                        mode.append(way['travel_mode'])
                detail = pd.DataFrame(list(zip(start_lat, start_lon, end_lat, end_lon, distance, duration, mode)),
                                      columns=['Start_lat', 'Start_lon', 'End_lat', 'end_lon', 'Distance', 'Duration',
                                               'Travelling mode'])

                list_of_routes.append(detail)
        elif (mode == "bicycling"):
            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            result = response.json()
            routes_dict = result['routes']
            list_of_routes = []
            for i in range(len(routes_dict)):
                route1 = routes_dict[i]
                distance = []
                duration = []
                start_lat = []
                start_lon = []
                end_lat = []
                end_lon = []
                mode = []
                for i in range(len(route1['legs'][0]['steps'])):
                    root = route1['legs'][0]['steps']

                    if route1['legs'][0]['steps'][i]['travel_mode'] != "TRANSIT":
                        way = route1['legs'][0]['steps'][i]
                        # print(way.keys())
                        # for j in range(len(way)):
                        distance.append(way['distance']['value'])
                        duration.append(way['duration']['value'])
                        start_lat.append(way['start_location']['lat'])
                        start_lon.append(way['start_location']['lng'])
                        end_lat.append(way['end_location']['lat'])
                        end_lon.append(way['end_location']['lng'])
                        mode.append(way['travel_mode'])

                    else:
                        way = route1['legs'][0]['steps'][i]
                        # for j in range(len(way)):
                        distance.append(way['distance']['value'])
                        duration.append(way['duration']['value'])
                        start_lat.append(way['start_location']['lat'])
                        start_lon.append(way['start_location']['lng'])
                        end_lat.append(way['end_location']['lat'])
                        end_lon.append(way['end_location']['lng'])
                        mode.append(way['travel_mode'])
                detail = pd.DataFrame(list(zip(start_lat, start_lon, end_lat, end_lon, distance, duration, mode)),
                                      columns=['Start_lat', 'Start_lon', 'End_lat', 'end_lon', 'Distance', 'Duration',
                                               'Travelling mode'])

                list_of_routes.append(detail)
        elif (mode == "walking"):
            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            result = response.json()
            routes_dict = result['routes']
            list_of_routes = []
            for i in range(len(routes_dict)):
                route1 = routes_dict[i]
                distance = []
                duration = []
                start_lat = []
                start_lon = []
                end_lat = []
                end_lon = []
                mode = []
                for i in range(len(route1['legs'][0]['steps'])):
                    root = route1['legs'][0]['steps']

                    if route1['legs'][0]['steps'][i]['travel_mode'] != "TRANSIT":
                        way = route1['legs'][0]['steps'][i]
                        # print(way.keys())
                        # for j in range(len(way)):
                        distance.append(way['distance']['value'])
                        duration.append(way['duration']['value'])
                        start_lat.append(way['start_location']['lat'])
                        start_lon.append(way['start_location']['lng'])
                        end_lat.append(way['end_location']['lat'])
                        end_lon.append(way['end_location']['lng'])
                        mode.append(way['travel_mode'])

                    else:
                        way = route1['legs'][0]['steps'][i]
                        # for j in range(len(way)):
                        distance.append(way['distance']['value'])
                        duration.append(way['duration']['value'])
                        start_lat.append(way['start_location']['lat'])
                        start_lon.append(way['start_location']['lng'])
                        end_lat.append(way['end_location']['lat'])
                        end_lon.append(way['end_location']['lng'])
                        mode.append(way['travel_mode'])
                detail = pd.DataFrame(list(zip(start_lat, start_lon, end_lat, end_lon, distance, duration, mode)),
                                      columns=['Start_lat', 'Start_lon', 'End_lat', 'end_lon', 'Distance', 'Duration',
                                               'Travelling mode'])

                list_of_routes.append(detail)
        else:
            list_of_routes = "Not Valid mode"
        return list_of_routes

    def co2_mapping(self,list_of_routes, mode="driving", driving_fuel="Diesel"):

        if mode == "driving":
            updated_routes = []
            print(driving_fuel)

            for i in range(len(list_of_routes)):
                temp = []
                route = list_of_routes[i]
                for i in range(len(route)):
                    if driving_fuel == "diesel":
                        temp.append((database_fuel.loc['Diesel']['Emission']) * route.iloc[i]['Distance'] / 1000)
                    if driving_fuel == "benzin":
                        temp.append((database_fuel.loc['Benzin']['Emission']) * route.iloc[i]['Distance'] / 1000)
                    if driving_fuel == "natural gas":
                        temp.append((database_fuel.loc['Natural gas']['Emission']) * route.iloc[i]['Distance'] / 1000)
                    if driving_fuel == "electric":
                        temp.append((database_fuel.loc['Electric']['Emission']) * route.iloc[i]['Distance'] / 1000)
                route_update = route.copy()
                route_update['CO2 Emission'] = temp
                route_update['Total CO2'] = route_update['CO2 Emission'].sum()
                route_update['Total duration'] = route_update['Duration'].sum()
                route_update['Total distance'] = route_update['Distance'].sum()
                updated_routes.append(route_update)

        elif mode == "transit":
            updated_routes = []

            for i in range(len(list_of_routes)):
                route = list_of_routes[i]
                temp = []
                for i in range(len(route)):
                    if route.iloc[i]['Name of Public Transport'] == "Train" or route.iloc[i][
                        'Name of Public Transport'] == "Subway":
                        temp.append((route.iloc[i]['Distance']) * 54 / 1000)
                    elif (route.iloc[i]['Name of Public Transport'] == "Bus"):
                        temp.append((route.iloc[i]['Distance']) * 83 / 1000)
                    elif (route.iloc[i]['Name of Public Transport'] == "Tram"):
                        temp.append((route.iloc[i]['Distance']) * 54 / 1000)
                    else:
                        temp.append(0)
                route_update = route.copy()
                route_update['CO2 Emission'] = temp
                route_update['Total CO2'] = route_update['CO2 Emission'].sum()
                route_update['Total duration'] = route_update['Duration'].sum()
                route_update['Total distance'] = route_update['Distance'].sum()
                updated_routes.append(route_update)
        elif mode == "bicycling":
            updated_routes = []

            for i in range(len(list_of_routes)):
                route = list_of_routes[i]
                temp = []
                for i in range(len(route)):
                    temp.append(0)
                route_update = route.copy()
                route_update['CO2 Emission'] = temp
                route_update['Total CO2'] = route_update['CO2 Emission'].sum()
                route_update['Total duration'] = route_update['Duration'].sum()
                route_update['Total distance'] = route_update['Distance'].sum()
                updated_routes.append(route_update)
        elif mode == "walking":
            updated_routes = []

            for i in range(len(list_of_routes)):
                route = list_of_routes[i]
                temp = []
                for i in range(len(route)):
                    temp.append(0)
                route_update = route.copy()
                route_update['CO2 Emission'] = temp
                route_update['Total CO2'] = route_update['CO2 Emission'].sum()
                route_update['Total duration'] = route_update['Duration'].sum()
                route_update['Total distance'] = route_update['Distance'].sum()

                updated_routes.append(route_update)
        else:
            updated_routes = "Incorrect parameters"
            updated_routes = pd.DataFrame()

        return updated_routes

    def tojson(self,listofdf):
        dict = {}

        for j in listofdf.keys():
            dict1 = {}
            dataframes_list = listofdf[j]
            array = []
            for i in range(len(dataframes_list)):
                # route="route"+str(i)
                dataframe = dataframes_list[i]
                # dict1[route]=dataframe.to_dict()
                array.append(dataframe.to_dict())
            dict[j] = array
        return dict

    def find_routes(self,origin="Nymphenburg Palace", destination="Marienplatz", departure_time="1638196470",
                    driving_fuel="Diesel"):
        import requests
        import pandas as pd
        modes = ["driving", "transit", "bicycling", "walking"]
        dict = {}
        dict1 = {}
        # temp=[]
        for i in modes:
            # temp.append(get_routes(origin, destination,i, departure_time))
            dict[i] = self.get_routes(origin, destination, i, departure_time)
        for i in modes:
            dict1[i] = self.co2_mapping(dict[i], i, driving_fuel)

        json = self.tojson(dict1)
        
        # json = json.dumps(dict1)
        return json  # dict1
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('origin', type=str)
        parser.add_argument('destination', type=str)
        parser.add_argument('departure_time', type=str)
        parser.add_argument('fuel_type', type=str)
        T=parser.parse_args()
        print(T)
        json = self.find_routes(T['origin'], T['destination'], T['departure_time'], T['fuel_type'])
        resp = jsonify(json)
        resp.headers.add("Access-Control-Allow-Origin", "*")
        #t1 = json.dumps(t1)
        return resp

api.add_resource(Route, '/route', endpoint='bar')

if __name__ == '__main__':

    app.run(debug=True)
