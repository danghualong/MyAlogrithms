# 还没有被淹没的岛屿数
class Island(object):
    def calCount(self,nums):
        if(nums==None):
            return 0
        m=len(nums)
        if(m<=0):
            return 0
        n=len(nums[0])
        states=[False for i in range(m*n)]
        count=0
        for i in range(m):
            for j in range(n):
                size=self.countNumber(nums,states,i,j)
                count+=1 if size>0 else 0
        return count

    def countNumber(self,nums,states,i,j):
        m=len(nums)
        n=len(nums[0])
        if(states[i*n+j]):
            return 0
        states[i*n+j]=True
        if(nums[i][j]==0):
            return 0
        else:
            centered=True
            if(i>0):
                centered&=(nums[i-1][j]==1)
            if(i<m-1):
                centered&=(nums[i+1][j]==1)
            if(j>0):
                centered&=(nums[i][j-1]==1)
            if(j<n-1):
                centered&=(nums[i][j+1]==1)
            size=1 if centered else 0
            if(i>0):
                size+=self.countNumber(nums,states,i-1,j)
            if(i<m-1):
                size+=self.countNumber(nums,states,i+1,j)
            if(j>0):
                size+=self.countNumber(nums,states,i,j-1)
            if(j<n-1):
                size+=self.countNumber(nums,states,i,j+1)
            return size
obj=Island()
nums=[
    [1,1,1,0,0],
    [0,1,0,0,1],
    [0,0,1,1,0],
    [1,1,1,1,0],
    [0,1,1,0,0]
]
print(obj.calCount(nums))      
            