# 数独求解方法
def solvesudoku(board):
    stack=[]
    lastData=0
    i=0
    j=0
    while(i<9):
        while(j<9):
            # print("{0}*{1},lastData={2}".format(i,j,lastData))
            if(board[i*9+j]==0):
                for d in range(lastData+1,10):
                    if(isValid(board,i,j,d)):
                        # print("push:",(i,j,d))
                        stack.append((i,j,d))
                        board[i*9+j]=d
                        lastData=0
                        (i,j)=switchNext(i,j) 
                        break
                else:
                    if(len(stack)==0):
                        print("no solution")
                        return
                    tup=stack.pop()
                    board[tup[0]*9+tup[1]]=0
                    lastData=tup[2]
                    i=tup[0]
                    j=tup[1]
                    #print("back:",(i,j,lastData))
            else:
                (i,j)=switchNext(i,j)
            
    for i in range(9):
        print(board[i*9:i*9+9])

def solve(board,index):
    if(index>=81):
        print(board)
    else:
        if(board[index]==0):
            for i in range(1,10):
                row=int(index/9)
                col=int(index%9)
                if(isValid(board,row,col,i)):
                    board[index]=i
                    solve(board,index+1)
                    board[index]=0
        else:
            solve(board,index+1)

def switchNext(i,j):
    j+=1
    if(j==9):
        i+=1
        j=0
        if(i==9):
            j=9
            i=9
    return (i,j) 

def isValid(board,i,j,data):
    return isRowValid(board,i,data) and isColumnValid(board,j,data) and isSquareValid(board,i,j,data)

def isRowValid(board,i,data):
    for i in board[i*9:i*9+9]:
        if(i==data):
            return False
    return True

def isColumnValid(board,j,data):
    for i in range(9):
        if(board[i*9+j]==data):
            return False
    return True

def isSquareValid(board,i,j,data):
    r=int(i/3)
    c=int(j/3)
    for i in range(3):
        for j in range(3):
            if(board[r*3*9+i*9+c*3+j]==data):
                return False
    return True



matT=[0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,     
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0]

mat=[0,0,0,0,5,7,0,8,0,
3,0,0,0,0,0,0,0,0,
0,0,2,9,0,0,4,0,0,
2,0,0,8,0,9,3,0,0,
4,0,0,0,0,0,0,0,7,     
0,0,7,4,0,6,0,0,8,
0,0,6,0,0,2,7,0,0,
0,0,0,0,0,0,0,0,5,
0,9,0,3,1,0,0,0,0]

mat1=[0,0,5,3,0,0,0,0,7,
0,0,0,0,0,8,0,0,6,
6,8,0,4,0,0,9,1,0,
0,0,0,0,0,7,0,0,0,
8,3,2,9,0,0,0,0,0,     
0,0,0,0,0,0,8,4,2,
0,2,0,0,0,3,0,0,0,
1,0,7,0,8,0,2,0,9,
0,9,0,0,1,0,0,7,0]

solvesudoku(mat)

solve(mat,0)





