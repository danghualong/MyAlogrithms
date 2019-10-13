class ForteenChess(object):
    RULES=[(1,2,4),(1,3,6),(2,4,7),(2,5,9),
    (3,5,8),(3,6,10),(4,5,6),(4,7,11),
    (4,8,13),(5,8,12),(5,9,14),(6,10,15),
    (6,9,13),(7,8,9),(8,9,10),(12,13,14),
    (11,12,13),(13,14,15),
    (12,8,5),(11,7,4),
    (13,8,4),(13,9,6),(13,12,11),
    (14,13,12),(14,9,5),
    (9,5,2),(9,8,7),
    (10,6,3),(10,9,8),
    (8,5,3),(7,4,2),(6,3,1),(6,5,4),(4,2,1),(15,14,13),(15,10,6)]

    def __init__(self):
        self.board=[0]
        for i in range(14):
            self.board.append(1)
        self.result=[]
        self.singlePaths=[]


    def getPaths(self):
        paths=[]
        for i in range(len(self.board)):
            if(self.board[i]==0):
                for rule in ForteenChess.RULES:
                    if(rule[2]==(i+1) and self.board[rule[0]-1]==1 and self.board[rule[1]-1]==1):
                        paths.append(rule)
        return paths

    def optimize(self,depth):
        if(depth>=13):
            print(self.singlePaths[:])
            self.result.append(self.singlePaths[:])
        else:
            paths=self.getPaths()
            for path in paths:
                self.board[path[0]-1]=0
                self.board[path[1]-1]=0
                self.board[path[2]-1]=1
                self.singlePaths.append(path)
                self.optimize(depth+1)
                self.board[path[0]-1]=1
                self.board[path[1]-1]=1
                self.board[path[2]-1]=0
                self.singlePaths.pop()

    
o=ForteenChess()
o.optimize(0) 
print(len(o.result))           

    
