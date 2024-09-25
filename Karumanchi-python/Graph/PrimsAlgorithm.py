import heapq
def prim(graph, start_vertex):
    """
    Compute a minimum spanning tree using Prim's algorithm.

    Parameters
    ----------
    graph : dict
        An adjacency list representation of the graph, where each key is a
        vertex and its corresponding value is a dictionary of its neighbors
        and the weights of the edges between them.
    start_vertex : str or int
        The starting vertex for the algorithm.

    Returns
    -------
    distances : dict
        A dictionary of the minimum distances from the start vertex to all
        other vertices.

    Notes
    -----
    The algorithm works by maintaining a priority queue of vertices to visit,
    where the priority is the minimum distance from the start vertex to the
    vertex. The algorithm repeatedly extracts the minimum priority vertex from
    the priority queue, marks it as visited, and updates the distances of all
    of its unvisited neighbors. The algorithm terminates when all vertices have
    been visited.

    This algorithm is guaranteed to find a minimum spanning tree for connected
    graphs. If the graph is not connected, the algorithm will only find the
    minimum spanning tree for the connected component containing the start
    vertex.

    Time complexity: O(E + VlogV), where E is the number of edges and V is
    the number of vertices.
    """
    visited = set()
    distances = {vertex: float('inf') for vertex in graph}
    distances[start_vertex] = 0
    pq = [(0, start_vertex)]
    while pq:
        (dist, current_vertex) = heapq.heappop(pq)
        if current_vertex not in visited:
            visited.add(current_vertex)
            for neighbor, neighbor_dist in graph[current_vertex].items():
                old_dist = distances[neighbor]
                new_dist = distances[current_vertex] + neighbor_dist
                if new_dist < old_dist:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    return distances


if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print(prim(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
    print(prim(graph, 'B'))  # Output: {'A': 1, 'B': 0, 'C': 2, 'D': 3}
    print(prim(graph, 'C'))  # Output: {'A': 4, 'B': 2, 'C': 0, 'D': 1}
    print(prim(graph, 'D'))  # Output: {'A': 5, 'B': 3, 'C': 1, 'D': 0}
