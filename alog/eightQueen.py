def isProper(board,row,col):
    return isRowProper(board,row,col) and isAngleProper(board,row,col) and isAntiAngleProper(board,row,col)
def isRowProper(board,row,col):
    for i in range(row):
        if(board[i][col]==1):
            return False
    return True
def isAngleProper(board,row,col):
    k=col if row>col else row
    for i in range(k):
        if(board[row-i-1][col-i-1]==1):
            return False
    return True
def isAntiAngleProper(board,row,col):
    n=len(board)
    for i in range(row):
        if(col+i+1<n):
            if(board[row-i-1][col+i+1]==1):
                return False
    return True

class EightQueen(object):
    def __init__(self,n):
        self.n=n
        self.board=[]
        for i in range(n):
            self.board.append([0 for j in range(n)])
        self.paths=[]

    def solve(self,row):
        if(row>=self.n):
            self.saveResult()
        else:
            for i in range(self.n):
                if(isProper(self.board,row,i)):
                    self.board[row][i]=1
                    self.solve(row+1)
                    self.board[row][i]=0

    def saveResult(self):
        path=[]
        for i in range(self.n):
            for j in range(self.n):
                if(self.board[i][j]==1):
                    path.append((i,j))
                    break
        self.paths.append(path)

o=EightQueen(8)
o.solve(0)
print("total paths:",len(o.paths))
print(o.paths)



        