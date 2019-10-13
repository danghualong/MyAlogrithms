<<<<<<< HEAD
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

=======


class Knapsack(object):
    def __init__(self,ws,cs,targetWt):
        self.ws=ws
        self.cs=cs
        self.target=targetWt
        self.n=len(ws)
        self.board=[0 for j in range(self.n)]
        self.maxCost=0
        self.paths=[]

    def isValid(self,board):
        tw=0
        for i in range(self.n):
            if(board[i]==1):
                tw+=self.ws[i]
        return tw<=self.target

    def solve(self,row):
        if(row>=self.n):
            self.saveResult(self.board)
        else:
            self.board[row]=1
            if(self.isValid(self.board)):
                self.solve(row+1)
            self.board[row]=0
            self.solve(row+1)

    def saveResult(self,board):
        sum=0
        for i in range(self.n):
            if(board[i]==1):
                sum+=self.cs[i]
        if(sum>self.maxCost):
            self.maxCost=sum
            self.paths.clear()
            self.paths.append(board[:])
        elif(sum==self.maxCost):
            self.paths.append(board[:])

ws=[1,2,3,4,5]
cs=[20,30,30,40,50]
target=10
o=Knapsack(ws,cs,target)
o.solve(0)
print("max cost is:",o.maxCost)
print("paths:",o.paths)



        
>>>>>>> 83d903f283ead19ac73bdea4f4c716b97e18e4d2
