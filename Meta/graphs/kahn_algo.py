from collections import defaultdict, deque

def kahn_tophological_sort(num_vertices, edges):
    # step 1: buld the adjacency list and compute in-degrees
    graph = defaultdict(list)
    in_degree = [0] * num_vertices

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # step 2: init the queue with nodes having in=dgree 0
    queue = deque([v for v in range(num_vertices) if in_degree[v] == 0])
    topo_order = []

    # step 3: process the queue
    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # step 4: check for cycle
    if len(topo_order) != num_vertices:
        raise ValueError("Graph contains a cycle, topological sor not possible")
    
    return topo_order


# example:
edges = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]

result = kahn_tophological_sort(6, edges)
print("Toplogical Order", result)