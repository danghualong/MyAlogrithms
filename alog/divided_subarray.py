import numpy as np

class  Solution(object):
    # 返回能被k整除的连续子数组个数(O(n2))
    def getSize(self,A,K):
        m=len(A)
        result=np.zeros((m,m))
        total=0
        for i in range(m):
            for j in range(i,m):
                if(i==j):
                    result[i,j]=A[i]
                else:
                    result[i,j]=result[i,j-1]+A[j]
                if(result[i,j]%K==0):
                    total+=1
        return total
    # 返回能被k整除的连续子数组个数(前缀和方法O(n))
    def getSize2(self,A,K):
        s=[0 for i in range(len(A)+1)]
        dict={0:1}
        for i in range(len(A)):
            s[i+1]=s[i]+A[i]
            modNum=s[i+1]%K
            if(modNum in dict):
                dict[modNum]+=1
            else:
                dict[modNum]=1
        result=0
        for item in dict.values():
            result+=item*(item-1)/2
        return int(result)
        
        
nums=[1,2,3,4,5,-1,-2,3]
k=3
print(Solution().getSize(nums,k))
print(Solution().getSize2(nums,k)) 

 

