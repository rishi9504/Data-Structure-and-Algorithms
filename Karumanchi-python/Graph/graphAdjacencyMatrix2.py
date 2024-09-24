class Vertex:
    def __init__(self, node):
        self.id = node
        # mark all nodes as not visited
        self.visited = False
        # store adjacent nodes
        self.adjacent = {}

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
    def __init__(self,numVertices,cost=0):
        self.adjMatrix = [[-1]*(numVertices) for i in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(numVertices):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)

    def setVertex(self,vtx, id):
        if 0 < vtx < self.numVertices:
            self.vertices[vtx].setVertexId(id)

    def getVertex(self,n):
        for vetxin in range(0, self.numVertices):
            if self.vertices[vetxin].getVertexId() == n:
                return vetxin
        return -1  

    def add_edge(self, v1, v2, cost=0):
        if self.getVertex(v1) == -1 or self.getVertex(v2) == -1:
            self.adjMatrix[self.getVertex(v1)][self.getVertex(v2)] = cost
            self.adjMatrix[self.getVertex(v2)][self.getVertex(v1)] = cost

    def getVertices(self):
        vertices=[]
        for i in range(0, self.numVertices):
            vertices.append(self.vertices[i].getVertexId())

        return vertices
    
    def printMatrix(self):
        for i in range(0, self.numVertices):
            row=[]
            for j in range(0, self.numVertices):
                row.append(self.adjMatrix[i][j])
            print(row)

    def getEdges(self):
        edges=[]
        for i in range(0, self.numVertices):
            for j in range(0, self.numVertices):

                if self.adjMatrix[i][j] != -1:
                    vid = self.vertices[i].getVertexId()
                    vid2 = self.vertices[j].getVertexId()
                    edges.append((vid, vid2, self.adjMatrix[i][j]))
        return edges

if __name__ == '__main__':
    g = Graph(6)
    g.setVertex(0,'a')
    g.setVertex(1,'b')
    g.setVertex(2,'c')
    g.setVertex(3,'d')
    g.setVertex(4,'e')
    g.setVertex(5,'f')
    print("Graph Data")
    g.add_edge('a','b',3)
    g.add_edge('a','c',2)
    g.add_edge('b','c',4)
    g.add_edge('b','d',2)
    g.add_edge('b','e',1)
    g.add_edge('c','d',1)
    g.add_edge('c','f',5)
    g.add_edge('d','e',1)
    g.add_edge('d','f',3)
    g.add_edge('e','f',2)
    print (g.printMatrix())
    print (g.getEdges())                       
                                        