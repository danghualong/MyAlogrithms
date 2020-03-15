
#最小生成树算法(MST)
class Solution(object):
    def __init__(self,vs,edges):
        self.vs=vs
        self.edges=edges
        self.n=len(vs)
        self.sortEdges()
        self.tree=[i for i in range(self.n)]
        self.selectedEdgeds=[]

    def sortEdges(self):
        self.edges.sort(key=lambda x:x[2])

    def isClosed(self,edge):
        p1=self.ancestor(edge[0]-1)
        p2=self.ancestor(edge[1]-1)
        if(not p1==p2):
            self.tree[p2]=p1
        return p1==p2

    def ancestor(self,v):
        while(self.tree[v]!=v):
            v=self.tree[v]
        return v

    def solve(self):
        while(len(self.selectedEdgeds)<self.n-1):
            edge=self.edges[0]
            if(not self.isClosed(edge)):
                self.tree[edge[1]-1]=edge[0]-1
                self.selectedEdgeds.append(edge)
            self.edges.pop(0)

vs=[1,2,3,4,5,6]
edges=[(1,2,5),(1,6,4),(1,3,3),(2,5,5),(2,3,4),(3,6,6),(3,4,6),(4,5,7),(5,6,6)]

s=Solution(vs,edges)
s.solve()
print(s.selectedEdgeds)




def prim(vs,edges):
    selectedEdges=[]
    selectedVs={1}
   
    while(len(selectedVs)<len(vs)):
        minWeight=100
        selectedEdge=None
        for selectedV in selectedVs:
            for edge in edges:
                if(edge[0] in selectedVs and edge[1] in selectedVs):
                    continue
                if(edge[0]==selectedV) or (edge[1]==selectedV):
                    if(minWeight>edge[2]):
                        minWeight=edge[2]
                        selectedEdge=edge
        selectedEdges.append(selectedEdge)
        selectedVs.add(selectedEdge[1])
        selectedVs.add(selectedEdge[0])
    print(selectedEdges)

vs=[1,2,3,4,5,6]
edges=[(1,2,5),(1,6,4),(1,3,3),(2,5,5),(2,3,4),(3,6,6),(3,4,6),(4,5,7),(5,6,6)]
prim(vs,edges)


            


        