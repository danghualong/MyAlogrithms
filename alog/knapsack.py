#背包问题（回溯法)


class Knapsack(object):
    def __init__(self,ws,cs,target):
        self.n=len(ws)
        self.states=[0 for i in range(self.n)]
        self.ws=ws
        self.cs=cs
        self.target=target
        self.maxCost=0
        self.paths=[]

    def solve(self,depth):
        if(depth>=self.n):
            self.handle()
        else:
            self.states[depth]=1
            self.solve(depth+1)
            self.states[depth]=0
            self.solve(depth+1)
        
    def handle(self):
        tw=0
        tc=0
        for i in range(self.n):
            if(self.states[i]==1):
                tw+=self.ws[i]
                tc+=self.cs[i]
        if(tw<=self.target):
            if(tc>self.maxCost):
                self.maxCost=tc
                self.paths.clear()
                self.paths.append(self.states[:])
            elif(tc==self.maxCost):
                self.paths.append(self.states[:])
    def printResult(self):
        print("Max cost is:",self.maxCost)
        print("Paths:",len(self.paths))
        for i in range(len(self.paths)):
            print("Path{0}:".format(i+1))
            print(self.paths[i])


ws=[1,2,3,4,5]
cs=[20,30,65,40,60]
target=10
o=Knapsack(ws,cs,target)
o.solve(0)
o.printResult()

