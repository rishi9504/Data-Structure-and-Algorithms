class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = 1000000
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor of a node
        self.previous = None
        # Indegree count
        self.indegree = 0
        # Outdegree count
        self.outdegree = 0
    def add_neighbor(self, neighbor, G):
        G.add_edge(self.id, neighbor)

    def __str__(self):
        return str(self.id)
    
    def __repr__(self):
        return str(self)
    
    def get_connections(self):
        return G.adjMatrix[self.id]
    
    def getVertexId(self):
        return self.id
    
    def setVertexId(self, id):
        self.id = id

    def setVisited(self):
        self.visited = True

class Graph:
    def __init__(self):
        self.vertDict = {}
        self.numVertices = 0
    def __iter__(self):
        return iter(self.vertDict.values())

    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDict[node] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertDict:
            return self.vertDict[n]
        else:
            return None

    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vertDict:
            self.addVertex(frm)
        if to not in self.vertDict:
            self.addVertex(to)
        self.vertDict[frm].add_neighbor(self.vertDict[to], cost)
        self.vertDict[to].add_neighbor(self.vertDict[frm], cost)

    def getVertices(self):
        return self.vertDict.keys()

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous

    def getEdges(self):
        edges = []
        for v in G:
            for w in v.get_connections():
                vid = v.vertex_id()
                wid = w.vertex_id()
                edges.append((vid, wid, v.getWeight(w)))
        return edges


def topologicalSOrt(G):
    """
    Perform a topological sort of the nodes. If the graph has a cycle 
    throw a GraphTopologicalError exception with the list of successfully sorted nodes
    """
    # topologically sorted list of the nodes
    T = []
    # queue (fifo list) of the nodes with indegree 0
    Q = []
    # {node: indegree} dictionary for the remaining nodes
    remaining = {}
    nodes = G.getVertices()
    for node in nodes:
        remaining[node] = G.getVertex(node).indegree
        if remaining[node] == 0:
            Q.append(node)
    while Q:
        current = Q.pop(0)
        T.append(current)
        for neighbor in G.getVertex(current).get_connections():
            remaining[neighbor] = remaining[neighbor] - 1
            if remaining[neighbor] == 0:
                Q.append(neighbor)
    if len(T) != len(nodes):
        raise GraphTopologicalError(T)
    
    # printing the topological order
    for node in T:
        print(node, end = " ")

    return T

import unittest

class TestTopologicalSort(unittest.TestCase):

    def test_topological_sort(self):
        # Create a graph with the following structure:
        # A -> B -> C
        # A -> D
        # E -> F
        G = Graph()
        G.addVertex('A')
        G.addVertex('B')
        G.addVertex('C')
        G.addVertex('D')
        G.addVertex('E')
        G.addVertex('F')
        G.addEdge('A', 'B')
        G.addEdge('A', 'D')
        G.addEdge('B', 'C')
        G.addEdge('E', 'F')

        # Perform topological sort
        sorted_vertices = topologicalSOrt(G)

        # Check if the sorted vertices are in the correct order
        self.assertEqual(sorted_vertices, ['A', 'E', 'B', 'D', 'C', 'F'])

    def test_topological_sort_with_cycle(self):
        # Create a graph with a cycle:
        # A -> B -> C -> A
        G = Graph()
        G.addVertex('A')
        G.addVertex('B')
        G.addVertex('C')
        G.addEdge('A', 'B')
        G.addEdge('B', 'C')
        G.addEdge('C', 'A')

        # Perform topological sort
        with self.assertRaises(GraphTopologicalError):
            topologicalSOrt(G)

    def test_topological_sort_with_no_edges(self):
        # Create a graph with no edges
        G = Graph()
        G.addVertex('A')
        G.addVertex('B')
        G.addVertex('C')

        # Perform topological sort
        sorted_vertices = topologicalSOrt(G)

        # Check if the sorted vertices are in the correct order
        self.assertEqual(sorted_vertices, ['A', 'B', 'C'])

if __name__ == '__main__':
    unittest.main()