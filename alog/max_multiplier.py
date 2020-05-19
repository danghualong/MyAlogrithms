import math
# 计算连乘最大的值
class Solution(object):
    def calMax(self,nums):
        m=len(nums)
        result=[[0 for j in range(m)] for i in range(m)]
        for i in range(m):
            result[i][i]=nums[i]
        for i in range(1,m):
            for j in range(m-i):
                result[j][j+i]=max(nums[j+i]*result[j][j+i-1],result[j+1][j+i])
        print(result)


obj=Solution()
obj.calMax([2,-2,3,4])