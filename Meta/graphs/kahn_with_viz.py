import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque

class KahnTopologicalSorter:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)
        self.in_degree = [0] * num_vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[v] += 1

    def sort(self):
        queue = deque([v for v in range(self.num_vertices) if self.in_degree[v] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for neighbor in self.graph[node]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) != self.num_vertices:
            raise ValueError("Graph contains a cycle, topological sort not possible")

        return topo_order

    def visualize(self):
        G = nx.DiGraph()
        for u in self.graph:
            for v in self.graph[u]:
                G.add_edge(u, v)

        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, arrowsize=25)
        plt.title("Graph Visualization")
        plt.show()
sorter = KahnTopologicalSorter(6)
edges = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]

for u, v in edges:
    sorter.add_edge(u, v)

topo_order = sorter.sort()
print("Topological Order:", topo_order)

sorter.visualize()
