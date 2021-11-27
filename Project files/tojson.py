def tojson(listofdf):
    dict={}
    for i in range(len(listofdf)):
        route="Route"+str(i)
        dict[route]=listofdf[i].to_json(orient="columns")
       
    return dict
