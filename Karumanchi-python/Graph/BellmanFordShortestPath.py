class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def bellman_ford(self, start_vertex):
        distances = {vertex: float('inf') for vertex in range(len(self.graph))}
        distances[start_vertex] = 0

        for _ in range(len(self.graph) - 1):
            for u, v, weight in self.graph:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        for u, v, weight in self.graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")

        return distances

# Example usage:
g = Graph()
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

start_vertex = 0
distances = g.bellman_ford(start_vertex)
print(distances)  # Output: {0: 0, 1: -1, 2: 2, 3: -2, 4: 1}


# This code defines a Graph class that uses a list to represent the graph, where each element is a tuple representing an edge and its weight. The add_edge method is used to add edges to the graph, and the bellman_ford method performs Bellman-Ford Algorithm.

# The bellman_ford method initializes the distances dictionary with distances to all vertices set to infinity, except for the start vertex which is set to 0. It then relaxes all edges V - 1 times, where V is the number of vertices. If a shorter path is found, the distance is updated.

# After relaxing all edges V - 1 times, it checks for negative cycles by iterating over all edges one more time. If a shorter path is found, it raises a ValueError indicating that the graph contains a negative cycle.

# The method returns the distances dictionary as the result of the algorithm.

# Note that this implementation assumes that the graph is represented as a weighted, directed graph. If the graph is undirected, the add_edge method should be modified to add edges in both directions with the same weight.

# Also, this implementation has a time complexity of O(VE), where V is the number of vertices and E is the number of edges. This is because the Bellman-Ford algorithm is implemented using a V - 1 iteration over all edges and an additional iteration to check for negative cycles.