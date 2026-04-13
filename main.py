from graph import Graph
from dijkstra import dijkstra
from traffic import apply_traffic
from astar import astar, get_path

g = Graph()

g.add_edge("Hostel", "College", 5)
g.add_edge("College", "Hospital", 3)
g.add_edge("Hostel", "Mall", 10)
g.add_edge("Mall", "Hospital", 4)

# Apply traffic
traffic_graph = apply_traffic(g)

print("Graph with traffic:")
for node in traffic_graph:
    print(node, "->", traffic_graph[node])

# Dijkstra
print("\nDijkstra Result:")
dij = dijkstra(traffic_graph, "Hostel")
for node in dij:
    print(node, ":", dij[node])

# A*
print("\nA* Result (Hostel → Hospital):")
distances, came_from = astar(traffic_graph, "Hostel", "Hospital")
path = get_path(came_from, "Hostel", "Hospital")

print("Distance:", distances["Hospital"])
print("Path:", " -> ".join(path))