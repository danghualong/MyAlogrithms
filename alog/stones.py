class Solution(object):
    def piles(self,nums):
        n=len(nums)
        result=[[[0,0] for i in range(n)] for j in range(n)]
        for i in range(n):
            result[i][i][0]=nums[i]
        for k in range(1,n):
            for i in range(0,n-k):
                j=i+k
                result[i][j][0]=max(result[i][j-1][1]+nums[j],result[i+1][j][1]+nums[i])
                result[i][j][1]=min(result[i][j-1][0],result[i+1][j][0])
            print(result)    
obj=Solution()
obj.piles([5,3,3,4]) 
        
        
