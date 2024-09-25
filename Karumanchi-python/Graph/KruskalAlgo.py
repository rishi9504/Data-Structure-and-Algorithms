import heapq
def Kruskal(graph):
    """
    Compute the minimum spanning tree using Kruskal's algorithm.

    Parameters
    ----------
    graph : dict
        An adjacency list representation of the graph, where each key is a
        vertex and its corresponding value is a dictionary of its neighbors
        and the weights of the edges between them.

    Returns
    -------
    edges : list
        A list of edges in the minimum spanning tree.

    Notes
    -----
    The algorithm works by maintaining a priority queue of edges to visit,
    where the priority is the weight of the edge. The algorithm repeatedly
    extracts the minimum weight edge from the priority queue, checks if it
    forms a cycle with any of the edges already in the spanning tree, and
    adds it to the spanning tree if it doesn't. The algorithm terminates
    when all edges have been visited.

    This algorithm is guaranteed to find a minimum spanning tree for connected
    graphs. If the graph is not connected, the algorithm will only find the
    minimum spanning tree for the connected component containing the starting
    vertex.

    This algorithm is not guaranteed to find the optimal solution for all
    graphs.
    """
    edges = []
    visited = set()
    heap = [(weight, (u, v)) for u, neighbors in graph.items() for v, weight in neighbors.items()]
    heapq.heapify(heap)
    while heap:
        weight, (u, v) = heapq.heappop(heap)
        if (u, v) in visited or (v, u) in visited:
            continue
        edges.append((u, v, weight))
        visited.add((u, v))
        visited.add((v, u))
    return edges

if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 2},
        'B': {'A': 1, 'C': 3},
        'C': {'A': 2, 'B': 3},
        'D': {'E': 1},
        'E': {'D': 1}
    }
    print(Kruskal(graph))