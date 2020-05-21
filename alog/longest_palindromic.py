import numpy as np

class Solution(object):
    def getLongestPalindromic(self,s):
        m=len(s)
        result=np.zeros((m,m),dtype=int)
        if(m==0):
            return ''
        if(m==1):
            return s
        for i in range(m):
            result[i,i]=1
        for i in range(m-2,-1,-1):
            for j in range(i+1,m):
                t1=result[i,j-1]
                t2=result[i+1,j]
                t3=result[i+1,j-1]
                result[i,j]=max(t1,max(t2,t3))
                if(s[i]==s[j] and result[i+1,j-1]>=j-i-1):
                    result[i,j]=2+result[i+1,j-1]
                    
        stopIndex=0
        maxV=0
        for i in range(m):
            if(result[0,i]>maxV):
                stopIndex=i
                maxV=result[0,i]
        # print(result[0,:])
        startIndex=stopIndex-maxV+1
        return s[startIndex:stopIndex+1]

obj=Solution()
result=obj.getLongestPalindromic("babaddtattarrattatddetartrateedredividerb")
print(result)
result=obj.getLongestPalindromic("ac")
print(result)

result=obj.getLongestPalindromic("babadada")
print(result)

result=obj.getLongestPalindromic("abcdbbfcba")
print(result)

s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
result=obj.getLongestPalindromic(s)
# print(result)
print(len(result))
