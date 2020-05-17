import numpy as np

class MyNode(object):
    def __init__(self,name):
        self._name=name
        self._visited=False
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name
    @property
    def visited(self):
        return self._visited
    @visited.setter
    def visited(self,v):
        self._visited = v
# 最大面积岛屿（DFS)
class Graph(object):
    def __init__(self):
        self.max=0
        self.m=4
        self.n=8
        self.islands=np.empty((self.m,self.n),dtype=MyNode)
        # m,n=len(self.islands)
        for i in range(self.m):
            for j in range(self.n):
                self.islands[i][j]=MyNode(0)
        self.islands[0,1].name=1
        self.islands[0,7].name=1
        self.islands[1,1].name=1
        self.islands[1,2].name=1
        self.islands[1,3].name=1
        self.islands[1,7].name=1
        self.islands[2,1].name=1
        self.islands[2,3].name=1
        self.islands[2,4].name=1
        self.islands[2,7].name=1
        self.islands[3,2].name=1
        self.islands[3,5].name=1
        self.islands[3,6].name=1
        self.islands[3,7].name=1
        p=np.array([k.name for k in self.islands.flat])
        print(p.reshape(4,8))

    def findMax(self):
        for i in range(self.m):
            for j in range(self.n):
                count=self.find(i,j)
                if(count>self.max):
                    self.max=count

    def find(self,row,col):
        if(row<0 or col<0 or row>=self.m or col>=self.n):
            return 0
        item=self.islands[row,col]
        if(item.name==0 or item.visited):
            return 0
        item.visited=True
        count=1
        count+= self.find(row+1,col)
        count+= self.find(row,col+1)
        count+= self.find(row-1,col)
        count+= self.find(row,col-1)
        return count
           
        

                


g=Graph()
g.findMax()
print(g.max)
