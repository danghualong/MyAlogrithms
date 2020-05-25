import numpy as np
# 获取最长的回文字符串
class Solution(object):
    # Dynamic Plan
    def getLongestPalindromic(self,s):
        m=len(s)
        if(m==0):
            return ''
        if(m==1):
            return s
        result=np.zeros((m,m),dtype=int)
        for i in range(m):
            result[i,i]=1
        for i in range(m-2,-1,-1):
            for j in range(i+1,m):
                t1=result[i,j-1]
                t2=result[i+1,j]
                result[i,j]=max(t1,t2)
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
    # Scatter method
    def getLongestPalindromic2(self,s):
        m=len(s)
        if(m==0):
            return ''
        if(m==1):
            return s
        pstr_odd=self.getScatterMaxStr(s)
        pstr_even=self.getScatterMaxStr(s,True)
        return pstr_odd if len(pstr_odd)>len(pstr_even) else pstr_even
          
    def getScatterMaxStr(self,s,isEven=False):
        m=len(s)
        maxLen=0
        total=0
        pstr=''
        for i in range(m):
            left=i
            if(isEven):
                right=i+1
            else:
                right=i
            total=0
            while(True):
                if(left<0 or right>=m):
                    break
                if(s[left]==s[right]):
                    if(left==right):
                        total+=1
                    else:
                        total+=2
                    if(total>maxLen):
                        maxLen=total
                        pstr=s[left:right+1]
                    left-=1
                    right+=1
                else:
                    break    
        return pstr

obj=Solution()
s="babaddtattarrattatddetartrateedredividerb"
result1=obj.getLongestPalindromic(s)
result2=obj.getLongestPalindromic2(s)
print(result1,result2)
print(result1==result2)

s="ac"
result1=obj.getLongestPalindromic(s)
result2=obj.getLongestPalindromic2(s)
print(result1,result2)
print(result1==result2)

s="baaba"
result1=obj.getLongestPalindromic(s)
result2=obj.getLongestPalindromic2(s)
print(result1,result2)
print(result1==result2)

s="abcdbbfcba"
result1=obj.getLongestPalindromic(s)
result2=obj.getLongestPalindromic2(s)
print(result1,result2)
print(result1==result2)

s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
result1=obj.getLongestPalindromic(s)
result2=obj.getLongestPalindromic2(s)
print(result1,result2)
print(result1==result2)

