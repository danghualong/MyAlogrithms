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
        self.availablePaths=[(4,2,1),(6,3,1)]
        self._count=0
    
    def getBoard(self):
        return self.board
    def getAvailablePaths(self):
        return self.availablePaths
    @property
    def count(self):
        return self._count

    def optimize(self,paths,board,availablePaths):
        # print(board)
        if(board.count(1)<2):
            self._count+=1
            print("***************************")
            print(paths)
            return

        for nextPath in availablePaths:
            # print(nextPath)
            board[nextPath[0]-1]=0
            board[nextPath[1]-1]=0
            board[nextPath[2]-1]=1
            paths.append(nextPath)
            print(paths,board)
            nextPaths=[]
            for tmp in ForteenChess.RULES:
                if ((board[tmp[0]-1]==1) and (board[tmp[1]-1]==1) and (board[tmp[2]-1]==0)):
                    nextPaths.append(tmp)
            self.optimize(paths,board,nextPaths)
        popPath=paths.pop()
        board[popPath[0]-1]=1
        board[popPath[1]-1]=1
        board[popPath[2]-1]=0
        print("exit....")
        
    


        

chess=ForteenChess()
board=chess.getBoard()
availablePaths=chess.getAvailablePaths()
chess.optimize([],board,availablePaths)

print(chess.count)
