# 获取包含偶数元音字母的子字符串最大长度
class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters='aeiou'
        count=len(s)
        marks=[]
        for i in range(count):
            if(i==0):
                t=0
            else:
                t=marks[i-1]
            ind=letters.find(s[i])
            if(ind!=-1):
                t=(t^(1<<ind))
            marks.append(t)
        print(marks)
        return self.getMaxRange(marks)
        
    def getMaxRange(self,marks):
        if(marks==None or len(marks)==0):
            return 0
        dict={}
        dict[0]=-1
        maxRange=0
        for i in range(len(marks)):
            if(marks[i] in dict):
                maxRange=max(maxRange,i-dict[marks[i]])
            else:
                dict[marks[i]]=i
        return maxRange


    
s="uoeetminicoworuep"
obj=Solution()
result=obj.findTheLongestSubstring(s)
print(result)
