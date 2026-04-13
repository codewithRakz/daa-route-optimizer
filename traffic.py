import random

def apply_traffic(graph):
    traffic_graph = {}

    for node in graph.nodes:
        traffic_graph[node] = []

        for neighbor, weight in graph.nodes[node]:
            # Add random traffic delay (1 to 5)
            traffic = random.randint(1, 5)
            new_weight = weight + traffic

            traffic_graph[node].append((neighbor, new_weight))

    return traffic_graph