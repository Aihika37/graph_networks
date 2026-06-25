# 🗺️ LANIS – Live Adaptive Navigation & Intelligent System

LANIS is an intelligent route planning system that computes the optimal path between two locations by considering **real-time traffic conditions** and **current weather information**. It provides an interactive map interface and supports multiple shortest-path algorithms for performance comparison.

---

##  Features

-  Real-time route planning
-  Weather-aware route cost adjustment
-  Traffic-aware edge weighting
-  Supports both **Dijkstra** and **A*** algorithms
-  Interactive route visualization using Folium
-  Address-to-coordinate geocoding
-  Displays execution time, route distance, and nodes traversed
-  Built on real OpenStreetMap road networks

---

##  Tech Stack

- Python
- Streamlit
- NetworkX
- OSMnx
- Folium
- OpenStreetMap
- OpenWeather API
- Traffic API (TomTom/api)

---

##  Project Structure

```
LANIS/
│
├── app.py                  # Streamlit application
├── road_loader.py          # Downloads and loads road network
├── geo_coder.py            # Converts addresses to graph nodes
├── dijkstra.py             # Dijkstra shortest path implementation
├── astar.py                # A* shortest path implementation
├── traffic.py              # Traffic API integration
├── weather_api.py          # Weather API integration
├── weight.py               # Dynamic edge weight calculation

```

---

##  How It Works

1. Load the city road network from OpenStreetMap.
2. Convert source and destination addresses into the nearest graph nodes.
3. Fetch current weather data.
4. Fetch live traffic information.
5. Update every road edge with a dynamic weight:

```
Dynamic Weight = Road Length × Weather Factor × Traffic Factor
```

6. Compute the optimal path using the selected algorithm.
7. Display the route on an interactive map.

---

##  Dynamic Weight Example

```
Road Length    = 100 m
Weather Factor = 1.20
Traffic Factor = 1.40

Dynamic Weight = 100 × 1.20 × 1.40
               = 168
```

---

##  Algorithms

### Dijkstra's Algorithm

- Finds the shortest path in weighted graphs.
- Guarantees the optimal solution.
- Uses cumulative path cost.

### A* Search Algorithm

- Uses a heuristic to guide the search.
- Visits fewer nodes than Dijkstra in most cases.
- Produces the optimal path with an admissible heuristic(distance between places on earth)
- We use distance of a place from destination while taking neighbours.

---

## Usage

1. Enter the source location.
2. Enter the destination.
3. Select an algorithm:
   - Dijkstra
   - A*
4. Click **Find Route**.
5. View:
   - Route on interactive map
   - Total distance
   - Execution time
   - Number of nodes traversed
   - Weather factor
   - Traffic factor

---

## Sample Output

```
Distance (m):      5321
Runtime (s):       0.01842
Nodes Traversed:   247
Weather Factor:    1.10
Traffic Factor:    1.35
```

---

## Concepts Used

- Graph Theory
- Shortest Path Algorithms
- Geographic Information Systems (GIS)
- Real-Time API Integration
- Heuristic Search
- Interactive Web Applications

---





Project: **LANIS – Live Adaptive Navigation & Intelligent System**
