import numpy as np
# 找到子序列片段点乘最大值
class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m=len(nums1)
        n=len(nums2)
        result=np.zeros((m,n),dtype=int)
        result[0,0]=nums1[0]*nums2[0]
        for i in range(m):
            for j in range(n):
                if(i==0 and j==0):
                    continue
                if(i==0):
                    result[i,j]=max(nums1[i]*nums2[j],result[i,j-1])
                elif(j==0):
                    result[i,j]=max(nums1[i]*nums2[j],result[i-1,j])
                else:
                    t1=max(0,result[i-1,j-1])+nums1[i]*nums2[j]
                    result[i,j]=max(t1,max(result[i-1,j],result[i,j-1]))
        print(result)
        return result[m-1,n-1]

obj=Solution()
nums1=[-3,-8,3,-10,1,3,9]
nums2=[9,2,3,7,-9,1,-8,5,-1,-1]
print(obj.maxDotProduct(nums1,nums2))