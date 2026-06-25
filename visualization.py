import folium

#saving the route
def save_route_map(G,path,filename="route.html"):
    start = path[0]
    center = [G.nodes[start]["y"],G.nodes[start]["x"]]
    m = folium.Map(location=center,zoom_start=13)
    coords = []
    for node in path:
        coords.append((G.nodes[node]["y"],G.nodes[node]["x"]))
    folium.PolyLine(coords,weight=5).add_to(m)
    folium.Marker(coords[0],popup="Source").add_to(m)
    folium.Marker(coords[-1],popup="Destination").add_to(m)
    m.save(filename)