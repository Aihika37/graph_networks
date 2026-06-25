import streamlit as st
import time
from road_loader import load_city
from geo_coder import nearest_node
from dijkstra import dijkstra
from astar import astar
from weather_api import get_weather
from traffic import get_traffic, TrafficEngine
from weight import WeightEngine
import folium
from streamlit.components.v1 import html

st.set_page_config(
    page_title="LANIS",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ LANIS")
st.subheader("Live Adaptive Navigation & Intelligent System")

@st.cache_resource
def get_graph():
    return load_city("Kolkata, India")

#setting up the app
G = get_graph()

source_place = st.text_input("Source","Howrah Railway Station, Kolkata, India")

destination_place = st.text_input("Destination","Victoria Memorial, Kolkata, India")

algorithm = st.selectbox("Algorithm",["Dijkstra", "A*"])

if st.button("Find Route"):

    with st.spinner("Computing route..."):

        source = nearest_node(G,source_place)
        destination = nearest_node(G,destination_place)
        lat = G.nodes[source]["y"]
        lon = G.nodes[source]["x"]
        weather = get_weather(lat,lon)
        weight = WeightEngine()
        weather_factor = weight.weather_multiplier(weather)
        try:

            flow = get_traffic(lat,lon)
            traffic_factor = (TrafficEngine.traffic_multiplier(flow))

        except Exception:

            traffic_factor = 1.0

        for u, v, k, data in G.edges(keys=True,data=True):
            base = data.get("length",1)
            data["dynamic_weight"] = (base * weather_factor* traffic_factor)
        start = time.perf_counter()
        if algorithm == "Dijkstra":
            path, cost = dijkstra(G,source,destination)
        else:
            path, cost = astar(G,source,destination)
        end = time.perf_counter()
        
    st.success("Route Computed")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Distance (m)",round(cost))
    with col2:
        st.metric("Runtime (s)",round(end - start, 5))
    with col3:
        st.metric("Nodes Traversed",len(path))
    st.write("Weather Factor:", round(weather_factor, 2))
    st.write("Traffic Factor:", round(traffic_factor, 2))
    
    coords = []
    for node in path:
        coords.append((G.nodes[node]["y"],G.nodes[node]["x"]))
    m = folium.Map(location=coords[0],zoom_start=13)
    folium.PolyLine(coords,weight=5).add_to(m)
    folium.Marker(coords[0],popup="Source").add_to(m)
    folium.Marker(coords[-1],popup="Destination").add_to(m)
    html(m._repr_html_(),height=600)