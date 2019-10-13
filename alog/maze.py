#迷宫问题
class Solution(object):
    def __init__(self,vs,es):
        self.vs=vs
        self.es=es
        n=len(vs)
        self.tv=n
        self.arr=[]
        for i in range(n):
            self.arr.append([-1 for j in range(n)]) 
        for i in range(len(es)):
            self.arr[es[i][0]][es[i][1]]=es[i][2]
            self.arr[es[i][1]][es[i][0]]=es[i][2]
        self.paths=[]

        

    def solve(self,num):
        if(num==(self.tv-1)):
            self.paths.append(num)
            print(self.paths)
            self.paths.pop()
        else:
            if(self.vs[num]['visited']==0):
                self.paths.append(num)
                self.vs[num]['visited']=1
                for i in range(self.tv):
                    if(self.arr[num][i]==1 and self.vs[i]['visited']==0):
                        self.solve(i)
                self.vs[num]['visited']=2
                self.paths.pop()




vs=[{'index':i,'visited':0} for i in range(9)]
es=[[0,3,1],[3,4,1],[4,7,1],[4,5,1],[7,8,1],[5,2,1],[5,8,1]]

s=Solution(vs,es)
s.solve(0)



        