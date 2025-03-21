from collections import defaultdict

class GraphCycleDetector:
    def __init__(self, num_vertices):
        self.graph = defaultdict(list)
        self.num_vertices = num_vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def has_cycle(self):
        visited = [False] * self.num_vertices
        recursion_stack = [False] * self.num_vertices

        def dfs(node):
            visited[node] = True
            recursion_stack[node] = True

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                    
                elif recursion_stack[neighbor]:
                    return True
            
        for v in range(self.num_vertices):
            if not visited[v]:
                if dfs(v):
                    return True
        
        return False
    

g = GraphCycleDetector(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)  # Back edge creates a cycle

print("Has cycle:", g.has_cycle())