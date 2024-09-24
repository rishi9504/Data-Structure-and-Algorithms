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

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def __repr__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
    def get_connections(self):
        return self.adjacent.keys()
    
    def vertex_id(self):
        return self.id
    
    def getWeight(self, neighbor):
        return self.adjacent[neighbor]
    
    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def getPrevious(self):
        return self.previous

    def setVisited(self):
        self.visited = True

    def getVisited(self):
        return self.visited



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

if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addEdge('a','b',3)
    G.addEdge('a','c',2)
    G.addEdge('b','c',4)
    G.addEdge('b','d',2)
    G.addEdge('b','e',1)
    G.addEdge('c','d',1)
    G.addEdge('c','f',5)
    print("Graph Data")
    print (G.getEdges())                                                

# For this representaion the order of edges in the input is important. This is because
# they determine the order of the vertices on the adjacency list. The order in which 
# the edges are added determines the order of the vertices in the adjacency list.
# 
#   

# Here are some disadvantages of adjacency lists:

# 1. **Slower edge lookup**: In an adjacency list, finding an edge between two vertices can take O(n) time, where n is the number of edges incident on one of the vertices. This is because we need to search through the list of edges to find the one we're interested in.
# 2. **More memory usage**: Adjacency lists can use more memory than adjacency matrices, especially for dense graphs. This is because each edge is represented by a separate object, which can take up more memory than a single matrix entry.
# 3. **Difficult to determine if an edge exists**: In an adjacency list, it can be difficult to determine if an edge exists between two vertices without iterating through the entire list of edges.
# 4. **Not suitable for dense graphs**: Adjacency lists are not well-suited for dense graphs, where most vertices are connected to most other vertices. In such cases, an adjacency matrix may be more efficient.
# 5. **Insertion and deletion of edges can be slow**: Inserting or deleting an edge in an adjacency list can be slow, especially if the list is large. This is because we need to update the list of edges for both vertices involved in the edge.
# 6. **Not suitable for parallel processing**: Adjacency lists can be difficult to parallelize, as each thread may need to access and update the same list of edges.
# 7. **May require additional data structures**: Depending on the implementation, adjacency lists may require additional data structures, such as dictionaries or sets, to keep track of vertex indices or edge weights.

# These disadvantages can make adjacency lists less suitable for certain types of graph algorithms or applications, such as those that require fast edge lookup or dense graph representations.  