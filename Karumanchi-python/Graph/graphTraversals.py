from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited_order = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                visited_order.append(vertex)

                if vertex in self.graph:
                    for neighbor in self.graph[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)

        return visited_order

# Example usage:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

start_vertex = 'A'
visited_order = g.bfs(start_vertex)
print(visited_order)  # Output: ['A', 'B', 'C', 'D', 'E']

# This code defines a Graph class that uses a dictionary to represent the graph, where each key is a vertex and its corresponding value is a list of its neighbors. The add_edge method is used to add edges to the graph, and the bfs method performs the BFS traversal.

# The bfs method uses a queue to keep track of vertices to visit next. It starts with the start_vertex and repeatedly removes a vertex from the queue, marks it as visited, and adds its unvisited neighbors to the queue.

# The visited_order list keeps track of the order in which vertices are visited. The method returns this list as the result of the BFS traversal.

# Note that this implementation assumes that the graph is represented as an undirected graph. If the graph is directed, the add_edge method should be modified to add edges in both directions.

# Also, this implementation uses a set to keep track of visited vertices, which has an average time complexity of O(1) for lookups. This makes the overall time complexity of the BFS algorithm O(V + E), where V is the number of vertices and E is the number of edges.




class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start_vertex):
        visited = set()
        traversal_order = []
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                traversal_order.append(vertex)

                if vertex in self.graph:
                    for neighbor in reversed(self.graph[vertex]):
                        if neighbor not in visited:
                            stack.append(neighbor)

        return traversal_order
    


# Example usage:
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.add_edge('D', 'E')

start_vertex = 'A'
visited_order = g.dfs(start_vertex)
print(visited_order)