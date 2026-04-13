import heapq

def heuristic(a, b):
    return abs(len(a) - len(b))  # simple heuristic

def astar(graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    came_from = {}

    while pq:
        current_cost, current_node = heapq.heappop(pq)

        if current_node == goal:
            break

        for neighbor, weight in graph[current_node]:
            new_cost = distances[current_node] + weight

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(pq, (priority, neighbor))
                came_from[neighbor] = current_node

    return distances, came_from
def get_path(came_from, start, goal):
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = came_from.get(node, start)

    path.append(start)
    path.reverse()
    return path