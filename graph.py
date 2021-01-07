class Vertex:
    def __init__(self, vertexID,x,y,label):
        self.vertexID = vertexID
        self.x = x
        self.y = y
        self.label = label
        self.adjacent = []
        self.previous = None

class Edge:
    def __init__(self,vertex1,vertex2,weight=0):
        self.v1 = vertex1
        self.v2 = vertex2
        self.weight = weight

    def __lt__(self,other):
        return self.weight < other.weight


