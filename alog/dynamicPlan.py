class Node(object):
    def __init__(self,name):
        self._name=name
        self._distance=0
        self._origins=[]
    
    def getName(self):
        return self._name

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self,distance):
        self._distance = distance

    @property
    def origins(self):
        return self._origins
        
    def addOrigin(self,tmpOrigin):
        if tmpOrigin!=None:
            self._origins.append(tmpOrigin)
            
    def clearOrigins(self):
        self._origins.clear()

    def __repr__(self):
        str="name:{0},distance:{1},origins:{2}".format(self._name,self._distance,self._origins)
        return str

class Edge(object):
    def __init__(self,fromIndex,toIndex,weight):
        self._fromIndex=fromIndex
        self._toIndex=toIndex
        self._weight=weight
    @property
    def fromIndex(self):
        return self._fromIndex
    @property
    def toIndex(self):
        return self._toIndex
    @property
    def weight(self):
        return self._weight

class Graph(object):
    def __init__(self):
        self._nodes=[]
        self._edges=[]
        self._result=None
        self._queue=[]

    def addNode(self,node):
        self._nodes.append(node)
    def addEdge(self,edge):
        self._edges.append(edge)
    
    @property
    def nodes(self):
        return self._nodes
    @property
    def edges(self):
        return self._edges

    def dfs(self,node,k):
        if(node.getName()==k):
            self._result=node
            return node
        node.visited=True
        index=self._nodes.index(node)
        tmpNodes=[self._nodes[e.toIndex] for e in self._edges if e.fromIndex==index]
        for n in tmpNodes:
            if(not n.visited):
                self.dfs(n,k)
        return self._result
    
    def bfs(self,root,k):
        self._queue.append(root)
        while(len(self._queue)>0):
            node=self._queue.pop(0)
            if(not node.visited):
                index=self._nodes.index(node)
                tmpNodes=[self._nodes[e.toIndex] for e in self._edges if (e.fromIndex==index)]
                for t in tmpNodes:
                    self._queue.append(t)
                node.visited=True 
                if(node.getName()==k):
                    return node
        return None
        

class MyNode(Node):
    def __init__(self,name):
        super(MyNode,self).__init__(name)
        self._visited=False
    @property
    def visited(self):
        return self._visited
    @visited.setter
    def visited(self,v):
        self._visited = v
    


def initGraph():
    graph=Graph()
    graph.addNode(Node('A'))
    graph.addNode(Node('B1'))
    graph.addNode(Node('B2'))
    graph.addNode(Node('C1'))
    graph.addNode(Node('C2'))
    graph.addNode(Node('C3'))
    graph.addNode(Node('D1'))
    graph.addNode(Node('D2'))
    graph.addNode(Node('E'))
    graph.addEdge(Edge(0,1,10))
    graph.addEdge(Edge(0,2,12))    
    graph.addEdge(Edge(1,3,7))
    graph.addEdge(Edge(2,3,10))
    graph.addEdge(Edge(1,4,9))
    graph.addEdge(Edge(2,5,6))
    graph.addEdge(Edge(3,6,4))
    graph.addEdge(Edge(4,6,6))
    graph.addEdge(Edge(5,6,7))
    graph.addEdge(Edge(3,7,5))
    graph.addEdge(Edge(4,7,6))
    graph.addEdge(Edge(5,7,8))
    graph.addEdge(Edge(6,8,11))
    graph.addEdge(Edge(7,8,9))
    return graph

def calc(graph):
    for i in range(len(graph.nodes)):
        vertex=graph.nodes[i]
        edges=[e for e in graph.edges if e.toIndex==i]
        if(len(edges)>0):
            min=float('inf')
            for j in range(len(edges)):
                tmp=graph.nodes[edges[j].fromIndex].distance+edges[j].weight
                if(tmp<min):
                    min=tmp
                    vertex.clearOrigins()
                    vertex.addOrigin(edges[j].fromIndex)
                elif(tmp==min):
                    vertex.addOrigin(edges[j].fromIndex)
            vertex.distance=min
    # print(vertexes)
    
def buildRoutes(graph):
    routes=[]
    vertexes=graph.nodes
    vertex=vertexes[len(vertexes)-1]
    routes.append({'name':vertex.getName(),'distance':vertex.distance})
    while(True):
        origins=vertex.origins
        vertex=vertexes[origins[0]]
        routes.append({'name':vertex.getName(),'distance':vertex.distance})
        if(len(vertex.origins)<=0):
            break
    routes.reverse()
    print(routes)

def initGraph2():
    graph=Graph()
    graph.addNode(MyNode('A'))
    graph.addNode(MyNode('B'))
    graph.addNode(MyNode('C'))
    graph.addNode(MyNode('D'))
    graph.addNode(MyNode('E'))
    graph.addNode(MyNode('F'))
    graph.addEdge(Edge(0,1,10))
    graph.addEdge(Edge(1,2,12))    
    graph.addEdge(Edge(1,3,7))
    graph.addEdge(Edge(1,4,10))
    graph.addEdge(Edge(2,4,9))
    graph.addEdge(Edge(2,5,6))
    graph.addEdge(Edge(5,0,4))
    return graph

if __name__=="__main__":
    #动态规划
    graph=initGraph()
    calc(graph)
    buildRoutes(graph)
    #DFS遍历搜索
    graph=initGraph2()
    f1=graph.dfs(graph.nodes[0],'D')
    print(f1)
    #ddd
    f2=graph.bfs(graph.nodes[0],'F')
    print(f2)

