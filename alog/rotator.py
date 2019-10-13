def isPost(ctrl,tup):
    if(tup[0]>ctrl[0]):
        return True
    elif(tup[0]==ctrl[0]):
        return tup[1]>ctrl[1]
    else:
        return False

class Solution(object):
    
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            arr=matrix[i]
            for j in range(n):
                if(isPost((i,j),(j,n-1-i)) and isPost((i,j),(n-1-i,n-1-j)) and isPost((i,j),(n-1-j,i))):
                    print(i,j)
                    tmp=matrix[i][j]
                    matrix[i][j]=matrix[n-1-j][i]
                    matrix[n-1-j][i]=matrix[n-1-i][n-1-j]
                    matrix[n-1-i][n-1-j]=matrix[j][n-1-i]
                    matrix[j][n-1-i]=tmp

s=Solution()
mat=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(mat)
print(mat)