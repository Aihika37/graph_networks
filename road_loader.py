import osmnx as ox

place="Kolkata, India"

#loading data of roads in Kolkata
def load_city(place):
    G = ox.graph_from_place(place,network_type="drive")
    return G

