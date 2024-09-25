from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[v] += 1

    def topological_sort(self):
        queue = deque([u for u in self.graph if self.in_degree[u] == 0])
        sorted_vertices = []

        while queue:
            u = queue.popleft()
            sorted_vertices.append(u)

            for v in self.graph[u]:
                self.in_degree[v] -= 1
                if self.in_degree[v] == 0:
                    queue.append(v)

        if len(sorted_vertices) != len(self.graph):
            raise ValueError("Graph has a cycle")

        return sorted_vertices

# Example usage:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

sorted_vertices = g.topological_sort()
print(sorted_vertices)  # Output: ['A', 'C', 'B', 'D', 'E']