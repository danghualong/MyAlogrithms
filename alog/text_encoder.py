class Solution(object):
    def __init__(self):
        self.NUMS=['0','1','2','3','4','5','6','7','8','9']
    def decodeString(self, s):
        # 首先生成子串和数量的列表
        strArr=[]
        numArr=[]
        tmpCount=0
        startIndex=-1
        numStartIndex=-1
        if('[' not in s):
            return s
        for i in range(len(s)):
            # 当前没有括号
            if(tmpCount==0):
                if(s[i] not in self.NUMS):
                    # 解析数量
                    if(numStartIndex!=-1):
                        subNum=s[numStartIndex:i]
                        numArr.append(int(subNum))
                        numStartIndex=-1
                if(s[i] in self.NUMS):
                    # 数量开始的位置
                    if(numStartIndex==-1):
                        numStartIndex=i
                elif(s[i]=='['):# 重复字符开始的位置
                    startIndex=i
                    tmpCount+=1
                else:#剩下的字符
                    numArr.append(1)
                    strArr.append(s[i])
            else:
                # 嵌套的重复字符
                if(s[i]=='['):
                    tmpCount+=1
                elif(s[i]==']'):
                    tmpCount-=1
                    # 解析最外层嵌套字符串
                    if(tmpCount==0):
                        strArr.append(s[startIndex+1:i])
        print(numArr,strArr)
        text=''
        for i in range(len(numArr)):
            for j in range(numArr[i]):
                text+=self.decodeString(strArr[i])
        return text
        

obj=Solution()
s='100[leetcode]'
print(obj.decodeString(s))

        
