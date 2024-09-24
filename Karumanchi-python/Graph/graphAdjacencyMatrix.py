class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacent = {}

    def add_neighbor(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    def __str__(self):
        return str(self.name) + ' adjacent: ' + str([x for x in self.adjacent])

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.name

    def get_weight(self, vertex):
        return self.adjacent[vertex]
    
class Graph:
    def __init__(self,num_vertices,cost=0):
        self.adjMatrix = [[-1]*(num_vertices) for i in range(num_vertices)]
        self.num_vertices = num_vertices
        self.vertices =[]
        for i in range(num_vertices):
            new_vertex = Vertex(i)
            self.vertices.append(new_vertex)


def test_graph():
    g = Graph(6)
    g.vertices[0].add_neighbor(g.vertices[1], 5)
    g.vertices[0].add_neighbor(g.vertices[5], 2)
    g.vertices[1].add_neighbor(g.vertices[2], 4)
    g.vertices[2].add_neighbor(g.vertices[3], 9)
    g.vertices[3].add_neighbor(g.vertices[4], 7)
    g.vertices[3].add_neighbor(g.vertices[5], 1)
    g.vertices[4].add_neighbor(g.vertices[0], 1)
    g.vertices[5].add_neighbor(g.vertices[4], 8)
    g.vertices[5].add_neighbor(g.vertices[2], 3)
    for v in g.vertices:
        for adj in v.get_connections():
            print("( %s , %s )" % (v.get_id(), adj.get_id()))

            
if __name__ == '__main__':
    test_graph()