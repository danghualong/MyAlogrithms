import math
# s中覆盖t的最小子串
class Solution(object):
    def minWindow(self,s,t):
        if(s==None or t==None or len(s)==0 or len(t)==0):
            return ''
        freqMap={}
        for i in t:
            if(i in freqMap):
                freqMap[i]+=1
            else:
                freqMap[i]=1
        left=-1
        right=-1
        # t中还剩多少字母没有找到
        tsize=len(t)
        minCount=len(s)+1
        minStr=''
        while(left<=right):
            if(tsize>0):
                right+=1
                if(right>=len(s)):
                    break
                if((s[right] in freqMap)):
                    if(freqMap[s[right]]>0):
                        tsize-=1
                    freqMap[s[right]]-=1
            else:
                if(right-left<minCount):
                    minCount=right-left
                    minStr=s[left+1:right+1]
                left+=1
                if(s[left] in freqMap):
                    if(freqMap[s[left]]>=0):
                        tsize+=1
                    freqMap[s[left]]+=1
        return minStr
        
        
obj=Solution()
s="ADOBECODEBANC"
t="ABCK"
result=obj.minWindow(s,t)
print(result)

                
