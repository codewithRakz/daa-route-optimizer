class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.nodes:
            self.nodes[from_node] = []
        if to_node not in self.nodes:
            self.nodes[to_node] = []

        self.nodes[from_node].append((to_node, weight))
        self.nodes[to_node].append((from_node, weight))  # undirected

    def display(self):
        for node in self.nodes:
            print(node, "->", self.nodes[node])