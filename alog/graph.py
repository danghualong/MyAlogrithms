

class Graph(object):
    def __init__(self,vs,edges):
        self.vs=vs
        self.edges=edges
        inf=float('inf')
        self.selectedVs=[]
        m=len(self.vs)
        self.distances=[[inf,False,[]] for i in range(m)]
    #bellman-ford算法
    def getMinPath(self,start):
        inf=float('inf')
        dst=[inf for i in range(len(self.vs))]
        dst[start]=0
        m=len(self.vs)
        n=len(self.edges)
        for k in range(1,m):
            for i in range(n):
                f=self.edges[i][0]-1
                e=self.edges[i][1]-1
                w=self.edges[i][2]
                if(dst[f]!=inf):
                    if(dst[f]+w<dst[e]):
                        dst[e]=dst[f]+w
        print(dst)
    #dijkstra算法
    def getMinPath2(self,start):
        m=len(self.vs)
        inf=float('inf')
        result=[[inf,[]] for i in range(m)]
        result[start][0]=0
        result[start][1].append(start+1)
        self.selectedVs.append(start+1)
        edges=self.edges[:]
        selectedCount=(len(self.selectedVs))
        while(selectedCount<m):
            #计算其他点距离当前顶点的距离
            tmpEdges=self.getFilterEdges(edges,self.selectedVs[selectedCount-1])
            for edge in tmpEdges:
                if(result[edge[0]-1][0]+edge[2]<result[edge[1]-1][0]):
                    result[edge[1]-1][0]=result[edge[0]-1][0]+edge[2]
                    result[edge[1]-1][1]=result[edge[0]-1][1][:]
                    result[edge[1]-1][1].append(edge[1])
            #排序最小值
            miniNodeNum=self.getMinNode(result)
            self.selectedVs.append(miniNodeNum)
            selectedCount=(len(self.selectedVs))
        print(result)             
            
    
    def getFilterEdges(self,edges,cur):
        v=list(filter(lambda x:x[0]==cur and (x[1] not in self.selectedVs),edges))
        return v
            
    def getMinNode(self,result):
        minIndex=-1
        minVal=float('inf')
        for i in range(len(result)):
            if(i+1 not in self.selectedVs):
                if(minVal>result[i][0]):
                    minVal=result[i][0]
                    minIndex=i
        return minIndex+1
    #回溯法寻找最小路径
    def getMinPath3(self,start):
        self.distances[start][0]=0
        self.distances[start][1]=True
        self.distances[start][2].append(start+1)
        self.backtrack(start)
        print(self.distances)

    def getMinPathAll(self):
        for i in range(len(self.vs)):
            self.distances.clear()
            self.getMinPath(i)
    
    def backtrack(self,start):
        selectedEdges=list(filter(lambda x:x[0]==start+1,self.edges))
        for edge in selectedEdges:
            endIndex=edge[1]-1
            if(not self.distances[endIndex][1]):
                if(self.distances[start][0]+edge[2]<self.distances[endIndex][0]):
                    self.distances[endIndex][0]= self.distances[start][0]+edge[2]
                    self.distances[endIndex][2]=self.distances[start][2][:]
                    self.distances[endIndex][2].append(edge[1])
                self.distances[endIndex][1]=True
                self.backtrack(endIndex)
                self.distances[endIndex][1]=False


vs=[1,2,3,4,5,6]
edges=[(1,2,1),(2,1,1),(1,3,2),(3,1,2),(3,6,4),(6,3,4),(3,5,2),(5,3,2),(3,4,2),(4,3,2),(2,4,3),(4,2,3),(2,5,1),(5,2,1),(4,5,2),(5,4,2),(5,6,1),(6,5,1)]
g=Graph(vs,edges)
g.getMinPath(0)
g.getMinPath2(0)
g.getMinPath3(0)

g.getMinPathAll()

        
