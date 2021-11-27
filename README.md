# route-planner

![Logo](images/image2.PNG)
## Functions
### api_processing
Use this function to get list of routes for particular journey. Function has three parameters: 
1. Origin
2. Destination
3. Mode ('driving','transit','bicycling')
### Example
result= get_routes("Nymphenburg Palace","Marienplatz","transit")
*result* will be list of dataframes (routes) broken into coordinates with distance and time. 
One of the dataframe is shown below:
![image](images/image1.PNG)
