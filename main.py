import time
from lanis.traffic import TrafficEngine
import osmnx as ox
from weight import WeightEngine
from weather_api import get_weather
from dijkstra import dijkstra
from astar import astar
from road_loader import load_city
from geo_coder import nearest_node
from visualization import save_route_map
from traffic import TrafficEngine, get_traffic

weight=WeightEngine()
print("Loading road network...")

G = load_city("Kolkata, India")#finding distances between places in kolkata
source_place = input("Source: ")

destination_place = input("Destination: ")
source = nearest_node(G,source_place)
#finding latitude longitude
lat = G.nodes[source]["y"]
lon = G.nodes[source]["x"]

#finding the traffic factor from api(based on source)
flow =get_traffic(lat, lon)
traffic_factor = (TrafficEngine.traffic_multiplier(flow))

#finding the weather factor from api(based on source)
weather = get_weather(lat,lon)
multiplier = weight.weather_multiplier(weather)

#adjusting traffic and weather factor
for u, v, k, data in G.edges(keys=True, data=True):
    base = data["length"]
    new_weight = base * multiplier* traffic_factor
    data["dynamic_weight"] = new_weight

#input the destination
destination = nearest_node(G,destination_place)

print("Finding route...")

#finding route using djikstra
start = time.perf_counter()
path1, cost1 = dijkstra(G,source,destination)
end = time.perf_counter()
print("Dijkstra:",end - start)#the time taken
print("Distance (meters):", round(cost1))
print("Nodes in route:",len(path1))

#finding route using A*
start = time.perf_counter()
path2, cost2 = astar(G,source,destination)
end = time.perf_counter()
print("A*:",end - start)#the time taken
print("Distance (meters):", round(cost2))
print("Nodes in route:",len(path2))

#saving the routes
save_route_map(G,path1)
save_route_map(G, path2)
print("Route saved to route.html")
ox.save_graphml(G, "kolkata.graphml")