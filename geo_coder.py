import osmnx as ox

#finding latitude and longitude
def get_coordinates(place):
    lat, lon = ox.geocode(place)
    return lat, lon

#finding nearest nodes with the given latitude longitude
def nearest_node(graph, place):
    lat, lon = get_coordinates(place)
    node = ox.distance.nearest_nodes(graph,X=lon,Y=lat)
    return node