class Solution(object):
    def deal(self,matrix):
        result=[]
        if(matrix==None or len(matrix)<=0):
            return result
        self.printResult(matrix,result,0,len(matrix[0])-1,0,len(matrix)-1)
        return result
    def printResult(self,mat,result,left,right,top,bottom):
        if(left>right or top>bottom):
            return
        if(top==bottom):
            for i in range(left,right+1):
                result.append(mat[top][i])
            return
        if(left==right):
            for j in range(top,bottom+1):
                result.append(mat[j][left])
            return
        for i in range(left,right):
            result.append(mat[top][i])
        for j in range(top,bottom):
            result.append(mat[j][right])
        for i in range(right,left,-1):
            result.append(mat[bottom][i])
        for j in range(bottom,top,-1):
            result.append(mat[j][left])
        self.printResult(mat,result,left+1,right-1,top+1,bottom-1)

mat=[[3,5,0,2],
     [4,9,9,6],
     [7,3,1,8],
     [4,2,1,9]]
    
obj=Solution()
arr=obj.deal(mat)
print(arr)
        

