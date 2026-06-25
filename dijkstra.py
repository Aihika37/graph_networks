import heapq

def dijkstra(G, source, destination):
    pq = [(0, source)]
    dist = {node: float("inf")for node in G.nodes}#distance from source
    parent = {}
    dist[source] = 0
    while pq:
        cost, node = heapq.heappop(pq)
        if node == destination:
            break
        for nbr in G.neighbors(node):
            edge_data = G[node][nbr]
            first_key = list(edge_data.keys())[0]
            weight = edge_data[first_key].get("dynamic_weight",
                    edge_data[first_key].get("length", 1))#getting dynamic weight if possible
            new_cost = cost + weight
            if new_cost < dist[nbr]:#if relaxation possible
                dist[nbr] = new_cost
                parent[nbr] = node
                heapq.heappush(pq,(new_cost, nbr))

    #reconstructing the path
    path = []
    cur = destination
    while cur != source:
        path.append(cur)
        cur = parent[cur]
    path.append(source)
    path.reverse()
    return path, dist[destination]