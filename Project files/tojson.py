def tojson(listofdf):
    dict={}
    
    for j in listofdf.keys():
        dict1={}
        dataframes_list=listofdf[j]
        for i in range(len(dataframes_list)):
            route="route"+str(i)
            dataframe=dataframes_list[i]
            dict1[route]=dataframe.to_json(orient="columns")
        dict[j]=dict1
        
       
    return dict   
