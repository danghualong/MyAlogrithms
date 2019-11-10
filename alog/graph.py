INF=float('inf')

class Graph(object):
    def __init__(self,vs,edges):
        self.vs=vs
        self.edges=edges
    
    def refresh(self):
        for v in self.vs:
            v.distance=INF
            v.paths=None
            v.visited=False

    def showPaths(self):
        dst=list(map(lambda x: x.distance,self.vs))
        print(dst)
        if(self.vs[0].paths!=None):
            paths=list(map(lambda x: x.paths,self.vs))
            print(paths)
        
    def findAdjEdges(self,node):
        result=[]
        for edge in self.edges:
            if(edge.fromName==node.name):
                result.append(edge)
        return result
    
    def findVertex(self,name):
        for v in self.vs:
            if(v.name==name):
                return v
        return None

    #bellman-ford算法
    def getShortestPath(self):
        self.vs[0].distance=0
        m=len(self.vs)
        n=len(self.edges)
        for k in range(1,m):
            for i in range(n):
                f=self.findVertex(self.edges[i].fromName)
                e=self.findVertex(self.edges[i].toName)
                w=self.edges[i].weight
                if(f.distance!=INF):
                    if(f.distance+w<e.distance):
                        e.distance=f.distance+w
        self.showPaths()

    #dijkstra算法
    def getMinPath2(self,start):
        m=len(self.vs)
        startNode=self.vs[start]
        startNode.paths=[startNode.name]
        startNode.distance=0
        selectedVs=[]
        selectedVs.append(startNode.name)
        selectedCount=(len(selectedVs))
        edges=self.edges[:]
        while(selectedCount<m):
            #计算其他点距离当前顶点的距离
            curNodeName=selectedVs[selectedCount-1]
            tmpEdges=self.getUnselectedAdjEdges(edges,curNodeName,selectedVs)
            for edge in tmpEdges:
                curNode=self.findVertex(curNodeName)
                toNode=self.findVertex(edge.toName)
                if(curNode.distance+edge.weight<toNode.distance):
                    toNode.distance=curNode.distance+edge.weight
                    toNode.paths=curNode.paths[:]
                    toNode.paths.append(edge.toName)
            #查找从原点到剩余点的最小距离
            nextNodeName=self.getMinNode(selectedVs)
            selectedVs.append(nextNodeName)
            selectedCount=(len(selectedVs))
        self.showPaths()            

    def getUnselectedAdjEdges(self,edges,curNodeName,selectedVs):
        v=list(filter(lambda x:x.fromName==curNodeName and (x.toName not in selectedVs),edges))
        return v
            
    def getMinNode(self,selectedVs):
        nodeName=None
        minVal= INF
        for node in self.vs:
            if(node.name not in selectedVs):
                if(minVal>node.distance):
                    minVal=node.distance
                    nodeName=node.name
        return nodeName

    #回溯法寻找最短路径
    def getShortestPathByDFS(self):
        startNode=self.vs[0]
        startNode.distance=0
        self.backtrack(startNode)
        self.showPaths()

    def backtrack(self,startNode):
        startNode.visited=True
        tmpEdges=self.findAdjEdges(startNode)
        for edge in tmpEdges:
            otherNode=self.findVertex(edge.toName)
            #当前节点还未被访问
            if(not otherNode.visited):
                if(startNode.distance+edge.weight<otherNode.distance):
                    otherNode.distance=startNode.distance+edge.weight
                self.backtrack(otherNode)
                otherNode.visited=False
                

    #遍历
    def search(self):
        self.DFS(self.vs[0])
    #深度优先
    def DFS(self,node):
        print(node.name)
        node.visited=True
        adjEdges=self.findAdjEdges(node)
        for edge in adjEdges:
            v=self.findVertex(edge.toName)
            if(v!=None and (not v.visited)):
                self.DFS(v)
    #汉密尔顿路径
    def hamilton(self):
        for v in self.vs:
            self.refresh()
            paths=[]
            v.visited=True
            paths.append(v.name)
            self.findPath(v,paths)

    def findPath(self,v,paths):
        if(len(paths)>=len(self.vs)):
            print(paths)
        else:
            tmpEdges=self.findAdjEdges(v)
            for edge in tmpEdges:
                nextV=self.findVertex(edge.toName)
                if(not nextV.visited):
                    paths.append(nextV.name)
                    nextV.visited=True
                    self.findPath(nextV,paths)
                    nextV.visited=False
                    paths.pop()


class Vertex(object):
    def __init__(self,name):
        self._name=name
        self._visited=False
        self._distance=INF
        self._paths=None
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
    
    @property
    def visited(self):
        return self._visited
    @visited.setter
    def visited(self,visited):
        self._visited=visited

    @property
    def distance(self):
        return self._distance
    @distance.setter
    def distance(self,distance):
        self._distance=distance

    @property
    def paths(self):
        return self._paths
    @paths.setter
    def paths(self,paths):
        self._paths=paths
    

class Edge(object):
    def __init__(self,fromName,toName,weight):
        self._from=fromName
        self._to=toName
        self._weight=weight
    @property
    def fromName(self):
        return self._from
    @property
    def toName(self):
        return self._to
    @property
    def weight(self):
        return self._weight
    
    


vs=[]
for i in range(1,7):
    vs.append(Vertex(i))
edges=[Edge(1,2,1),Edge(2,1,1),Edge(1,3,2),Edge(3,1,2),Edge(3,6,4),Edge(6,3,4),Edge(3,5,2),Edge(5,3,2),Edge(3,4,2),Edge(4,3,2),
Edge(2,4,3),Edge(4,2,3),Edge(2,5,1),Edge(5,2,1),Edge(4,5,2),Edge(5,4,2),Edge(5,6,1),Edge(6,5,1)]

obj=Graph(vs,edges)
obj.search()
print("Bellman-ford paths:")
obj.refresh()
obj.getShortestPath()
print("Backtrack paths:")
obj.refresh()
obj.getShortestPathByDFS()
print("Dijkstra paths:")
obj.refresh()
obj.getMinPath2(0)
print("hamilton paths:")
obj.refresh()
obj.hamilton()

