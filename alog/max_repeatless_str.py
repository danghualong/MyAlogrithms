# 无重复最长子串
class Solution(object):
    def getMaxLength(self,s):
        if(s==None or len(s)==0):
            return 0
        dict={}
        maxStr=''
        maxLen=0
        start=0
        stop=0
        while(stop<len(s)):
            if(s[stop] not in dict):
                dict[s[stop]]=1
                if(stop-start+1>maxLen):
                    maxLen=stop-start+1
                    maxStr=s[start:stop+1]
                stop+=1
            else:
                dict.pop(s[start])
                start+=1
        return len(maxStr)    

obj=Solution()
p=obj.getMaxLength("tmmzuxt")
print(p)
