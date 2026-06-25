import heapq
from math import radians, sin, cos, sqrt, atan2

#this method have some pre-built estimates which help in determining nodes easily
def haversine(lat1, lon1, lat2, lon2):
    #calculate the distance between two places on earth using latitude,longitude
    R = 6371000
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (sin(dlat / 2) ** 2+ cos(radians(lat1))* cos(radians(lat2))* sin(dlon / 2) ** 2)
    c = 2 * atan2(sqrt(a),sqrt(1 - a))
    return R * c

def heuristic(G, u, goal):
    lat1 = G.nodes[u]["y"]
    lon1 = G.nodes[u]["x"]

    #goal's latitude and longitude
    lat2 = G.nodes[goal]["y"]
    lon2 = G.nodes[goal]["x"]
    
    #from every node we calculate distance to destination
    return haversine(lat1,lon1,lat2,lon2)

def astar(G, source, destination):
    pq = []
    heapq.heappush(pq,(0, source))#pushing source
    g_score = {node: float("inf")for node in G.nodes}#distance from source
    parent = {}
    g_score[source] = 0
    while pq:
        _, node = heapq.heappop(pq)
        if node == destination:
            break
        for nbr in G.neighbors(node):
            edge_data = G[node][nbr]
            edge_key = list(edge_data.keys())[0]
            weight = edge_data[edge_key].get("dynamic_weight",
                     edge_data[edge_key].get("length",1))#getting dynamic weight if possible
            tentative = (g_score[node]+ weight)
            if tentative < g_score[nbr]:#if improvement possible
                g_score[nbr] = tentative
                parent[nbr] = node
                f_score = (tentative + heuristic(G,nbr,destination))#we take minimum based on distances to destination
                heapq.heappush( pq,(f_score,nbr))

    #reconstructing path
    path = []
    cur = destination
    while cur != source:
        path.append(cur)
        cur = parent[cur]
    path.append(source)
    path.reverse()

    return (path,g_score[destination])